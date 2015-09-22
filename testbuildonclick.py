__author__ = '184766'

def getQuestionAnswer():
    answer = "test"
    return answer



def onClick(answer):
    var = "test"
    if answer == var:
        print("Answer is equal to test")
    else:
        print("Answer is not equal to test")

def main():
    getQuestionAnswer()
    onClick(getQuestionAnswer())

main()