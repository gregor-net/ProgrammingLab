print("538 minuti nel formato h : min :  ")

x = 538
y = x % 60
x = (x - y )/60

print(str(x) + "h:" + str(y) + "min")

print("l' equivalente di 538 minuti è {}h:{}min".format(538//60, 538%60))