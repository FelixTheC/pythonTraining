#! /usr/env/python3
from random import randint

def language(lang):
    """
    This function needs a string as paramter and return a dictionary, 
    avalaibles are only english and german specially created for this game
    """
    eng = {'minimum':'Please set your minimum: ',
           'maximum':'Please set your maximum: ',
           'start': 'Please guess the number between %s and %s',
           'try':'Your %d. try: ', 'fail':'The game is called guess the NUMBER!!!!',
           'out':'Your number is out of the defined range',
           'again':'You had tryed this number bevor',
           'greater':'The number we are looking for is smaller', 'low':'The number we are looking for is greater',
           'win':'Congratulations the number you typed in ( %s ) was the number we are looking for'}
    deu = {'minimum':'Bitte wähle deine Untergrenze: ',
           'maximum':'Bitte wähle deine Obergrenze: ',
           'start': 'Bitte errate die Zahl zwischen %s und %s',
           'try':'Ihr %d. Versuch: ', 'fail':'Das Spiel heißt rate die NUMMER!!!!',
           'out':'Die eingegebene Zahl befindet sich ausserhalb des von ihnen definierten Bereich',
           'again':'Mit dieser Zahl haben Sie es bereits versucht',
           'greater':'Die gesuchte Zahl ist kleiner', 'low':'Die gesuchte Zahl ist größer',
           'win':'Glückwunsch die von Ihnen eingegeben Zahl ( %s ) stimmt mit der gesuchten Zahl überein'}
    if lang == 'english':
        return eng
    elif lang == 'deutsch':
        return deu


def chooseLang():
    """
    ask the user for a language and check the input if success it will return a language dictionary 
    """
    langDic = None
    languages = ['english', 'deutsch']
    lang = input('Please choose your language/Bitte wähle deine Sprache, english/deutsch: ')
    if lang in languages:
        langDic = language(lang)
        return langDic
    else:
        return chooseLang()


def checkNumbers(number, guess):
    """
    needs the number we are looking for and the guessing number as parameters
    checks the number with the guess, if the guess is not an int it will return a failure
    """
    try:
        if int(guess) > number:
            return 'greater'
        elif int(guess) < number:
            return 'low'
        elif int(guess) == number:
            return 'win'
    except:
        return 'fail'


def main():
    """
    the main function
    """
    langDic = chooseLang()
    guesses = 1
    guestNums = []
    
    #setting up the minimum and the maximum
    minimum = input(langDic['minimum'])
    maximum = input(langDic['maximum'])
    
    #creating the number which the user must guess
    theNumber = randint(int(minimum), int(maximum))
    
    print(langDic['start']%(minimum, maximum))
    
    while True:
        guess = input(langDic['try']%(guesses))
        guesses += 1
        check = checkNumbers(theNumber,guess)
        if guess in guestNums:
            print(langDic['again'])
        elif int(guess) < int(minimum) or int(guess) > int(maximum):
            print(langDic['out'])      
        else:
            guestNums.append(guess)
            if check == 'win':
                print(langDic[check]%(guess))
                break
            else:
                print(langDic[check])
                
            
            
if __name__ == '__main__':
    main()