num = int(input())
list = [2, 3, 4]
list_2 = [0, 5, 6, 7, 8, 9]
if num % 10 == 1:
    print(num, "попугай")
elif num % 10 in list:
    print(num, "попугая")
elif num % 10 in list_2:
    print(num, "попугаев")
