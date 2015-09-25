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
"Define the following function GetAnswer": "def GetAnswer():",
"Call the following function def GetAnswer(value):": "GetAnswer(value)",
"What is the import statement used for?": "import modules so they can be used in current program",
"Import the following module called brompton": "import brompton",
"Name 3 statements that conditionally execute a block of code": "if else elif",
"What does the class statement do?": "attaches it's local namespace to a class and executes a block of code",
"Name 3 statements that work together to raise, catch, and clean up code from exceptions": "try except finally",
"Name 2 programs that can be used to install python programs": "easy_install and pip",
"Write the code to open countries.txt in read mode and assign to variable file": "file = open(\"countries.txt\", \"r\")",
"Write the code to open countries.txt in write mode and assign to variable file": "file = open(\"countries.txt\"), \"w\")",
"How is BeautifulSoup4 installed from the command line using pip?": "pip install BeautifulSoup4",
"Write the line of code to close the following file opened like this f = open(\"states.txt\", \"w\")": "f.close()",
"Name 3 types of applications that can be written with python": "web games scripts",
"How is BeautifulSoup4 installed using easy_install from the command line?": "easy_install BeautifulSoup4",
"Can python be used for object oriented programming (yes or no)?": "yes",
"What two ways can comments be specified in a python program?": "# or beginning and ending triple quotes",
"Name 2 popular cross platform (Windows, Linux, Mac OSX) python GUI frameworks?": "wxPython and PyQT",
"What is python?": "modern interpreted programming language with objects, modules, threads, exceptions, and automatic memory management",
"What is a negative index in python": "pythons arrays and lists can be accessed with positive and negative indexes",
"Name 2 ways to execute python scripts?": "open IDE and run or python scriptname.py",
"What does a Unit Test test?": "tests a programs functionality in isolation",
"What do integration tests test?": "They test that a programs modules work together",
"What application needs to be installed in Python 2.7 in order to be able to create a virtual environment?": "virtualenvwrapper",
"How is a virtual environment activated?": "source /bin/activate",
"How is a virutal environment deactivated?": "source /bin/deactivate",
"How is a virtual environment requirements.txt file created?": "pip freeze > requirements.txt",
"How can information on an installed package called Sphinx be shown?": "pip show Sphinx",
"What is the name of the debugger that can be used to debug python programs?": "pdb",

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
