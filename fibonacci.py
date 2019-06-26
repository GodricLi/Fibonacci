# _*_ coding=utf-8 _*_


def fib(m):
    n, a, b = 0, 0, 1
    while n < m:
        yield b
        a, b = b, a + b

        n += 1


num = fib(10)
print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())