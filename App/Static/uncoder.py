def uncoder(a: str):
    res = []
    nums = []
    v = a.split(",")
    text = [t for t in v if "-" in t]
    v = [int(i) for i in v if "-" not in i]
    for n in text:
        idx = n.split("-")
        nums = list(range(int(idx[0]), int(idx[1]) + 1))
        res += nums
    res = v + res
    res.sort()
    return res
