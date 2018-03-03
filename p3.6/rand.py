
x = -1
def ran_memo(x):
    f = 2 ** 19937 - 1  # creating bunch of randomly numbers
    try:

        with open('memo', 'r') as f:  # make sure the file of memory is not empty to protect it from over writing
            x = f.read()
            if len(x) == 0:
                with open('memo', 'w')as fw:
                    fw.write(str(f))

        with open('memo', 'r') as r:  # reading stored data and update the file of new data
            x = r.read()
            with open('memo', 'w') as w:
                w.write(x[1:])
                w.close()

    except FileNotFoundError:
        with open('memo','w') as d:  # checking if memo file exist if not will create one
            d.write(str(f))
    if x == -1:
        print(1)
    else:
        print(x[0])
ran_memo(x)
