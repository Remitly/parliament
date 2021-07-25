import unittest
from nose.tools import raises, assert_equal, assert_true, assert_false
from icecream import ic

# import parliament
from parliament import analyze_policy_string, is_arn_match, is_arn_strictly_valid, is_glob_match
from parliament.statement import is_valid_region, is_valid_account_id
from parliament.cli import is_finding_filtered


class TestIsFindingFiltered(unittest.TestCase):
    """Test class for is_finding_filtered"""
    def get_policy(self):
        return analyze_policy_string(
            """
{
    "Version": "2012-10-17",
    "Id": "123",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "s3:abc",
        "Resource": [ "arn:aws:s3:::bucket/obj1", "arn:aws:s3:::bucket/obj2" ]
      }
    ]
 }
""",
            ignore_private_auditors=True,
        )

    def test_is_not_filtered(self):
        finding = self.get_policy().findings[0]
        finding.ignore_locations = []
        assert_false(is_finding_filtered(finding))

    def test_is_not_filtered_with_unrelated_action(self):
        finding = self.get_policy().findings[0]
        finding.ignore_locations = [{'Action': 's3:xyz'}]
        assert_false(is_finding_filtered(finding))

    def test_is_filtered_single_action(self):
        finding = self.get_policy().findings[0]
        finding.ignore_locations = [{'Action': 's3:abc'}]
        assert_true(is_finding_filtered(finding))

    def test_is_filtered_multiple_actions(self):
        finding = self.get_policy().findings[0]
        finding.ignore_locations = [{'Action': ['s3:abc', 's4']}]
        assert_true(is_finding_filtered(finding))

    def test_is_filtered_action_with_filepath(self):
        finding = self.get_policy().findings[0]
        finding.location["filepath"] = 'test.json'
        finding.ignore_locations = [
            {
                'Action': ['s3:abc', 's4'],
                'filepath': 'test.json'
            }
        ]
        assert_true(is_finding_filtered(finding))

# TODO debug those
    def test_is_filtered_single_action_with_single_resource(self):
        finding = self.get_policy().findings[0]
        finding.ignore_locations = [{'Action': 's3:abc', 'Resource': 'arn:aws:s3:::bucket/obj1'}]
        assert_true(is_finding_filtered(finding))

    def test_is_filtered_single_action_with_multiple_resource(self):
        finding = self.get_policy().findings[0]
        finding.ignore_locations = [{'Action': 's3:abc', 'Resource': ['arn:aws:s3:::bucket/obj1', 'arn:aws:s3:::bucket/not_a_finding']}]
        assert_true(is_finding_filtered(finding))
