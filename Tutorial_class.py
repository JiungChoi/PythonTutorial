class User:
    def say_hello(self):
        print("안녕하세요! 저는 {}입니다.".format(self.name))

    def login(self, my_email, my_password):
        if(self.email == my_email and self.password == my_password):
            print("로그인 성공, 환영합니다")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

    def check_name(self, name):
        return self.name in name

user1 = User()
user2 = User()
user3 = User()

user1.name = '최지웅'
user1.email = 'king_jiung@gmail.com'
user1.password = 'wldnd6'

user2.name = '권익현'
user2.email = 'king_ikhyung@gmail.com'
user2.password = 'dlrgus'

user3.name = '박경민'
user3.email = 'king_kyungmingmail.com'
user3.password = 'rudals'

User.say_hello(user1)
user1.say_hello()

user1.login(user1.email, user1.password)

print(user1.check_name("최지웅") )