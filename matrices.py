import numpy as np
def generate_key_matrix_6x6(key):
    key = "".join(dict.fromkeys(key)) #to remove duplicates

    # Create the initial matrix with the key
    matrix = list(key) #change it to 1d array
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for letter in alphabet:
        if letter not in matrix:
            matrix.append(letter)#fill matrix with missing chars
    print(matrix)
    matrix = np.array(matrix)#convert it to np
    matrix = matrix.reshape((6, 6))#reshape it to 2d array 6x6
    return matrix
def generate_key_matrix_5x5(key):
    key = "".join(dict.fromkeys(key)) #to remove duplicates
    key = key.replace("J", "I")
    # Create the initial matrix with the key
    matrix = list(key) #change it to 1d array
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        if letter not in matrix:
            matrix.append(letter)#fill matrix with missing chars
    matrix = np.array(matrix)#convert it to np
    matrix = matrix.reshape((5,5))#reshape it to 2d array 5x5
    print(matrix)
    return matrix

def generate_key_matrix_8x8(key):
    key = "".join(dict.fromkeys(key)) #to remove duplicates

    # Create the initial matrix with the key
    matrix = list(key) #change it to 1d array
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/"
    for letter in alphabet:
        if letter not in matrix:
            matrix.append(letter)#fill matrix with missing chars
    print(matrix)
    matrix = np.array(matrix)#convert it to np
    matrix = matrix.reshape((8, 8))#reshape it to 2d array 8x8
    return matrix