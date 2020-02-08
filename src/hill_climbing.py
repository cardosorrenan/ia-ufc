from assist_hill_climbing import *


local_max, path = [], []
n_searches = get_n_searches()

for search in range(1, n_searches+1):
    current_node = throw_node_field()
    while True:
        path.append([search, round(current_node.x, 2), round(current_node.y, 2), round(current_node.value, 6)])
        neighbors = calc_neighbors(current_node)
        values_climbs = [node.value for node in neighbors]
        value_max_climb = max(values_climbs)
        if not any((x_y <= -20 or x_y >= 20) for x_y in [current_node.x, current_node.y]):
            if current_node.value <= value_max_climb:
                for nb in neighbors:
                    if nb.value == value_max_climb:
                        current_node = nb
            else:
                cont = 0
                for t in path:
                    if t[0] == search:
                        cont += 1
                local_max.append([search, current_node.x, current_node.y, current_node.value])
                print("-- Search nº{}: X: {}, Y: {}, Value: {} - Steps: {}".format(search, round(current_node.x, 2), round(current_node.y, 2), round(current_node.value, 6), cont))
                break
        else:
            print("-- Search nº{}: The search found the limit (-20 < x,y < 20)".format(search))
            break

i_global_max = find_print_global_max(local_max)
plot_result(i_global_max, path)

