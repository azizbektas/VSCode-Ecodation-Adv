# region rekursif_oncesi_hatirlatma_pratigi
"""

"""

# n = 5
# f = 1
# while n>0:
#     f *= n
#     n -= 1
# print(f)
# endregion

# region rekursif_konsepti
"""

"""


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n-1)


print(faktoriyel(5))
# endregion
