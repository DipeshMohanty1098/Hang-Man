import random


def create_list(guess_list):
    new_list = []
    for i in range(len(guess_list)):
        new_list.append('_ ')
    return new_list


def print_word(new_list):
    a = ''
    c = a.join(new_list)
    return c


def word_check(c, guess, new_list):
    if c == guess:
        print("Guessed right!")
        result = print_word(new_list)
        print(result + " is the correct word")
        run = False
        return run
    else:
        pass


def letter_check(guess_list, new_list, turn):
    flag = int
    for j in range(len(guess_list)):
        if guess_list[j] == turn:
            flag = 1
            new_list[j] = turn
            print_word(new_list)
    if flag == 1:
        correct = 1
        return correct
    else:
        return 0


def clear():
    guess = ''
    guess_list = []



def main():
    result1 = str
    ready = str(input("Ready to Play, Y or N? ").upper())
    if ready == 'Y':
        words = ['synonymous', 'interest', 'second', 'handy', 'descriptive', 'visitor', 'shoe', 'sort', 'rebel','decisive' , 'verdant', 'weather']
        print("Random word will be picked now!")
        guess = random.choice(words)
        print("Number of letters in the word is '{}'".format(len(guess)))
        guess_list = list(guess)
        res1 = create_list(guess_list)
        result = print_word(res1)
        print(result)
        moves = 6
        while moves > 0:
            turn = str(input("guess a letter: "))
            res4 = letter_check(guess_list, res1, turn)

            if res4 == 0:
                moves -= 1
                print("Letter isn't present, {} turns remaining".format(moves))
                result1 = print_word(res1)
                print(result1)
                if moves == 0:
                    print("Game Over!, The correct word was '{}'".format(guess))
                    ask = str(input("Play again? Y or N: ")).lower()
                    if ask == 'y':
                        clear()
                        main()
                    else:
                        break

            else:
                print("letter present! ")
                result1 = print_word(res1)
                print(result1)
                res3 = word_check(result1, guess, res1)
                if res3 is False:
                    break
                else:
                    pass
                full = str(input("Know the full word? take a guess Y or N: ").upper())
                if full == 'Y':
                    fw = str(input("enter word: "))
                    if fw == guess:
                        print("Correct! great job!")
                        ask = str(input("Play again? Y or N")).lower()
                        if ask == 'y':
                            clear(guess, guess_list)
                            main()
                        else:
                            break
                    else:
                        moves -= 1
                        print("Wrong! Try Again, {} turns remaining".format(moves))
                        continue
                else:
                    pass
                result1 = print_word(res1)
                print(result1)
            res3 = word_check(result1, guess, res1)
            if res3 is False:
                break
            else:
                continue



main()















