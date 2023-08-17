def solution(N):
    binary = bin(N).replace("0b", "")
    numbers = list(str(binary))
    for num in numbers:
        print(num)

solution(4)