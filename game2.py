import random

select = ["가위", "바위", "보"]

win = 0
lose = 0
draw = 0

while True:
    com = random.choice(select)
    while True:
        user = input("가위, 바위, 보 중 하나를 선택하세요: ")
        if user not in select: # [가위, 바위, 보] 의 입력만 받으며, 그외의 경우 경고
            print("유효한 입력이 아닙니다")
            continue
        elif com == user: # 컴퓨터와 유저가 같은 선택 시
            print(f'**************************\n사용자: {user}, 컴퓨터: {com}\n무승부\n**************************')
            draw += 1
            break
        elif (user == "가위" and com == "보") or (user == "바위" and com == "가위") or (user == "보" and com == "바위"): # 유저가 이기는 경우
            print(f'**************************\n사용자: {user}, 컴퓨터: {com}\n사용자 승리!\n**************************')
            win += 1
            break
        else: # 그외 = 컴퓨터가 이기는 경우
            print(f'**************************\n사용자: {user}, 컴퓨터: {com}\n컴퓨터 승리!\n**************************')
            lose += 1
            break
    
    while True:
        retry = input("다시 하시겠습니까? Y/N (이외 문자는 Y로 인식합니다)\n")
        if retry.lower() == "n":
            print(f'게임을 종료합니다\n승: {win} 패: {lose} 무승부: {draw}')
            break
        elif retry.lower() == "y":
            print("**** 새로운 게임 ****")
            break
        else:
            print("y와 n 중 하나를 입력해주세요.")
            continue
    
    if retry.lower() == "n":
        break