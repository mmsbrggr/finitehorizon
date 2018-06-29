from config import INFINITY


def get_optimal_path_info(u, T):
    opt = None
    opt_t1 = None
    opt_t2 = None

    for t1 in range(0, T+1):
        for t2 in range(T, INFINITY):
            if t1 != t2:
                value = u[t1] + ((T - t1)/(t2 - t1)) * (u[t2] - u[t1])
                if opt is None or value <= opt:
                    opt = value
                    opt_t1 = t1
                    opt_t2 = t2

    return {'value': opt, 't1': opt_t1, 't2': opt_t2}
