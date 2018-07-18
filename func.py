# #Function
# def my_test_func(num1, num2):
#     if type(num1)==type(num2):
#         return num1+num2
#     else:
#         print("Please input the same type!")

# result = my_test_func('2','a')
# print(result)


# #Filter

# l = [1, 2, 3, 4, 5, 6]
# def even_num(num):
#     return num%2==0
# print(len(filter(even_num,l))) #count even numbers
  
# evens=filter(even_num,l)

# evens=filter(lambda num:num%2==0, l)  #lambdaExpression
 
# print(list(evens))

#problem1
# def arrayCheck(nums):
#     for i in range(len(nums)-2):
#         if ((1 == nums[i]) and (2 == nums[i+1]) and (3 == nums[i+2])):
#             return True
#     return False

# test=[1,2,3,1,1,2]
# x=arrayCheck(test)
# print(x)


#problem2
# string1='Helloollasl'
# def stringBits(string):
#     result =''
#     for i in range(len(string)):
#         if i%2==0:
#             result+=string[i]
#     print(result)

# stringBits(string1)


