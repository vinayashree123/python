# with open('file.txt','w') as file:
#     file.write('hi hello\npython\nc program\nappium')
#
# with open('file.txt','r') as file:
#     last_line = file.readlines()[-2:]
#     for line in last_line:
#         print(line.strip())
#
# with open('file.txt','r') as file:
#     last_line = file.read()
#     line = last_line[::-1]
#     with open('write.txt','w')as file:
#         file.write(line)
#
# with open('file.txt','r') as file:
#     last_line = file.read()
#     word = last_line.split()
#     print(len(word))

# def count_vowels(fname):
#     with open(fname,'r') as file:
#         data = file.read()
#         vowels = 'aeiouAEIOU'
#         count = 0
#         for char in data:
#             if char in vowels:
#                 count += 1
#         return count
# print(count_vowels('file.txt'))

# def reverse(num):
#     rev_num = 0
#     while num > 0:
#         d = num % 10
#         rev_num = (rev_num * 10) + d
#         num //= 10
#     return rev_num
#
#
# def func(reverse, list1):
#     new_list = []
#     for word in list1:
#         if type(word) == str:
#             new_list.append(word)
#         elif type(word) == int:
#             # word1 = str(word)
#             new_list.append(reverse(word))
#     return new_list
#
#
# list_1 = ['hi', 123, 'hello', 567]
# print(func(reverse, list_1))
#
#
# # using decoratpr
# def decor(func):
#     def inner(*args):
#         res = func(*args)
#         if res < 0:
#             return abs(res)
#         return res
#     return inner
# @decor
# def sub(a, b):
#     return a - b
# print(sub(10, 5))
# print(sub(20,10))
# print(sub(5,10))


#generators

# def generator(list):
#     for i in list:
#         yield i
#
# list = [10,20,30]
# res = generator(list)
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))

#iterator is object which iterates the iterable objects
# list = [10,20,30]
# iter1 = iter(list)
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))

import pickle
data = {'name':'veena','age':21}
with open('pickle.pkl','wb') as file:
    pickle.dump(data,file)

with open('pickle.pkl','rb') as file:
    r = pickle.load(file)
    print(r)

dict = {'name':'veeena','age':21}
s = {k:v for v,k in dict.items()}
print(s)


