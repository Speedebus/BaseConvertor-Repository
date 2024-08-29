def int_to_list(number):
    number = str(number)
    numberlist = []
    for digit in number:
        numberlist.append(int(digit))
    return numberlist
def base_converter(number, base, new_base):
    numberlist = int_to_list(number)
    baseten = 0
    length = len(numberlist)
    opposite = 1
    for digit in numberlist:
        power = length - opposite
        baseten += digit * base**power
        opposite += 1
    print(baseten)
base_converter(123,4,19)
