def solution(N):
    maxlen = 0
    counter = 0
    foundOne = False
    
    binary = bin(N).replace("0b", "")
    
    numbers = list(str(binary))
    
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