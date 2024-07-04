from tabulate import tabulate
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class Member:
    members = {
        'yoshi': {'name': 'Ben', 'password': 123},
        'Tachanka': {'name': 'Lord', 'password': 13214}
    }

    @classmethod
    def display(cls):
        table = []
        for username, user_info in cls.members.items():
            table.append([user_info['name'], username])
        print(tabulate(table, headers=['Name', 'ID'], tablefmt='fancy_grid'))

class Post:
    posts = []

    @classmethod
    def posting(cls, title, content, username, password):
        user_info = Member.members.get(username)
        if user_info is not None and user_info['password'] == password:
            cls.posts.append({
                'title': title,
                'author': username,
                'content': content
            })
            print("작성 성공")
            logging.debug("Login Successful")
            logging.getLogger().handlers[0].flush()
        else:
            print("로그인 실패로 작성 불가")

    @classmethod
    def display_posts(cls):
        if not cls.posts:
            print("\n[글 목록]\n포스트가 없습니다.")
        else:
            print("\n[글 목록]")
            for index, post in enumerate(cls.posts, start=1):
                print(f"[{index}]. 제목: {post['title']}\n     작성자: {post['author']}\n     내용: {post['content']}\n---------------------")

# 실제 프롬프트에서 처음 보게 될 작업, 하고자하는 작업을 선택함
while True:
    print("\n[작업 목록]\n1. 계정 추가\n2. 유저 목록\n3. 글 목록\n4. 글 작성\n그외. 종료") # 작업 5를 추가해 글 삭제 기능을 구현

    select = input("원하는 작업을 선택하세요: ")
    if select == '1': # 계정 생성
        print("\n[계정 생성]")
        name = input("이름: ")
        id = input("id: ")
        password = input("ps: ")
        Member.members[id] = {'name': name, 'password': int(password)}
    elif select == '2':  # 유저 목록 확인
        print("\n[유저 목록]")
        Member.display()
    elif select == '3': # 글 목록 확인 (과제내용 6번이 for반복문을 통해 표시될 글을 필터링할 것을 요구함) (이에 대한 보강 필요)
        # 작성된 글 목록
        Post.display_posts()
    elif select == '4': # 글 작성 작업
        # 사용자 입력 받기
        title = input("\n제목: ")
        content = input("내용: ")
        author = input("ID: ")
        password = input("PS: ")
        # 작성 시도
        Post.posting(title, content, author, int(password))
    else: # 위에 없는 내용이 입력될 시 종료
        print("종료합니다.")
        break
