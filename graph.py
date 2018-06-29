def get_utility_sequence(utility_matrix, path):
    u = [0]
    for edge in path:
        u.append(u[-1] + utility_matrix[edge[0], edge[1]])
    return u
