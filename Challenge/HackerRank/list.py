if __name__ == '__main__':
    N = int(input())
    vector = []
    for i in range(N):
        command = input().split()
        if command[0] == 'insert':
            vector.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(vector)
        elif command[0] == 'remove':
            vector.remove(int(command[1]))
        elif command[0] == 'append':
            vector.append(int(command[1]))
        elif command[0] == 'sort':
            vector.sort()
        elif command[0] == 'pop':
            vector.pop()
        elif command[0] == 'reverse':
            vector.reverse()
        else:
            print('Invalid command')