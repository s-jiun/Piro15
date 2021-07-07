class OutOfRangeError(Exception):
    pass

num = 0
game_num = 0

while True:
    try:
        num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능)) :"))
        if num < 1 or num > 3:
            raise OutOfRangeError
    except ValueError:
        print("정수를 입력하세요")
        continue
    except OutOfRangeError:
        print("1,2,3 중 하나를 입력하세요")
        continue
    else:
        break

for i in range(num):
    game_num += 1
    print("PlayerA : {0}".format(game_num))

while True:
    try:
        num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능)) :"))
        if num < 1 or num > 3:
            raise OutOfRangeError
    except ValueError:
        print("정수를 입력하세요")
        continue
    except OutOfRangeError:
        print("1,2,3 중 하나를 입력하세요")
        continue
    else:
        break

for i in range(num):
    game_num += 1
    print("PlayerB : {0}".format(game_num))

