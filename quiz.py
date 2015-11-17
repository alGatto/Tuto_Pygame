__author__ = 'alGatto'

class Quiz():
    """La class des quiz"""
    def __init__(self):
        self.question = ""
        self.rep1 = ""
        self.rep2 = ""
        self.rep3 = ""
    def quiz(self):
        print("Question 1")
        print("What percentage of the land is used for farming?")
        print()
        print("a. 25%")
        print("b. 50%")
        print("c. 75%")
        answer = input("Make your choice: ")
        if answer == "c":
            print("Correct!")
