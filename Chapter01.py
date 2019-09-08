# 迭代为可变长元组
# records = [
# ('foo', 1, 2),
# ('bar', 'hello'),
# ('foo', 3, 4),
# ]
# def do_foo(x, y):
#     print('foo', x, y)
#
# def do_bar(s):
#     print('bar', s)
#
# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#             do_bar(*args)

# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割
# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(':')
# print(uname)
# print(fields)
# print(homedir)
# print(sh)

