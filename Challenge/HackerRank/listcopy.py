if __name__ == '__main__':
    N = int(input())
    vetor = []
    for i in range(N):
        inputCommand = input().split()
        if(inputCommand[0] == "append"):
            vetor.append(int(inputCommand[1]))
        elif(inputCommand[0] == "insert"):
            vetor.insert(int(inputCommand[1]), int(inputCommand[2]))
        elif(inputCommand[0] == "remove"):
            vetor.remove(int(inputCommand[1]))
        elif(inputCommand[0] == "sort"):
            vetor.sort()
        elif(inputCommand[0] == "pop"):
            vetor.pop()
        elif(inputCommand[0] == "reverse"):
            vetor.reverse()
        elif(inputCommand[0] == "print"):
            print(vetor)
        else:
            print("Invalid Command")
