__author__ = '184766'
""" The following program quizzes the computer user on the python programming language.
"""

import random
#from colorama import init
#from colorama import Fore, Back

#init()



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
"Define the following function call GetAnswer": "def GetAnswer():",
"Call the following function def GetAnswer(value):": "GetAnswer(value)",
"What is the import statement used for?": "import modules so they can be used in current program",
"Import the following module called brompton": "import brompton",
}

questions = list(question_answer.keys())
# print(questions)
question = random.choice(questions)

#user_answer = input(question)
#user_answer.strip()
#print(Fore.RED + 'some red text')

while True:
    question = random.choice(questions)
    answer = question_answer[question]
    user_answer = raw_input(question)
#    str(user_answer)
#    user_answer.strip()
#    print(user_answer)
    if user_answer == answer:
        print("\nCorrect Answer Great Job!  :>) \n")
    elif user_answer == "quit":
        print("Thank you for using Python Quiz....Bye For Now!!")
        break
    else:
        print("Wrong! ... The correct answer is ", answer)
