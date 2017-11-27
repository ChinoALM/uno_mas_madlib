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

def game_instructions(madlib_level, blanks, answers):
    """
    As the game proceeds, this function finds blanks, prompts user input, converting the madlib_level
    string into a list. Correct answers are put into a new list along with the non-blank words, joining
    them to reform a string to print out; if user is incorrect after 3 attempts, func prints out answers
    within the madlib_level to continue game.
    """
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

def game_intro():
    """
    Prompts user to select a level difficulty, then calls on the game_instructions function
    to set up the appropriate madlib and answers associated with that level.
    asks user to try again if a subject from the list is not selected
    """