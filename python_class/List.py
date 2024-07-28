lst = [12, 'ab', 3.14, 'ab']

print(lst[1:3])

# 查找
print(lst.count('ab'))
print(lst.index(12))
print(len(lst))

lst.append([1, 2])
print(lst)
lst.extend([1, 4, 'hello'])
print(lst)
lst.insert(lst.index('ab'), 13)
print(lst)

# lst.pop(lst.index('ab'))
print(lst)
