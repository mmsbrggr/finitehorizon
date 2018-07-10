def get_utility_sequence(utility_matrix, path):
    u = [(0, 0)]
    for edge in path:
        value_0 = u[-1][0] + utility_matrix[edge[0]][edge[1]][0]
        value_1 = u[-1][1] + utility_matrix[edge[0]][edge[1]][1]
        u.append((value_0, value_1))
    return u
