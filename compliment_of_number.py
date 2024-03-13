# finding binary of number

def FindComplement(num):

    binary = bin(num)[2:]
    complement = ''

    # visit every bit and flit it
    for bit in binary:
        if bit == '1':
            complement += '0'
        else:
            complement += '1'

    # converting to interger with base 2
    return (int(complement,2))


n = int(input("Enter number: "))
print("Compliment of ",n,":",FindComplement(n))

