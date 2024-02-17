s = input()
t = input()

# 全部の候補を列挙して、それぞれ入ってればOK
a = ["AB", "BC", "CD", "DE", "EA", "BA", "CB", "DC", "ED", "AE"]
b = ["AC", "AD", "BE", "BD", "CE", "CA", "DA", "EB", "DB", "EC"]

if (s in a and t in a) or (s in b and t in b):
    print("Yes")
else:
    print("No")
