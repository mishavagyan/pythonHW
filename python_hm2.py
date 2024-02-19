# Exercise: Number Classification
# nums = input("Please enter numbers separated with spaces: ").split()
# my_list = [int(i) for i in nums]
# print(my_list)

# def classify_numbers(nums_list):
#     even = []
#     odd = []
#     for num in nums_list:
#         even.append(num) if num % 2 == 0 else odd.append(num)
#         # if num % 2 == 0:
#         #     even.append(num)
#         # else:
#         #     odd.append(num)
#     return even, odd

# even, odd = classify_numbers(my_list.copy())
# print("Even:", even, "\nOdd:", odd)


# Exercise: Sum of Elements

# nums = input("Please enter numbers separated with spaces: ").split()
# my_list = [int(i) for i in nums]
# answer = input("Do you want to exclude negative numbers (yes / no)? ")

# if answer == "yes":
#     answer = True
# else: 
#     answer = False

# def sum_of_elements(nums_list, exclude_negative = False):
#     res = 0
#     if(exclude_negative == False):
#         for num in nums_list:
#             res += num
#     else:
#         for num in nums_list:
#             if(num >= 0):
#                 res += num
#     return res

# print(sum_of_elements(my_list.copy(), exclude_negative = answer))
# print(sum_of_elements(my_list.copy(), exclude_negative = not answer))