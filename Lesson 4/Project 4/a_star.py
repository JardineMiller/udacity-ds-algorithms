import math

class NodeCoords:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

class Node:
    def __init__(self, intersection_num, coords, parent = None):
        self.intersection = intersection_num
        self.parent = parent
        self.coords = NodeCoords(coords)
        
        self.g_cost = 0
        self.h_cost = 0
    
    @property
    def f_cost(self):
        return self.g_cost + self.h_cost

    def __eq__(self, other):
        if not isinstance(other, Node):
            raise ValueError("Can't compare two objects of different types")
            
        return self.intersection == other.intersection

    def __hash__(self):
        return hash(self.intersection)

def calculate_cost(start_node, end_node):
    x_diff = (end_node.coords.x - start_node.coords.x) ** 2
    y_diff = (end_node.coords.y - start_node.coords.y) ** 2

    return math.sqrt(x_diff + y_diff)

def priority_sort(node_list):
    return sorted(node_list, key = lambda node:node.f_cost)

def shortest_path(map, start_intersection, end_intersection):
    """Returns a list of ints representing the path between the start_node and end_node"""

    start_node = Node(start_intersection, map.intersections[start_intersection])
    end_node = Node(end_intersection, map.intersections[end_intersection])

    open_list = []
    closed_list = []
    
    open_list.append(start_node)

    while len(open_list):
        # Re-sort the list so we retain priority
        open_list = priority_sort(open_list)

        current_node = open_list.pop(0)
        closed_list.append(current_node)

        # If we have found the end, return the path
        if (current_node == end_node):
            path = []
            while current_node is not None:
                path.append(current_node.intersection)
                current_node = current_node.parent

            path.reverse()
            return path

        connected_intersections = map.roads[current_node.intersection]

        for intersection in connected_intersections:
            connected_node = Node(intersection, map.intersections[intersection], current_node)

            if connected_node in closed_list:
                continue
            
            connected_node.g_cost = calculate_cost(current_node, connected_node) + current_node.g_cost
            connected_node.h_cost = calculate_cost(connected_node, end_node)

            if connected_node in open_list:
                index = open_list.index(connected_node)
                assessed_node = open_list[index]
                if assessed_node.f_cost < connected_node.f_cost:
                    continue
                else:
                    open_list.pop(index)
        
            open_list.append(connected_node)


def test(scenario, result, expected):
	separator = "-------------------------"
	scenario = "Scenario: " + scenario
	status = "Status: PASS" if result == expected else "Status: FAIL"
	result_str = "Result: " + str(result)
	expected_str = "Expected: " + str(expected)

	print(scenario)
	print(result_str)
	print(expected_str)
	print(status)
	print(separator)

def test_coords():
    coords1 = NodeCoords([2,5])
    coords2 = NodeCoords([2,5])
    coords3 = NodeCoords([1,5])

    test("Two different coord objects with diff values are not the same", coords1 == coords3, False)
    test("Compare the same object is the same", coords1 == coords1, True)
    test("Two different coord objects with same values are the same", coords1 == coords2, True)

def test_node_props():
    node1 = Node(1, [0, 1])
    test("Node should start with g_cost of 0", node1.g_cost, 0)
    test("Node should start with h_cost of 0", node1.h_cost, 0)
    test("Node should start with f_cost of 0", node1.f_cost, 0)

    node1.g_cost = 5
    test("Node g_cost should reflect change to g_cost", node1.g_cost, 5)
    test("Node f_cost should reflect change to g_cost", node1.f_cost, 5)

def test_shortest_path():
    path1 = shortest_path(map, 5, 34)
    test("Shortest path (5, 34) is correct", path1, [5, 16, 37, 12, 34])

    path2 = shortest_path(map, 5, 5)
    test("Shortest path (5, 5) is correct", path2, [5])

    path3 = shortest_path(map, 8, 24)
    test("Shortest path (8, 24) is correct", path3, [8, 14, 16, 37, 12, 17, 10, 24])


# test_coords()
# test_node_props()
test_shortest_path()

