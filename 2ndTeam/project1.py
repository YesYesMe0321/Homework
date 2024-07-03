class Member:
    members = {
        'yoshi': {'name': 'Ben', 'password': 123},
        'Tachanka': {'name': 'Lord', 'password': 13214}
    }

    @classmethod
    def display(cls):
        for username, user_info in cls.members.items():
            print(f"회원이름: {user_info['name']}, 아이디: {username}")

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

while True:
    # 유저 목록 출력
    print("\n[유저 목록]")
    Member.display()

    # 작성된 글 목록
    Post.display_posts()

    # 사용자 입력 받기
    title = input("\n제목: ")
    content = input("내용: ")
    author = input("ID: ")
    password = input("PS: ")

    # 작성 시도
    Post.posting(title, content, author, int(password))
