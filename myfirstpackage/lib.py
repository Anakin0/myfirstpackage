from xavtest import lib

def try_me():
    print("Do you want to try me?")
    Answer = input()
    if lib.try_me(Answer.lower()) == True:
        return "Hello there."
    if lib.try_me(Answer.lower()) == False:
        return "I find your lack of faith disturbing."

