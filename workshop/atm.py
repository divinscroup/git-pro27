balance = 1000

x = int(input('enter a value  to withdraw:\n'))
while x > 1000:
    x = int(input('enter a value  to withdraw:\n'))

request = x
while request > 0:
    if request >= 100:
        print 'gave 100'
        request -= 100
    elif request >= 50:
        print 'gave 50'
        request -= 50
    elif request >= 20:
        print 'gave 20'
        request -= 20
    elif request >= 10:
        print 'gave 10'
        request -= 10
    elif request >= 5:
        print 'gave 5'
        request -= 5
    elif request >= 2:
        print 'gave 2'
        request -= 2
    elif request >= 1:
        print 'gave 1'
        request -= 1
print 'your current balance is :' + str(balance - x)



