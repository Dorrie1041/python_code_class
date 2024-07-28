set1 = {101, 87, 3.14, 'abcde'}
print(len(set1))

set1.add(99)
print(set1)

set1.remove('abcde')
print(set1)

set2 = {'hello', (100, 200)}
print(set2)

# 可变  && 不可变
s1 = 'hello, world'
print(id(s1))
s1 = 'abc'

print(id(s1))
print('-' * 30)
lst = [100, 200, 300, 400]
print(id(lst))
lst.append(500)
print(id(lst))
