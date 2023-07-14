def find_direct_routes_map():
    direct_routes_full_map = []
    for tree in trees_coordinates:
        direct_routes = []

        for other_tree in trees_coordinates:
            if other_tree != tree:
                distance = tree_distance(other_tree, tree)
        
                if distance <= vine_length:
                    direct_routes.append(other_tree)

        direct_routes_full_map.append(direct_routes)
    return direct_routes_full_map

def tree_distance(other_tree, tree):
    return ((other_tree[X] - tree[X]) ** 2 + (other_tree[Y] - tree[Y]) ** 2) ** 0.5

trees_quant, vine_length = map(int, input().split())
trees_coordinates = []
stop = False 

X = 0
Y = 1

for i in range(trees_quant):
    trees_coordinates.append(list((map(int, input().split()))))

direct_routes_full_map = find_direct_routes_map()

for tree in trees_coordinates:

    i = 0
    while i < len(trees_coordinates):
        other_tree = trees_coordinates[i]
        if other_tree != tree:
            distance = tree_distance(other_tree, tree)

            if distance <= vine_length:
                print()
        
                

    


   