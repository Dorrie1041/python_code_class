from decimal import Decimal

# name = input("welcome! please enter your name: ")
# print("welcome back! ", name)

# transfer
# number = input("please enter your number: ")
# number = int(number)
# print(type(number))

# float(x)
# str(x)

# %s : str and number
# %d : int
# %f: float

my_name = 'Dorrie'
my_age = 23
my_city = "Wuhan"

print('my name is %s, and my age is %d, my city is %s' % (my_name, my_age, my_name))

# 特殊的格式化
money = 8923
num = 1.71

# 保留5位小数
print('my income is : %5d' % money)

# 精确到小数点后一位
print('%.1f' % num)

num02 = 22.345
# 精确到小数点后二位 : 22.35
print('%.2f' % num02)

# 精确的四舍五入
print(Decimal(str(num02)).quantize(Decimal('0.00'), rounding='ROUND_HALF_UP'))

# f-string f'{}'
print(f'my name is{my_name} , and my age is {my_age + 1}, my city is {my_city}')
