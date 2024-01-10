from random import randint

def get_input():

    while True:
        user_input = input("Guess: ")
        try:
            return int(user_input)
        except:
            print("That's not a number!")


def generate_random_number():
    
    return randint(1, 20)

random_number = generate_random_number()
user_value = -1

for i in range(5):
    user_value = get_input()
    if user_value == random_number:
        break
    else:
        if user_value < random_number:
            print("Go Higher!!!")
        else:
            print("Go Lower!!!")

if user_value == random_number:
    print("Correct!")
