import sys

def input_str(prompt, choices):
    """
        input_str
        This method will input a string. In addition it is supplied a set of valid choices
    """
    input_ok = False
    while not input_ok:
        response = input(prompt)
        input_ok = response in choices
    return response
    
def input_int(prompt):
    """
        input_int
        This method inputs a integer
    """
    input_ok = False
    while not input_ok:
        response = input(prompt)
        input_ok = response.isnumeric()
    return int(response)

def main(argv):
    """
        main
        This is the main guessing progran
    """
    max_number = input_int("Please enter a number n: ")
    low_number = 0
    game_done = False
    total_guesses = 0
    total_games = 0

    while not game_done:        
        found = False
        high_number = max_number
        low_number = 0
        total_games = total_games + 1
        guesses = 0
        while not found:
            guess = int(((high_number-low_number)/2)+low_number)
            hint = input_str("{}? [h, l, c]: ".format(guess), ['h', 'H', 'l', 'L', 'c', 'C'])
            guesses = guesses + 1
            if hint in ['h', 'H']:
                low_number = guess +1
            elif hint in ['l', 'L']:
                high_number = guess - 1
            elif hint in ['c', 'C']:
                total_guesses = total_guesses + guesses
                found = True
            if high_number==low_number:
                print("Your number is {}".format(high_number))
                found = True
        print("It took me {} guesses".format(guesses))
        total_guesses = total_guesses + guesses
        print("I averaged {} guesses per game for {} game(s)".format(total_guesses / total_games, total_games))
        play_again = input_str("Want to play again [y/n]: ", ['y', 'Y', 'n', 'N'])
        game_done = play_again in ['n', 'N']
if __name__ == "__main__":
    main(sys.argv[1:])
