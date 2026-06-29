from art import logo
from game_data import data
import random



def format_data(account):
    """Function takes the account data and returns the printable format:"""
    account_name = account["name"] #getting information from the dictionaries
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(user_guess, a_follower_count, b_follower_count):
    """Function takes the user's guess and the amount of followers to check if they were right"""
    if a_follower_count > b_follower_count:
        return user_guess == "a"
    else:
        return user_guess == "b"



print(logo)
score = 0
game_continue = True

# generating a random account from the game data:
account_a = random.choice(data)
account_b = random.choice(data)

while game_continue:
    #making A become B as user progresses in game, B becomes a new random account
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(f"Against B: {format_data(account_b)}.")


    # asking the user for their guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # clearing the screen to make it look better
    print("\n" * 20)
    print(logo)

    # checking is the user is correct:
    # getting the follower amount from each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

    # keeping score:
    if is_correct:
        score += 1
        print("You are right!")
    else:
        print(f"You are wrong. Your final score is: {score}")
        game_continue = False











