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
        "Resource": "*"
      }
    ]
 }
""",
            ignore_private_auditors=True,
        )

    def test_is_filtered_single_action(self):
        finding = self.get_policy().findings[0]
        finding.ignore_locations =  [{'actions': 's3:abc'}]
        assert_true(ic(is_finding_filtered(finding)))

    def test_is_filtered_multiple_actions(self):
        finding = self.get_policy().findings[0]
        finding.ignore_locations =  [{'actions': ['s3:abc', 's4']}]
        assert_true(ic(is_finding_filtered(finding)))
