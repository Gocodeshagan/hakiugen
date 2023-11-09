from string import punctuation

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
            file.readline()
            values = lines.strip().split(', ')
       
            data_dict.update({values[0]:values[1]})
        print(data_dict)
    pass


def create_random_line(words, syllables = 5):
    






    pass
   
    


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

#main code

word_to_syllable = create_dictionary('syllable_data.txt')


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
