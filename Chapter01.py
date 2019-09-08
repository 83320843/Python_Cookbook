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

# 你想解压一些元素后丢弃它们，你不能简单就使用 * ，但是你可以使用一
# 个普通的废弃名称，比如 _ 或者 ign
# record = ('ACME', 50, 123,45, (12,18,2012))
# name, *_, (*_, year) = record
# print(name)
# print(year)

# 使用星号进行递归算法
# items = [1, 10, 7, 4, 5, 9]
# head, *tail = items
# print(head)
# print(tail)

# def sum(items):
#     head, *tail = items
#     return head + sum(tail) if tail else head
# print(sum(items))
