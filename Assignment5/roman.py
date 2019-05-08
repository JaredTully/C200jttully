def roman(number):
    hundred = "C"
    fifty = "L"
    ten = "X"
    five = "V"
    one = "I"

    output = ""

    if (number / 10) >= 1:

        if number < 100 and number > 89:
            output = ten + hundred
            number = number - 90

        if number >= 50:
            output = fifty
            number = number - 50

        if number >= 40 and number < 50:
            output = output + ten + fifty
            number = number - 40

        while (number >= 10):
            output = output + ten
            number = number - 10

    if number == 9:
        output = output + one + ten
        number = number -9

    if number < 9 and number >= 5:
        output = output + five
        number = number - 5

    if number == 4:
        output = output + one + five
        number = number - 4

    while ((number / 1) >= 1):
        output = output + one
        number = number -1 

    return output

for i in range(1,100):
    if i % 5 == 0:
        print()
    print(i, roman(i), ", ", end="")