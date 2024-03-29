import random

class OutOfRangeError(Exception):
    pass

def brGame():
    num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능)) :"))
    if num < 1 or num > 3:
        raise OutOfRangeError
    return num

num = 0
game_num = 0

while game_num < 31:
    
    num = random.randint(1,3)

    for i in range(num):
        game_num += 1
        print("computer : {0}".format(game_num))
        if game_num == 31:
            break
        
    if game_num == 31:
        print("player win!")
        break

    while True:
        try:
            num = brGame()
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
        print("player : {0}".format(game_num))
        if game_num == 31:
            break
        
    if game_num == 31:
        print("computer win!")
        break
