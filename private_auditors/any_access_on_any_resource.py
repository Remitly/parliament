import re
from parliament import is_arn_match, expand_action, is_glob_match
from parliament.misc import listify

def is_permissive(string):
    # return regex match or None
    return re.match("\w+:\*", string) or re.match("\*", string) or re.match("\*:\*", string)

def audit(policy):
    for statement in policy.policy_json.Statement():
        actions = listify(statement['Action'])
        resources = listify(statement['Resource'])
        for action in actions:
            for resource in resources:
                # import code; code.interact(local=dict(globals(), **locals()))
                # if is_arn_match("object", "", action) :
                if is_permissive(action) and is_permissive(resource):
                    policy.add_finding("CUSTOM_PERMISSIVE_ACTION", location={"action": action, "resource": resource})
