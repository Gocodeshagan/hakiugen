from string import punctuation
import random

#functions  
def get_menu_input(): # optional helper function to ensure user is giving valid menu input
    pass


def get_haiku_input(): # optional helper function to ensure user is giving valid haiku input
    pass

def print_menu(): # function to print menu - leave in!
    print('------------------------------------')
    print('-       HAIKU MAKING PROGRAM       -')
    print('- OPTIONS                          -')
    print('- 1 : Get randomly generated poems -')
    print('- 2: Have your haiku checked       -')
    print('- 3: Quit the program              -')
    print('------------------------------------')

def clean_punctuation(word): # function that cleans out punctuations from a string - leave in!
    clean_word = ""
    for letter in word:
        if letter not in punctuation:
            clean_word += letter
    return clean_word

def create_dictionary(file):
    data_dict = {}
    
    with open('syllable_data.txt','r') as file:
      
        for lines in file:
            values = lines.strip().split(', ')
       
            data_dict.update({values[0]:values[1]})
        print(data_dict)
    return data_dict
    pass


def create_random_line(word_to_syllable, words, syllables=5):
    line_syllable_count = 0
    line_words = []

    for _ in range(100):  # Limit to 100 iterations to avoid infinite loop
        random_word = random.choice(words)
        word_syllables = int(word_to_syllable.get(random_word, 1))

        # Check if adding the current word exceeds the desired syllable count
        if line_syllable_count + word_syllables <= syllables:
            line_words.append(random_word)
            line_syllable_count += word_syllables

            # Stop if we reach the desired syllable count
            if line_syllable_count == syllables:
                break

    if line_syllable_count != syllables:
        # If unable to create a line with the desired syllables, try again
        return create_random_line(word_to_syllable, words, syllables)

    print("Selected words:", line_words)
    return ' '.join(line_words)

def create_random_haiku(word_to_syllable):
    u_file = input("Enter a file name: ")

    with open(u_file, 'r') as file:
        u_words = [clean_punctuation(word.strip()) for word in file]

    # Ensure each line has the correct syllable count
    line1 = create_random_line(word_to_syllable, u_words, 5)
    line2 = create_random_line(word_to_syllable, u_words, 7)
    line3 = create_random_line(word_to_syllable, u_words, 5)

    if line1 and line2 and line3:
        haiku = f"{line1}\n{line2}\n{line3}"
        print("\nYour random haiku: ")
        print(haiku)
    else:
        print("Unable to generate a haiku with the given file.")

def check_syllable_count(line, count=5):
    '''
    This function takes in a line of a poem and the number of syllables this
    line should have. count has a DEFAULT value of 5.

    YOU CHOOSE THE RETURN VALUE.
    '''
    pass


def check_haiku():
    '''
    This is the function that will be called when the user requests their haiku
    checked. Your function must tell them which line has the wrong
    syllable count.

    YOU CHOOSE THE PARAMETERS AND RETURN VALUE.

    Use the check_syllable_count function.
    '''
    pass

#main code

word_to_syllable = create_dictionary('syllable_data.txt')


run = True

while run:
    print_menu()
    user_choice = input('(1/2/3): ')
 

    if user_choice == '1':
        
    
            

        haiku = create_random_haiku(word_to_syllable)
        print(haiku)

    elif user_choice == '2':
        check_haiku()
        
    elif user_choice == '3':
        print('End')

    else:
        print('Invalid Option, Enter 1 2 or 3')
        '''
        Add code here so the program will stop when the user types 3.
        '''
        pass
