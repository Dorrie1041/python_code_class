s1 = 'hello'
s2 = "hello"
s3 = """hello
world"""
s4 = '''hello'''

s5 = 'hello\nword'

s6 = 'I\'m Tom'

s7 = 'make string "strong"'

print(s1[1])
print(s7[2])

s = 'abcefghijk'

print(s[2:6:1])
print(s[2:6])
print(s[-8:-4])
print(s[:4])
print(s[5:])

print(s[::-1])

ss = 'hellopythonword'

print(ss.find('py'))
print(ss.index('py'))

# 切割
sss = 'I am a student'
print(sss.split(' '))  # 分隔符不会在结果中出现
print(sss.partition(' '))  # 分区： 分隔符单独一个区

print(sss.replace('student', 'teacher'))
