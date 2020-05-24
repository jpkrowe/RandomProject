import random
print("Hello! Welcome to the test")

NoOfQuestions = int(input('Choose the number of questions you wish to answer'))
NoCorrect = 0
i = 0
while i < NoOfQuestions:
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    symbol = random.randint(1, 3)
    if symbol == 1:
        question = number1 + number2
        answer = int(input('what is ' + str(number1) + ' + ' + str(number2)))
    elif symbol == 2:
        question = number1 - number2
        answer = int(input('what is ' + str(number1) + ' - ' + str(number2)))
    elif symbol == 3:
        question = number1 * number2
        answer = int(input('what is ' + str(number1) + ' * ' + str(number2)))
    if answer == question:
        print("You got the question correct!")
        NoCorrect += 1
    else:
        print("You got the question wrong")
    i += 1
print("You got " + str(NoCorrect) + " questions correct out of " + str(NoOfQuestions))



