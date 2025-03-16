import art
from game_data import data
from random import choice


def choose_celebrity():
    """Picks a celebrity from data list"""
    celebrity_object = choice(data)
    return celebrity_object


def celebrity_description(celebrity):
    """Returns description of a celebrity (name, profession, country)"""
    name = celebrity["name"]
    profession = celebrity["description"]
    country = celebrity["country"]
    return f"{name}, the {profession}, from {country}"


def ask_for_guess():
    """Ask for input"""
    guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
    return guess


def get_user_input():
    """Get user input and check the correctness"""
    input_guess = ask_for_guess()
    while input_guess != "A" and input_guess != "B":
        print("Please make sure your guess is either 'A' or 'B'")
        input_guess = ask_for_guess()

    return input_guess


def compare_followers(num1, num2):
    """Compares two numbers and returns 'A' if the first number if greater and 'B' otherwise"""
    if num1 > num2:
        return 'A'
    elif num2 > num1:
        return 'B'
    else:
        return 'D'


def play_game():
    guess_correct = True
    current_score = 0

    # randomize celebrity A
    celebrity_a = choose_celebrity()

    # loop while the guess is correct
    while guess_correct:
        # randomize celebrity B
        celebrity_b = choose_celebrity()

        # if celebrity B is the same as celebrity A, choose a different celebrity B
        while celebrity_b is celebrity_a:
            celebrity_b = choose_celebrity()

        # get follower count for both celebrities
        celebrity_a_followers = celebrity_a["follower_count"]
        celebrity_b_followers = celebrity_b["follower_count"]

        # compare follower counts
        correct_answer = compare_followers(celebrity_a_followers, celebrity_b_followers)

        # display options to user
        print(f"Compare A: {celebrity_description(celebrity_a)}")
        print(art.vs)
        print(f"Against B: {celebrity_description(celebrity_b)}")

        # get user input
        user_guess = get_user_input()

        print("\n" * 20)
        print(art.logo)

        # if guess was correct, increment score
        if user_guess == correct_answer:
            current_score += 1
            print(f"You're right! Current score: {current_score}")

            # move celebrity B to the position A
            celebrity_a = celebrity_b

        # otherwise display final score and break out of the loop
        else:
            print(f"Sorry, that's wrong! Final score: {current_score}")
            guess_correct = False


print(art.logo)
print("** Play a game and guess the number of followers of each celebrity/organization on Instagram. **")
print()

play_game()
