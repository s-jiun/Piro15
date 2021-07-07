class OutOfRangeError(Exception):
    pass

num = 0

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
    print("PlayerA : {0}".format(i+1))
