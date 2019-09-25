# In Windows Active Directory, a group can consist of user(s) and group(s) themselves. 
# We can construct this hierarchy as such. Where User is represented by str representing their ids.

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.users:
        return True

    for sub_group in group.groups:
        return is_user_in_group(user, sub_group)

    return False


def test(scenario, result, expected):
	separator = "-------------------------"
	scenario = "Scenario: " + scenario
	status = "Status: PASS" if result is expected else "Status: FAIL"
	result_str = "Result: " + str(result)
	expected_str = "Expected: " + str(expected)

	print(scenario)
	print(result_str)
	print(expected_str)
	print(status)
	print(separator)


def run_tests():
    #Level 1
    root = Group("root")
    root_user = "root_user"
    root.add_user(root_user)

    #Level 2
    child1 = Group("child")
    child2 = Group("child2")

    #Level 3
    child1_child = Group("subchild")
    child1_child_user = "child1_child_user"
    child1_child.add_user(child1_child_user)

    orphaned_user = "orphaned_user"
    
    child1.add_group(child1_child)

    root.add_group(child1)
    root.add_group(child2)

    test("child1_child_user is in child1_child", is_user_in_group("child1_child_user", child1), True)
    test("child1_child_user is in child1_child group", is_user_in_group("child1_child_user", child1_child), True)
    test("child1_child_user is not in child2 group", is_user_in_group("child1_child_user", child2), False)
    test("root_user is in root group", is_user_in_group("root_user", root), True)

    orphaned_user_in_no_group = is_user_in_group("orphaned_user", root) and is_user_in_group("orphaned_user", child1) and is_user_in_group("orphaned_user", child1_child)

    test("orphaned user is in no group", orphaned_user_in_no_group, False)

run_tests()