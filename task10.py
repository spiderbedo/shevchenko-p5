pincode = input()
if len(pincode) == 4:
    list_numbers = [i for i in pincode]
    set_numbers = set(list_numbers)
    if len(list_numbers) == len(set_numbers):
        if int(pincode) in range(1900, 2051):
            print("ERROR")
        else:
            print("OK")
    else:
        print("ERROR")
else:
    print("ERROR")
