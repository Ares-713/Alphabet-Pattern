def add(num1, num2):
    return int(num1 + num2)

def sub(num1, num2):
    return int(num1 - num2)

def mul(num1, num2):
    return int(num1 * num2)

def div(num1, num2):
    return num1 / num2

def flr(num1, num2):
    return int(num1 // num2)

def exp(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2

def calc(string = input("Enter equation to evaluate: ")):
    sign_list = []
    num_list = []
    i4 = 0

    for i1 in range(len(string)):
        if string[i1] in ["+", "-", "*", "/"]:
            if string[i1+1] in ["*", "/"]:
                sign_list.append(string[i1:i1+2])
                num_list.append(string[i4:i1])
                i4 = i1 + 1
            else:
                sign_list.append(string[i1])
                num_list.append(string[i4:i1])
                i4 = i1 + 1
    num_list.append(string[i4 - i1 - 1:])
    num = []

    for j in range(len(num_list)):
        if num_list[j] != '':
            num.append(int(num_list[j]))

    symbl_list = sign_list[::]
    i3 = 1

    for i2 in range(len(sign_list)-1):
        if sign_list[i2] in ["**", "//"]:
            del symbl_list[i2+i3]
            i3 -= 1

    j1 = 0
    while "**" in symbl_list:
        if symbl_list[j1] == "**":
            num[j1] = exp(num[j1], num[j1+1])
            del num[j1+1]
            del symbl_list[j1]
            j1 -= 1
        j1 += 1

    j2 = 0
    while "//" in symbl_list or "*" in symbl_list or "/" in symbl_list:
        if symbl_list[j2] == "//":
            num[j2] = flr(num[j2], num[j2+1])
            del num[j2+1]
            del symbl_list[j2]
            j2 -= 1
        elif symbl_list[j2] == "*":
            num[j2] = mul(num[j2], num[j2+1])
            del num[j2+1]
            del symbl_list[j2]
            j2 -= 1
        elif symbl_list[j2] == "/":
            num[j2] = div(num[j2], num[j2+1])
            del num[j2+1]
            del symbl_list[j2]
            j2 -= 1
        elif symbl_list[j2] == "%":
            num[j2] = mod(num[j2], num[j2+1])
            del num[j2+1]
            del symbl_list[j2]
            j2 -= 1
        j2 += 1

    j3 = 0
    while "+" in symbl_list or "-" in symbl_list:
        if symbl_list[j3] == "+":
            num[j3] = add(num[j3], num[j3+1])
            del num[j3+1]
            del symbl_list[j3]
            j3 -= 1
        elif symbl_list[j3] == "-":
            num[j3] = sub(num[j3], num[j3+1])
            del num[j3+1]
            del symbl_list[j3]
            j3 -= 1
        j3 += 1

    print("The answer is:", num[0])         

calc()
