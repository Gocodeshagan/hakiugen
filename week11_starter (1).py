'''
Haiku Generator

Author:Shagan Brar
Date:

[describe your project here]
'''#aim is to take file as input and create haiku from it

# IMPORTS ----------------------------------------------------------------------

from string import punctuation

# HELPER FUNCTIONS  ------------------------------------------------------------
'''
Here are some functions you might want to create to keep your code clean.
Completely optional.
'''


def get_menu_input(): # optional helper function to ensure user is giving valid menu input
    pass


def get_haiku_input(): # optional helper function to ensure user is giving valid haiku input
    pass


'''
If you find any of the necessary functions very complicated or repetitive,
create your own helper functions here too. Highly recommended!
'''

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

# NECESSARY FUNCTIONS ----------------------------------------------------------


def create_dictionary(file):
    '''
    This function must take in an OPENED file object.
    It will read through the data file and create a dictionary object that maps
    words (as strings) to their syllable counts (as integers).
    Your function will RETURN this new dictionary.

    Be sure to CLEAN the data 
    - eliminate spaces and newline characters
    - use the clean_punctation to get rid of punctuation from words
    '''
    pass

def create_random_line(words, syllables = 5):
    '''
    This is a helper function for create_random_haiku.
    It takes in a list of words to use and a number of syllables,
    and uses the words_to_syllables dictionary to return a STRING
    of words with that exact amount of syllables.

    HINT: use a while loop to keep track of how many syllables you
    need to fill, and another INNER while loop to make sure you 
    never accidentally use a word with too many syllables. Test
    out this function lots!
    '''


def create_random_haiku():
    '''
    This is the function that will be called when the user wants to create a 
    randomized haiku based on their input file.

    YOU CHOOSE THE PARAMETERS AND RETURN VALUE.

    use the create_random_line function.
    You may create other helper functions too if you need.
    '''
    pass


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


# MAIN CODE --------------------------------------------------------------------


'''
Write the preparation needed before you are able to call create_dictionary.
'''

# word_to_syllable will be the global dictionary storing all the 
# words from the dictionary file and their syllables
# you will be using this global dictionary in SEVERAL PLACES
# but you should not be CHANGING it.
word_to_syllable = create_dictionary()
run = True

while run:
    print_menu()
    user_choice = input('(1/2/3): ')
    '''
    Add some input sanitization and error-catching here!
    If the user enters something other than 1,2, or 3, let them know
    that is not valid input!
    '''

    '''
    You are free to change the code below!
    Use your functions wisely.
    The function calls CAN AND SHOULD BE CHANGED since you will be
    deciding on the parameters and return values for these functions.
    '''

    if user_choice == '1':
        create_random_haiku()
    elif user_choice == '2':
        check_haiku()
    elif user_choice == '3':
        '''
        Add code here so the program will stop when the user types 3.
        '''
        pass
        