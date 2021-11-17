dic = {}


def ADD(key, value):
    if key in dic:
        print("It's repetitious key!")
    else:
        dic[key] = value
        print("insert successfully!")


def REMOVE(key, value):
    if key in dic:
        if dic[key] == value:
            del dic[key]
            print("remove successfully")
        else:
            print("Wrong operation! ")
    else:
        print("the key is not in dictionary!")


print(dic)

for i in range(5):
    key = input("Enter a key: ")
    value = input(f"Enter a value for {key}: ")
    ADD(key, value)
for i in range(3):
    key = input("Enter a key: ")
    value = input(f"Enter a value for {key}: ")
    add_or_remove = input("add or remove: ")
    if add_or_remove.upper() == 'ADD':
        ADD(key, value)
    elif add_or_remove.upper() == 'REMOVE':
        REMOVE(key, value)

print(dic)
