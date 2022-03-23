def aa():
    n = 5
    print('11111')
    for i in range(5):
        print(i)
        yield i

i = aa()
print(next(i))
i = aa()
print(i)
