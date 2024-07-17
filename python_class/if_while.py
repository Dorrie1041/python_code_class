# if
# age = int(input("Enter your age: \t"))
#
# if 0 <= age < 18:
#     print("You are a teenager")
# elif 18 <= age < 65:
#     print("You are worker")
# else:
#     print("You are older")

# num = int(input('please enter a number: \t'))
# result = f'current number is {num} is odd' if num % 2 != 0 else f'current number {num} is even'
# print(result)

# while / for

n = 0
my_sum = 0
while True:
    n += 1
    if n > 100:
        break
    if n % 2 == 0:
        continue
    my_sum += n

print(my_sum)

my_sum = 0
for n in range(100):
    if n % 2 == 0:
        continue
    my_sum += n

print(my_sum)

# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print(f'{col} * {row} = {col * row}', end='\t')
#         col += 1
#     print()
#     row += 1

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j} * {i} = {i * j}', end='\t')
    print()
