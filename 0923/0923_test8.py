import random, time

game_list = ["moon", "potato", "sky", "garlic", "book", "sun", "car", "grape", "apple"]

num_questions = 10

input("[타자 게임] 준비되면 엔터!")

start_time = time.time()
for q in range(1, num_questions + 1):
    target = random.choice(game_list)

    while True:
        print(f"문제 {q}")
        print(f"{target}")
        user = input("").strip()  
        if user == target:
            print("통과!!")
            break
        else:
            print("오타! 다시 도전!!")

end = time.time()  
elapsed = end - start_time

print(f"타자 시간: {elapsed:.2f}초")