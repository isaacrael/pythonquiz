__author__ = '184766'
""" The following program quizzes the computer user on the python programming language.
"""

import random
from colorama import init
from colorama import Fore, Back

init()



question_answer = {
"What characters are used to create an empty python list?": "[]",
"What characters are used to create an empty python dictionary?": "{}",
"What is the name of a well known Python web framework?": "django",
"What does a python dictionary store?": "key value pairs",
"What is the name of a popular website where python docs can be obtained?": "python.org",
"What do modules do?": "they extend the functionality of python",
"What is the name of the python interpreter?": "idle",
"Write the code to display the keys from the following dictionary called phonebook {\"Gil\": \"8330785\", \"Bill\": \"9786543\"}": "phonebook.keys()",
"Create a list from the following data Gil Mark Carlos": "[\"Gil\", \"Mark\", \"Carlos\"]",
"Create a dictionary from the following data Gil, 8330785 Steve, 2037659": "{\"Gil\": \"8330785\", \"Steve\": \"2037659\"}",
"Who created python?": "Guido van Rossum",
"What year was python conceived?": "1989",
"Name 2 types of loops used in python": "for and while loops",
"Define the following function GetAnswer": "def GetAnswer():",
"Call the following function def GetAnswer(value):": "GetAnswer(value)",
"What is the import statement used for?": "import modules so they can be used in current program",
"Import the following module called brompton": "import brompton",
"Name 3 statements that conditionally execute a block of code": "if else elif",
"What does the class statement do?": "attaches it's local namespace to a class and executes a block of code",
"Name 3 statements that work together to raise, catch, and clean up code from exceptions": "try except finally",
"Name 2 programs that can be used to install python programs": "easy_install and pip",

}

questions = list(question_answer.keys())
question = random.choice(questions)

#print(Fore.RED + 'some red text')

name = raw_input("Please enter your name")
print"\n******************************************** Welcome to Python Quiz",(name) + " ***************************"
print("\n")


motivationalText = ["Awesome Keep It Up!", "Great Job!!!", "Yeah Buddy :>)", "Just Do It!", "Your Kickin Ass Dude!",
                    "Don't Get Mad Get Even!", "Teach These Monkey's A Lesson", "I'm Coming For You Beeacchhes!",
                    "A Fire Has Been Lit That Will Never Be Extinguished!"]



while True:
    question = random.choice(questions)
    answer = question_answer[question]
    user_answer = raw_input(question)
# Creates a random number so that a different motivationalText message is displayed when a correct answer is given
    for x in range(1):
        value = random.randint(1,5)
#        print(value)
    if user_answer == answer:
        print("\n")
        print(motivationalText[value])
        print("\n")
    elif user_answer == "quit":
        print"\n********************************** Thank you for using Python Quiz", (name) + " *******************Bye For Now!!"
        break
    else:
        print("Wrong! ... The correct answer is ", answer)
