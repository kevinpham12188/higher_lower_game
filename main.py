from game_data import data
import random
from art import logo, vs

list_length = len(data)


def get_data():
    return random.choice(data)


def play_game():
    print(logo)
    is_game_over = True
    current_score = 0
    while is_game_over:
        character1 = get_data()
        character2 = get_data()
        print(f"Compare A: {character1['name']}, a {character1['description']}, from {character1['country']}")
        print(vs)
        print(f"Against B: {character2['name']}, a {character2['description']}, from {character2['country']}")
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_guess == 'a' and character1['follower_count'] > character2['follower_count']:
            current_score += 1
            print(f"You are right! Current score: {current_score}")
        elif user_guess == 'a' and character1['follower_count'] < character2['follower_count']:
            is_game_over = False
            print(f"Sorry! That's wrong. Your final score is {current_score}")
        elif user_guess == 'b' and character1['follower_count'] < character2['follower_count']:
            current_score += 1
            print(f"You are right! Current score: {current_score}")
        elif user_guess == 'b' and character1['follower_count'] > character2['follower_count']:
            is_game_over = False
            print(f"Sorry! That's wrong. Your final score is {current_score}")


play_game()
