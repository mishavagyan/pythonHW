# ################################
# ################################
# ######## ## first way ###########
# ################################
# ################################
# operations with only two numbers
num1 = eval(input("Enter first number: "))
op = input("Enter operation: ")
num2 = eval(input("Enter second number: "))

if op == "+":
    print("Result is:", num1 + num2)
elif op == "-":
    print("Result is:", num1 - num2)
elif op == "*":
    print("Result is:", num1 * num2)
elif op == "/" and num2 != 0:
    print("Result is:", num1 / num2)
else:
    print("Invalid operacion")

# ##############################
# ##############################
# ######## second way ##########
# ##############################
# ##############################

# but if expr is 12 + 3 * 5 it will do 12+3=15*5=75

# expr = input("Enter the expression with spaces: ").split(" ")
# i = 1
# res = eval(expr[0])
# while i < len(expr):
#     if expr[i] == "+":
#         res += eval(expr[i+1])
#     elif expr[i] == "-":
#         res -= eval(expr[i+1])
#     elif expr[i] == "*":
#         res *= eval(expr[i+1])
#     elif expr[i] == "/" and expr[i+1] != "0":
#         res /= eval(expr[i+1])
#     else:
#         print("Invalid operacion")
#         break
#     i += 2

# if i >= len(expr):
#     print(res)



# ##############################
# ##############################
# ######## third way ##########
# ##############################
# ##############################
# if expr is 12 + 3 * 5 it will do 3 * 5 = 15; 15 + 12 = 27

# expr = input("Enter the expression with spaces: ").split(" ")
# i = 1
# while i < len(expr):
#     if expr[i] == "*":
#         expr[i-1] = str(eval(expr[i-1]) * eval(expr[i+1]))
#         expr.pop(i+1)
#         expr.pop(i)
#     elif expr[i] == "/" and expr[i+1] != "0":
#         expr[i-1] = str(eval(expr[i-1]) / eval(expr[i+1]))
#         expr.pop(i+1)
#         expr.pop(i)
#     elif expr[i] == "/" and expr[i+1] == "0":
#         print("Invalid operacion")
#         break
#     i += 2

# res = eval(expr[0])
# i = 1
# while i < len(expr):
#     if expr[i] == "+":
#         res += eval(expr[i+1])
#     elif expr[i] == "-":
#         res -= eval(expr[i+1])
#     i += 2


# if i >= len(expr):
#     print(res)


# ##############################
# ##############################
# ######## fourth way ##########
# ##############################
# ##############################

# print(eval(input("Enter expr: ")))