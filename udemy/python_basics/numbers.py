
underscore_number = 10_500_000
addition_number = 1+2
extended_float = 0.1
if addition_number == 3:
    print("True")
# Addition of 2 Float Numbers doesn't give the exact answers
float_numbers=0.1+0.1+0.1
if float_numbers ==0.3:
    print("True")
    print("The actual summation value is {}".format(format(0.1+0.1+0.1),'0.25f'))

print("UnderScore Number: {}".format(underscore_number))
print("Summation of Number: {}".format(addition_number))
print("Exact Float: {}".format(format(extended_float,'.25f')))