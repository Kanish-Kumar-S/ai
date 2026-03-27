import math

def alphabeta(depth, node_index, alpha, beta, is_max, values, height):
    if depth == height:
        return values[node_index]

    if is_max:
        best = -math.inf
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, alpha, beta, False, values, height)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, alpha, beta, True, values, height)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]
height = 3

print("Alpha-Beta Result:", alphabeta(0, 0, -math.inf, math.inf, True, values, height))