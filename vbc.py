import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: vbc.py <integer>")
        sys.exit(1)
    # else if the argument type is not an integer
    elif not sys.argv[1].isdigit():
        print("Usage: vbc.py <integer greater than 0> (Do not use letters)")
        sys.exit(1)
    elif int(sys.argv[1]) <= 0:
        print("Usage: vbc.py <integer greater than 0>")
        sys.exit(1)

    else:
        n = int(sys.argv[1])
        # convert the number to a variable byte integer

        if n < 127:
            binary = bin(n)[2:]

            # if the length of the binary is less than 7, add 0s to the front
            if len(binary) < 7:
                binary = '1' + '0' * (7 - len(binary)) + binary
            else:
                binary = '1' + binary

            # print the binary
            print(binary)

        else:
            finalBinary = ''
            # get the length of the binary
            length = len(bin(n)[2:])
            # convert to binary
            binary = bin(n)[2:]

            # get the last 7 bits of the binary and add 1
            lowerBits = int('1' + binary[length - 7:])

            # get the higher bits of the binary
            higherBits = ''

            binary = binary[::-1]

            # from the 7nth bit to the end of the binary, every 7 bits
            for i in range(7, length, 7):
                # add 0 to the 7 bits
                higherBits = binary[i:i + 7]
                # reverse the higher bits
                higherBits = higherBits[::-1]
                # if the length of the higher bits is lower than 8, add 0s to the front
                if len(higherBits) < 8:
                    higherBits = '0' * (8 - len(higherBits)) + higherBits
                # add the higher bits to the front of the final binary
                finalBinary = higherBits + finalBinary

            # add the lower bits to the final binary
            finalBinary += str(lowerBits)

            # print the final binary
            print(finalBinary)
