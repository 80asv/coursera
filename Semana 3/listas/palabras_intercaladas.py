def intercalar(ca1: str, ca2: str)->str:
    res = ""
    palabra1 = ca1.split()
    palabra2 = ca2.split()

    for i in range(0, len(palabra1)):
        res += (palabra1[i]+" "+palabra2[i]+" ")
    return res


r = intercalar("andres felipe", "sanabria velasquez")

print(r)