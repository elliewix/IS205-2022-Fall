# gameif (game == 'true') or (game == 'dare'):

ans1 = 1
ans2 = '1'


# print(1 + '1')


# print("line 10", "ans1", type(ans1), "ans2", type(ans2))
# print(ans1 + ans2)
# print("hello from 12")

isRaining = False
isSnowing = False
isWindy = True
isSick = False

if any([isRaining, isSnowing, isWindy, isSick]):
    print("not gonna happen")
else:
    print('get your bike out')

x = 1
y = 2

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
