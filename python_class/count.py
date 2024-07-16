# // 整除
# ** 指数

a = 17
print(a % 2)
print(2 ** 2)
print(8 ** (1 / 2))  # 根号 8

print(pow(8, 1 / 3))  # 立方

x = 13

x += 2 * 4
# x = 2 * 4 + x

one = 11
two = 12
print((one == two))

# example

h = float(input("Please enter your height:\t "))
w = float(input("Please enter your weight:\t "))

if (h > 0) and (w > 0):
    bmi = w / pow(h, 2)
    print(f'height: {h}, weight: {w}, ', end='')
    print('BMI: %.2f' % bmi)

# \n: 换行
# \t: 制表
