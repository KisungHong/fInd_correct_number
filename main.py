import random

random_number = random.randint(1, 100)
# print(random_number)

game_count = 1

while True :
    try:
        my_number = int(input("1~100 사이의 숫자를 입력하시오 : "))
        if my_number > random_number :
            print('다운')
        elif my_number < random_number :
            print('업')
        elif my_number == random_number :
            print(f"축하해요. {game_count}회 만에 맞췄어요")
            break
        game_count += 1

    except :
        print("에러발생, 숫자를 입력하시오")