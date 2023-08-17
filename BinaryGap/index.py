def solution(N):
    maxlen = 0
    # Converting number to binary and removing starting binary code i.e 0b.
    binary = bin(N).replace("0b", "")
    # converting number to string then to list
    numbers = list(str(binary))
    foundOne = False
    counter = 0
    for num in numbers:
        if num == str(1):
            if foundOne == True:
                if counter > maxlen:
                    maxlen = counter
                counter = 0
            else:
                foundOne = True
        else:
            if foundOne == True:
                counter = counter + 1
    return maxlen