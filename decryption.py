import functions as fn
import matrices as matrix
import numpy as np
import base64


def decode_text_function(cypher_text:str,key:str):
    key_matrix_length = 0
    key_matrix =[]
    if(fn.has_numbers(key) or fn.has_numbers(cypher_text)):
        key_matrix = matrix.generate_key_matrix_6x6(key.upper())
        key_matrix_length=6
    else:
        key_matrix = matrix.generate_key_matrix_5x5(key.upper())
        key_matrix_length = 5
    plain_text=""
    for pair in zip(cypher_text[0::2], cypher_text[1::2]):
        pair_1, pair_2 = pair[0], pair[1]
        pos1 = np.argwhere(key_matrix == pair_1)
        pos2 = np.argwhere(key_matrix == pair_2)
        if(pos1[0,0]==pos2[0,0]):#in the same row
            letter1 = key_matrix[pos1[0, 0], (pos1[0, 1] - 1) % key_matrix_length]
            letter2 = key_matrix[pos2[0, 0], (pos2[0, 1] - 1) % key_matrix_length]
            plain_text += letter1+letter2

        elif(pos1[0,1]==pos2[0,1]):#in the same column
            letter1 = key_matrix[(pos1[0, 0]-1)%key_matrix_length, pos1[0, 1]]
            letter2 = key_matrix[(pos2[0, 0]-1) % key_matrix_length, pos2[0, 1]]
            plain_text += letter1+letter2
        else:#in different row,column
            letter1=key_matrix[pos1[0,0],pos2[0,1]]
            letter2=key_matrix[pos2[0,0],pos1[0,1]]
            plain_text += letter1+letter2
    plain_text= plain_text.replace('X','')
    print(plain_text)
    return plain_text

def decode_base64_to_image(playfair_encoded_image, key,output_path):
    with open(playfair_encoded_image, "r") as image_file:
        encoded_string = image_file.read()
    decoded_data = base64.b64decode(decode_image_function(encoded_string,key))
    with open(output_path, "wb") as image_file:
        image_file.write(decoded_data)

def decode_image_function(cypher_image:str,key:str):
    key_matrix = matrix.generate_key_matrix_8x8(key)
    key_matrix_length=8
    plain_text=""
    for pair in zip(cypher_image[0::2], cypher_image[1::2]):
        pair_1, pair_2 = pair[0], pair[1]
        pos1 = np.argwhere(key_matrix == pair_1)
        pos2 = np.argwhere(key_matrix == pair_2)
        if(pos1[0,0]==pos2[0,0]):#in the same row
            letter1 = key_matrix[pos1[0, 0], (pos1[0, 1] - 1) % key_matrix_length]
            letter2 = key_matrix[pos2[0, 0], (pos2[0, 1] - 1) % key_matrix_length]
            plain_text += letter1+letter2

        elif(pos1[0,1]==pos2[0,1]):#in the same column
            letter1 = key_matrix[(pos1[0, 0]-1)%key_matrix_length, pos1[0, 1]]
            letter2 = key_matrix[(pos2[0, 0]-1) % key_matrix_length, pos2[0, 1]]
            plain_text += letter1+letter2
        else:#in different row,column
            letter1=key_matrix[pos1[0,0],pos2[0,1]]
            letter2=key_matrix[pos2[0,0],pos1[0,1]]
            plain_text += letter1+letter2
    plain_text = fn.replace_equal(plain_text)
    plain_text= plain_text.replace("//X/",'')
    return plain_text



def decode_base64_to_wav(playfair_encoded_wav, key,output_path):
    with open(playfair_encoded_wav, "r") as wav_file:
        encoded_string = wav_file.read()
    decoded_data = base64.b64decode(decode_wav_function(encoded_string,key))
    with open(output_path, "wb") as wav_file:
        wav_file.write(decoded_data)

def decode_wav_function(cypher_wav:str,key:str):
    key_matrix = matrix.generate_key_matrix_8x8(key)
    key_matrix_length=8
    plain_wav=""
    for pair in zip(cypher_wav[0::2], cypher_wav[1::2]):
        pair_1, pair_2 = pair[0], pair[1]
        pos1 = np.argwhere(key_matrix == pair_1)
        pos2 = np.argwhere(key_matrix == pair_2)
        if(pos1[0,0]==pos2[0,0]):#in the same row
            letter1 = key_matrix[pos1[0, 0], (pos1[0, 1] - 1) % key_matrix_length]
            letter2 = key_matrix[pos2[0, 0], (pos2[0, 1] - 1) % key_matrix_length]
            plain_wav += letter1+letter2

        elif(pos1[0,1]==pos2[0,1]):#in the same column
            letter1 = key_matrix[(pos1[0, 0]-1)%key_matrix_length, pos1[0, 1]]
            letter2 = key_matrix[(pos2[0, 0]-1) % key_matrix_length, pos2[0, 1]]
            plain_wav += letter1+letter2
        else:#in different row,column
            letter1=key_matrix[pos1[0,0],pos2[0,1]]
            letter2=key_matrix[pos2[0,0],pos1[0,1]]
            plain_wav += letter1+letter2
    plain_wav = fn.replace_equal(plain_wav)
    plain_wav = plain_wav.replace("//X///","")

    return plain_wav

# decode_base64_to_image("image_3_encoded.jpg","deso2365","image_3_decoded.jpg")
