def vowel_checker(input_string):
    """Checks if the input word bgins with a vowel.

    Parameters
    ----------
    input_string: string
        String that gets checked if the first letter of the word is a vowel  

    Returns
    -------
    output: boolean
        True if string starts with vowel, otherwise False
    """

    vowels = ['a', 'e', 'i', 'o', 'u']

    if input_string[0] in vowels:
        output = True

    else:
        output = False

    return output


def add_vowel_suffix(input_string):
    """Adds the "-way" suffix to it the given string.

    Parameters
    ----------
    input_string: string
        String beginning with vowel that gets suffix added to it

    Returns
    -------
    output: string
        String with added suffix
    """

    output = input_string + '-' + 'way'
    return output

def remove_vowel_suffix(input_string):
    """Removes the vowel suffix from input string.

    Parameters
    ----------
    input_string: string
        String that contains the "-way" suffix

    Returns
    -------
    output: string
       String without any suffix
    """

    output = input_string[0:-4]
    return output



def add_suffix(input_string):
    """Adds suffix to input.

    Parameters
    ----------
    input_string: string
        String gets "-ay" suffix added to the word

    Returns
    -------
    output: string
       String with suffix added to the end of each word
    """
    
    output = input_string + '-' + input_string[0] + 'ay'
    return output


def remove_first_letter(input_string):
    """Removes first letter from input 

    Parameters
    ----------
    input_string: string
        String to get first letter of the word removed from it

    Returns
    -------
    output: string
       String without the first letter of thre original word
    """

    output = input_string[1:]
    return output 


def add_first_letter(input_string):
    """Add first letter of original word back to the string

    Parameters
    ----------
    input_string: string
        String with first letter of the original word missing

    Returns
    -------
    output: string
        String witht the first letter of the original word added back to it
    """

    output = input_string[-3] + input_string
    return output


def remove_suffix(input_string):
    """Removes suffix from input 

    Parameters
    ----------
    input_string: string
        String with suffix at the end

    Returns
    -------
    output: string
       String with no suffix at the end 
    """

    output = input_string[0:-4] 
    return output


def pig_latin_encoder(input_string):
    """Takes input in english and translates it into pig latin

    Parameters
    ----------
    input_string: string
        String with one or more words

    Returns
    -------
    output: string
       String twith each word translated into pig latin
    """
    # seperates the string and stores each word into a list
    seperated = input_string.split(' ')
    translated = ''

    for i in seperated:

        # if the word doesn't begin with a vowel then the suffix gets added
        # then the first letter gets removed and that string is then added to
        # an initialized string
        if vowel_checker(i) == False:
            with_suffix =  add_suffix(i)
            new_word = remove_first_letter(with_suffix)
            translated = translated + new_word + ' '
            
        else:
            new_word = add_vowel_suffix(i) 
            translated = translated + new_word + ' '

    return translated[0:-1]


def pig_latin_decoder(input_string):
    """Takes input and translates it from pig latin to english

    Parameters
    ----------
    input_string: string
        String in pig latin 

    Returns
    -------
    output: string
       String in english
    """

    seperated = input_string.split(' ')
    translated = ''

    for i in seperated:
        
        # adds the first letter of the string back to the front it then
        # removes the suffix from the end of the word and stores it
        # an initialized string
        if input_string[-4:] != '-way':
            with_prefix = add_first_letter(i)
            original_word = remove_suffix(with_prefix)
            translated = translated + original_word + ' '
    
        elif input_string[-4:] == '-way':
            original_word = input_string[0:-4]
            translated = translated + original_word + ' '

    return translated[0:-1]

    
