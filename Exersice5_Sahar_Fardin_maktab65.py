balance = 0
while True:
    _input = input("Input:")
    if _input == '-1':
        break
    info = _input.split()
    if info[0].upper() == "D":
        balance += int(info[1])
    elif info[0].upper() == "W":
        balance -= int(info[1])
    else:
        print("incorroct input")

print("Balance is: ", balance)       