def es_divisible(n: int, d: int) -> int:
    if n%(2*d) == 0:
        res = 2
    elif not (n%(2*d) == 0) and n%d == 0:
        res = 1
    else:
        res = 0

    return res


print(es_divisible(5, 0))