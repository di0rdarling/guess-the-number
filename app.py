import random
import sympy


def guess_number():
    # Get a random number.
    random_number = random.randint(1, 50)
    user_input = input(
        "A random number between 1 and 50 has been selected. Guess the number...")
    attempts = 1

    # The user only has a maximum of three attempts.
    while (random_number != int(user_input)) and attempts <= 3:
        if attempts == 1:
            print("Sorry, that was incorrect. Here's a hint...")
            first_hint(random_number)
            user_input = input("Can you guess what the number is now?")
            attempts += 1
        elif attempts == 2:
            print("Damn, that wasn't the answer either. Here's another hint...")
            second_hint(random_number)
            user_input = input("Can you guess what the number is now?")
            attempts += 1
        elif attempts == 3:
            print("Wow, that still wasn't it. Try one more time. Here's another hint...")
            third_hint(random_number)
            user_input = input("Can you guess what the number is now?")
            attempts += 1

    if random_number == int(user_input):
        print("Well done, that's correct! The number is " +
              str(random_number) + "!")
    else:
        print("Sorry that was not correct. The number is " +
              str(random_number) + ". Better luck next time!")
        print("You said the answer was " + str(user_input) + ".")


# Returns the first hint
def first_hint(number):
    hint_range = get_number_range(number)
    print("It's a number between " +
          str(hint_range[0]) + " and " + str(hint_range[1]))

# Returns the second hint


def second_hint(number):
    if is_even(number):
        print("It's an even number.")
    else:
        print("It's an odd number.")


# Returns the third hint
def third_hint(number):
    is_prime = sympy.isprime(number)
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Determines if a number if odd or even.
def is_even(number):
    if (number % 2) == 0:
        return True
    else:
        return False


# Returns a random range given a number.
def get_number_range(number):
    randon_range = random.randint(5, 10)

    if number < randon_range:
        return [1, randon_range]
    else:
        return [number - randon_range, number + randon_range]


guess_number()
