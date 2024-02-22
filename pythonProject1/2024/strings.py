# def sort_key(name):
#     name = name.split()
#     last_name = name[-1]
#     return last_name
# names = ['steve jobs', 'bill gates', 'john doe', 'tim cook', 'laura turner', 'alex martin']
# print(sorted(names, key=sort_key))
#
# #reverse string
# def reverse(str):
#     s = ''
#     for i in str:
#         s = i + s
#     return s
# str = 'hello'
# print(reverse(str))
# print(str[::-1])
# print(''.join(reverse(str)))
#
# def reverse(str):
#     index = len(str)-1
#     s = ''
#     while index >= 0:
#         s = s + str[index]
#         index -= 1
#     return s
# str = 'vina'
# print(reverse(str))
#
# #count vowels
# def count_vowels(str):
#     v = 'aeiouAEIOU'
#     c = 0
#     for i in str:
#         if i in v:
#             c += 1
#     return c
# str = 'hi hello'
# print(count_vowels(str))
#
# def count_consonents(str):
#     v = 'aeiouAEIOU'
#     c = 0
#     for i in str:
#         if i not in v:
#             c += 1
#     return c
# str = 'hi hello'
# print(count_consonents(str))
#
# def count_word(str):
#     word = str.split()
#     return len(word)
# str = 'hi hello'
# print(count_word(str))
#
# def cap_word(str):
#     data = str.split()
#     list = []
#     for word in data:
#         list.append(word.capitalize())
#     return ' '.join(list)
# print(cap_word('hi hello How are you'))
#
# #remove duplicate
# def rem_dup(str):
#     s = ''
#     for i in str:
#         if i not in s:
#             s = s + i
#     return s
# print(rem_dup('hiii helllo'))
#
# def rem_dup_word(str):
#     s = ''
#     for i in str.split():
#         if i not in s:
#             s = s + ' ' + i
#     return s
# print(rem_dup_word('hi hello hi how are you'))
#
# #count nor of occurace of character
# str = 'hi hello veena how'
# char = 'h'
# c = 0
# for i in str:
#     if i == char:
#         c += 1
# print(c)
#
# #nor occurance of each char
# str = 'hi hello veena how'
# dict = {}
# for i in str:
#     if i != ' ':
#         dict[i] = dict.get(i,0)+1
# print(dict)
#
# #without in built convert to lower
# def lower(str):
#     res = ''
#     for char in str:
#         if 'A' <= char <= 'Z':
#             res += chr(ord(char)+32)
#         else:
#             res += char
#     return res
# print(lower('Hello HoW'))
#
# def swap(str):
#     res = ''
#     for char in str:
#         if 'a' <= char <= 'z':
#             res += chr(ord(char)-32)
#         elif 'A' <= char <= 'Z':
#             res += chr(ord(char)+32)
#         else:
#             res += char
#     return res
# print(swap('heLLo HoW'))
#
#
# def upper(str):
#     res = ''
#     for char in str:
#         if 'a' <= char <= 'z':
#             res += chr(ord(char)-32)
#         else:
#            res += char
#     return res
# print(upper('heLLo HoW'))


# longest common prefix
def long_prefix(strs):
    if not strs:
        return strs
    strs.sort()
    # print(strs)
    first_char = strs[0]
    last_char = strs[-1]
    prefix = ''
    for i in range(len(first_char)):
        if i < len(first_char) and first_char[i] == last_char[i]:
            prefix += first_char[i]
    return prefix


strs = ["flower", "flow", "flight"]
print(long_prefix(strs))


# stack
def isValid(str):
    stack = []
    dict = {')': '(', '}': '{', ']': '['}
    for char in str:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if not stack or stack.pop() != dict[char]:
                return False
        else:
            return False
    return not stack

print(isValid("()"))
