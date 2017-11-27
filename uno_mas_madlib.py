blanks = ["__1__", "__2__", "__3__", "__4__", "__5__"]

#madlib_levels and answers
easy_madlib = """Hey __1__ , dont make it __2__ .  Take a sad __3__ and make it better.
Remember to let __4__ into you heart. Then you can __5__ to make it better."""

easy_answers = ['Jude', 'bad', 'song', 'her', 'start']

medium_madlib = """Let __1__ take you down cause Im going to __2__ fields.
Nothing is __3__ , and __4__ to get hung about. Strawberry __5__ forever."""

medium_answers =  ['me', 'strawberry', 'real', 'nothing', 'fields']

hard_madlib = """There is nothing __1__ can do that cant be done. Nothing you can __2__ that
cant be __3__ . Nothing you can say but you can __4__ how to play the game. Its __5__ . All you
need is love."""

hard_answers = ['you', 'sing', 'sung', 'learn', 'easy']

def fill_in_blanks(word, blanks):
    """
    Searches madlib for blanks by comparing word to blanks list using (word, blanks) as inputs and
    outputs a blank or None. Func given to us from the madlib class materials.
    """
    for blank in blanks:
        if blank in word:
            return blank
    return None

def check_answers(answer):
    """
    Prompts user input and compares user input to answers list to check if guess is correct.
    User is informed: correct or incorrect; and receives three strikes (attempts) per blank.
    """
    check = False
    while check == False:
        strike_count = 3
        for strike in range(strike_count):
            user_input = raw_input("What is the correct answer? ")
            if user_input == answer:
                print "You are correct!"
                return answer
            else:
                print "Incorrect. Please guess again."
            if strike == strike_count - 1:
                print "The correct answer is " + answer + "."
                return answer

def game_instructions(madlib_level, blanks, answers): #prompts user input, passes thru madlib_level string.
    print madlib_level
    replaced = []
    madlib_level = madlib_level.split()
    counter = 0
    for word in madlib_level:
        replacement = fill_in_blanks(word, blanks)
        if replacement != None:
            print "Please fill in the answer for blank #" + str(counter + 1) + "."
            response = check_answers(answers[counter])
            new_word = word.replace(replacement, response)
            replaced.append(new_word)
            phrase = " ".join(replaced)
            remainder = " ".join(madlib_level)
            print phrase + remainder[remainder.find("_"+str(counter + 1)+"_") + len(word):]
            counter += 1
        else:
            replaced.append(word)
            phrase = " ".join(replaced)

def game_intro(): #Asks the user to input a difficulty level and loads that levels data.
    print '\n'+ "Fill in the blanks with lyrics from me Mad Hatter's favorite Beatles' songs! Good luck!" + '\n'
    select_level_difficulty = False
    while select_level_difficulty == False:
        user_input = raw_input("Please select a level -- easy, medium or hard: ").lower()
        if user_input == "easy":
            print "You selected easy."
            select_level_difficulty = True
            game_instructions(easy_madlib, blanks, easy_answers)
        elif user_input == "medium":
            print "You selected medium."
            select_level_difficulty = True
            game_instructions(medium_madlib, blanks, medium_answers)
        elif user_input == "hard":
            print "You selected hard."
            select_level_difficulty = True
            game_instructions(hard_madlib, blanks, hard_answers)
        else:
            print "You selected an invalid level. Please select easy, medium, or hard."

game_intro() #func runs madlib
raw_input("Thanks for playing! Hit return to exit:")