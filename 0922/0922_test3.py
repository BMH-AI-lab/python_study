class User:
    total_users = 0
    
    def __init__(self, username, points):
        self.username = username
        self.points = 0
        User.total_users += 1
    
    def add_points(self, amount):
        if amount > 0:
            self.points += amount

    def get_level(self):
        if self.points < 100:
            return "Bronze"
        elif self.points < 500:
            return "Silver"
        elif self.points > 500:
            return "Gold"
    
    @classmethod
    def get_total_users(cls):
        return (f"총 유저 수: {cls.total_users}")
    
user_name1 = User("김철수", 200)
user_name2 = User("이영희", 50)
user_name3 = User("홍길동", 600)
user_name1.add_points(400)
user_name2.add_points(10)
user_name3.add_points(700)
User.get_total_users()
print(user_name1.username, ":", user_name1.get_level())
print(user_name2.username, ":", user_name2.get_level())
print(user_name3.username, ":",  user_name3.get_level())
print(User.get_total_users())

