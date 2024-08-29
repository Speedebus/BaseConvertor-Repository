def int_to_list(number):
    number = str(number)
    numberlist = []
    for digit in number:
        numberlist.append(int(digit))
    return numberlist


def convert_to_baseten(number, base):
    numberlist = int_to_list(number)
    baseten = 0
    length = len(numberlist)
    opposite = 1
    for digit in numberlist:
        power = length - opposite
        baseten += digit * base**power
        opposite += 1
    return baseten

    
def convertbase(number,base,newbase):
    output = ""
    baseten = int(convert_to_baseten(number, base))
    output_list = []
    quotient = baseten
    while quotient > 0:
        digit = quotient%newbase
        output_list.insert(0,int(digit))
        withoutdigit = quotient-digit
        quotient = withoutdigit/newbase
    for digit in output_list:
        output += str(digit)
    output = int(output)
    return output
try:
    number = int(input("What is the current number: "))
    base = int(input("What base is this in: "))
    newbase = int(input("What base would you like to convert this into: "))
except ValueError:
    print("That is not an integer")
print(convertbase(number,base,newbase))