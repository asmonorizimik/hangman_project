import random
def display_hangman(tries):
    stages = [  """
            +------+      
            |      |      
            0      |      
           /|\     |     
           / \     |      
                   |
                   |    
            ======== 
                   """,
                   """
            +------+ 
            |      |      
            0      |      
           /|\     |     
             \     |      
                   |
                   |     
            ========       
                   """,
                   """
            +------+       
            |      |      
            0      |      
           /|\     |   
                   |      
                   |
                   |
            ========       
                   """,
                   """
            +------+ 
            |      |
            0      |      
            |\     |      
                   |     
                   |      
                   |
            ========
                   """,
                   """
            +------+
            |      |
            0      |      
            |      |      
                   |      
                   |
                   |
            ========
                   """,
                   """
            +------+  
            |      |
            0      |
                   |
                   |
                   |
                   |
            ========
                   """,
                   """
            +------+
            |      |  
                   |      
                   |
                   |
                   |
                   |
            ========
                   """,
                   """
            +------+
                   |        
                   |
                   |
                   |
                   |
            ========"""
    ]
    return stages[tries]


def load_word():
    with open("words.txt","r") as file:
        line= file.read()
        word_list=line.split("\n")
    return word_list

def get_word():
    word_list=load_word()
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7
    i=1
    print("I'm thinking about",len(word),"letters long word...\n \n      GOOD LUCK!!!!.")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already tried", guess, "!")
            elif guess not in word:
                print(guess, "isn't in the word :(\tyou have",tries-i,"tries left")
                tries -= 1
                print("you have",tries,"tries left...")
                guessed_letters.append(guess)
            else:
                print("Nice one,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]##list comprehension
                print(indices,"indices for the guessed letters")
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already tried ", guess, "!")
            elif guess != word:
                print(guess, " not in the word :(")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
            i+=1
        else:
            print("invalid input")
        print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print("congrats!!!, you guessed the word!")
    else:
        print("I'm sorry, you ran out of tries. The word was " + word + ". Maybe next time!")



def main():
    user=input("enter your name:")
    print("WELCOME!!!",user)
    print("Let's play Hangman Game !!..Guess your letters of a word and Pliz don't hang me!!")
    word = get_word()
    play(word)
    while True:
        if input("Again? (Y/N) ").upper() == "Y":
            word = get_word()
            play(word)
        else:
            print("Thank You!!!!")
            break
main()