operandOne = 0.0
operandTwo = 0.0
sum = 0.0
difference = 0.0
quotient = 0.0
product = 0.0
remainder = 0.0

realnumber = int(input("Input the first operand."))
operandOne += realnumber
print("FIRST>", operandOne)

realnumber2 = int(input("Input the second operand."))
operandTwo += realnumber2
print("SECOND>", operandTwo)

sum = operandOne + operandTwo
sum = round(sum, 1)
quotient = operandOne / operandTwo
quotient = round(quotient, 1)
product = operandOne * operandTwo
product = round(product, 1)
remainder = operandOne % operandTwo
remainder = round(remainder, 1)
print("The product of ", operandOne, " and ", operandTwo, " is ", product)
print("OUTPUT ", product)
print("The quotient of ", operandOne, " and ", operandTwo, " is ", quotient)
print("OUTPUT ", quotient)
print("The sum of ", operandOne, " and ", operandTwo, " is ", sum)
print("OUTPUT ", sum)
print("The remainder of ", operandOne, " and ", operandTwo, " is ", remainder)
print("OUTPUT ", remainder)
