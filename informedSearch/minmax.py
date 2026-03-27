import math

def minimax(depth, node_index, is_max, values, height):
    if depth == height:
        return values[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, values, height),
            minimax(depth + 1, node_index * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values, height),
            minimax(depth + 1, node_index * 2 + 1, True, values, height)
        )


values = [3, 5, 6, 9, 1, 2, 0, -1]
height = 3

print("Minimax Result:", minimax(0, 0, True, values, height))