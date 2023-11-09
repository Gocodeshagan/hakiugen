def create_dictionary(file):
    data_dict = {}
    
    with open('syllable_data.txt','r') as file:
      
        for lines in file:
            file.readline()
            values = lines.strip().split(', ')
       
            data_dict.update({values[0]:values[1]})
        print(data_dict)
    pass

word_to_syllable = create_dictionary('syllable_data.txt')
print(word_to_syllable)
