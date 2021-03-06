# Function to do insertion sort

def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)): # tem que começar em 1, porque mais em baixo vai comparar com o anterior. E se não tiver um anterior, não tem com o que comparar.

        key = arr[i]

        # move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1 # posição anterior ao i. se o i for a 3ª posição, j vai ser a 2ª posição.

        while j >= 0 and key < arr[j]:
            """
            while j maior ou igual a zero, isso comparando a posição j. key menor que arr[j]
            lembrando que key é key = arr[i], ou seja, key guarda o elemento do vetor arr que esta na posição i.
            então key < arr[j] esta comparando o elemento que esta do vetor arr que esta na posição i, com o elemento do vetor arr que esta na posição j 
            """

            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# test

arr = [13, 11, 12, 5, 6]
insertionSort(arr)

#print
for i in range(len(arr)):
    print("% d" % arr[i])