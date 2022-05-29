#OLD
def calculate(
    operationType,
    firstNumber,
    secondNumber
):
    if operationType == "addition":
        return firstNumber + secondNumber
    elif operationType == "substraction":
        return firstNumber - secondNumber
    elif operationType == "multiplication":
        return firstNumber * secondNumber
    elif operationType == "division":
        if secondNumber == 0:
            return "Error"
        else:
            return firstNumber / secondNumber


#NEW
def calculate(
    operationType,
    firstNumber,
    secondNumber
):
    if operationType == "addition":
        return add(firstNumber, secondNumber)
    elif operationType == "substraction":
        return substract(firstNumber, secondNumber)
    elif operationType == "multiplication":
        return multiply(firstNumber, secondNumber)
    elif operationType == "division":
        if secondNumber == 0:
            return "Error"
        else:
            return divide(firstNumber, secondNumber)
def add(firstNumber, secondNumber):
    return firstNumber + secondNumber

def substract(firstNumber, secondNumber):
    return firstNumber - secondNumber

def multiply(firstNumber, secondNumber):
    return firstNumber * secondNumber

def divide(firstNumber, secondNumber):
    if secondNumber == 0:
        return "Error"
    else:
        return firstNumber / secondNumber