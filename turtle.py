import random
print("Hello! Welcome to the test")

NoOfQuestions = input ('Choose the number of questions you wish to answer')
for i in NoOfQuestions:
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    symbol = random.randint(1,4)
    if symbol == 1:
         question = number1 + number2
        answer = input('what is' + number1 + ' + ' + number2)
    elif symbol == 2:
        question = number1 - number2
        answer = input('what is' + number1 + ' - ' + number2)
    elif symbol == 3:
        question = number1 * number2
        answer = input('what is' + number1 + ' * ' + number2)
    elif symbol == 4:
        question = number1 / number2
        answer = input('what is' + number1 + ' / ' + number2)
    if answer == question:
        print("You got the question correct!")
        NoCorrect = NoCorrect + 1
    else:
        print("You got the question wrong")

print("You got " + NoCorrect + "questions correct " + " out of " + NoOfQuestions)



