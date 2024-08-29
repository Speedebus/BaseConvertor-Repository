def convert(number, current_base, new_base):
    number = str(number)
    numberlist = []
    for digit in number:
        numberlist.append(int(digit))
    print(numberlist)
convert(133,325,2326)