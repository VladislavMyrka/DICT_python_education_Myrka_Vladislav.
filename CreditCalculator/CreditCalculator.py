monthlyPayment = 0
loan = 0
interestRate = 0
numberOfPayments = 0
loanDurationInYears = 0


strLoan = input("How much money will you borrow? ")
strInterestRate = input("What is the interest rate on the loan? ")
strLoanDurationInYears = input("How many years will it take you to pay off the loan? " )


loanDurationInYears = float(strLoanDurationInYears)
loan = float(strLoan)
interestRate = float(strInterestRate)


numberOfPayments = loanDurationInYears*12


monthlyPayment = loan * interestRate * (1+ interestRate) * numberOfPayments \
    / ((1 + interestRate) * numberOfPayments -1)


print("Your monthly payment will be " + str(monthlyPayment))


print("Your monthly payment will be $%.2f" % monthlyPayment)