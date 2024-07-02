import random

min = 1
max = 100

while True: # 업다운 알고리즘과 재시작 여부 입력까지 모두 포함한 반복문으로 재시작 여부에서 N할 시 중단됨
    target = random.randint(min, max)
    trying = 0 # 정답을 맞출때까지 시도횟수, 재시작 시 초기화되도록 반복문 안에 넣음

    # 업다운 알고리즘
    while True:
        user = input("숫자를 입력하세요: ")
        if not user.isdecimal():        
            print("숫자가 아닙니다")
        elif int(user) < min or int(user) > max:
            print("유효한 범위 내의 숫자를 입력하세요 (1~100)")
        elif target > int(user):
            trying += 1
            print("[업]")
        elif target < int(user):
            trying += 1
            print("[다운]")
        elif target == int(user):
            print("\n****    정답    ****\n시도횟수: " + str(trying))
            break


   
   # 정답을 맞춰 break 시 재시작 여부를 물음
    while True:
        retry = input("다시 하시겠습니까? Y/N (이외 문자는 Y로 인식합니다)\n")
        if retry.lower() == "n":
            print(f'게임을 종료합니다')
            break
        elif retry.lower() == "y":
            print("**** 새로운 게임 ****")
            break
        else:
            print("y와 n 중 하나를 입력해주세요.")
            continue
    
    if retry.lower() == "n":
        break