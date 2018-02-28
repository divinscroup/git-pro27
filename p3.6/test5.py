def sqr_nums(num):
    for i in num:
        yield (i * i)


my_nums = sqr_nums([1, 2, 3, 4, 5, 6])
for num in my_nums:
    print(num)
my_num = (x * x for x in [1, 2, 3, 4, 5])
print(list(my_num))
