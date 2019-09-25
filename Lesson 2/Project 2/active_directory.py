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
    return None

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

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

root_group_user = "root_user"
sub_child_user = "sub_child_user"
orphaned_user = "orphaned_user"

sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)

test("sub_child groups contains user: sub_child_user returns true", is_user_in_group("sub_child_user", sub_child), True)
test("sub_child_user is not in root group", is_user_in_group("sub_child_user", parent), False)

test("root_user is in root group", is_user_in_group("root_user", parent), True)

test("orphaned user is in no group", is_user_in_group("orphaned_user", parent), False)
test("orphaned user is in no group", is_user_in_group("orphaned_user", child), False)
test("orphaned user is in no group", is_user_in_group("orphaned_user", sub_child), False)