import functions as fn
import matrices as matrix
import base64
import numpy as np
cypher_text= ""
def encode_text_function(plain_text:str,key:str):
    global cypher_text
    key_matrix =[]
    key_matrix_length=0
    if(fn.has_numbers(key) or fn.has_numbers(plain_text)):
        key_matrix = matrix.generate_key_matrix_6x6(key.upper())
        key_matrix_length=6
    else:
        key_matrix_length=5
        key_matrix = matrix.generate_key_matrix_5x5(key.upper())
    if len(plain_text)%2==1:
        plain_text+='X'
    plain_text = plain_text.upper()
    plain_text = fn.insert_X_duplicates(plain_text)
    cypher_text=""
    for pair in zip(plain_text[0::2], plain_text[1::2]):
        pair_1, pair_2 = pair[0], pair[1]
        pos1 = np.argwhere(key_matrix == pair_1)
        pos2 = np.argwhere(key_matrix == pair_2)
        print((pos1[0, 1] + 1) )
        if(pos1[0,0]==pos2[0,0]):#in the same row
            letter1 = key_matrix[pos1[0, 0], (pos1[0, 1] + 1) % key_matrix_length]
            letter2 = key_matrix[pos2[0, 0], (pos2[0, 1] + 1) % key_matrix_length]
            cypher_text+=letter1+letter2
        elif(pos1[0,1]==pos2[0,1]):#in the same column
            letter1 = key_matrix[(pos1[0, 0]+1)%key_matrix_length, pos1[0, 1]]
            letter2 = key_matrix[(pos2[0, 0]+1) % key_matrix_length, pos2[0, 1]]
            cypher_text+=letter1+letter2
        else:#in different row,column
            letter1=key_matrix[pos1[0,0],pos2[0,1]]
            letter2=key_matrix[pos2[0,0],pos1[0,1]]
            cypher_text+=letter1+letter2
    print(cypher_text)
    return cypher_text


def encode_image_to_base64(image_path,key,output_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encode_image_function(encoded_string.decode('utf-8'),key,output_path)
def encode_image_function(plain_image:str,key:str,output_path:str):
    key_matrix = matrix.generate_key_matrix_8x8(key)
    key_matrix_length=8
    plain_image = fn.remove_equal(plain_image)
    plain_image = fn.insert_X_Image_duplicates(plain_image)
    cypher_image=""
    for pair in zip(plain_image[0::2], plain_image[1::2]):
        try:
            pair_1, pair_2 = pair[0], pair[1]
            pos1 = np.argwhere(key_matrix == pair_1)
            pos2 = np.argwhere(key_matrix == pair_2)
            if(pos1[0,0]==pos2[0,0]):#in the same row
                letter1 = key_matrix[pos1[0, 0], (pos1[0, 1] + 1) % key_matrix_length]
                letter2 = key_matrix[pos2[0, 0], (pos2[0, 1] + 1) % key_matrix_length]
                cypher_image+=letter1+letter2
            elif(pos1[0,1]==pos2[0,1]):#in the same column
                letter1 = key_matrix[(pos1[0, 0]+1)%key_matrix_length, pos1[0, 1]]
                letter2 = key_matrix[(pos2[0, 0]+1) % key_matrix_length, pos2[0, 1]]
                cypher_image+=letter1+letter2
            else:#in different row,column
                letter1=key_matrix[pos1[0,0],pos2[0,1]]
                letter2=key_matrix[pos2[0,0],pos1[0,1]]
                cypher_image+=letter1+letter2
        except:
            print(pair)
    with open(output_path, "w") as image_file:
        image_file.write(cypher_image)
    return cypher_image


def encode_wav_function(plain_wav:str,key:str,output_path):
    key_matrix = matrix.generate_key_matrix_8x8(key)
    key_matrix_length=8
    plain_wav= fn.remove_equal(plain_wav)
    plain_wav = fn.insert_X_Audio_duplicates(plain_wav)
    cypher_wav=""
    for pair in zip(plain_wav[0::2], plain_wav[1::2]):
        try:
            pair_1, pair_2 = pair[0], pair[1]
            pos1 = np.argwhere(key_matrix == pair_1)
            pos2 = np.argwhere(key_matrix == pair_2)
            if(pos1[0,0]==pos2[0,0]):#in the same row
                letter1 = key_matrix[pos1[0, 0], (pos1[0, 1] + 1) % key_matrix_length]
                letter2 = key_matrix[pos2[0, 0], (pos2[0, 1] + 1) % key_matrix_length]
                cypher_wav+=letter1+letter2
            elif(pos1[0,1]==pos2[0,1]):#in the same column
                letter1 = key_matrix[(pos1[0, 0]+1)%key_matrix_length, pos1[0, 1]]
                letter2 = key_matrix[(pos2[0, 0]+1) % key_matrix_length, pos2[0, 1]]
                cypher_wav+=letter1+letter2
            else:#in different row,column
                letter1=key_matrix[pos1[0,0],pos2[0,1]]
                letter2=key_matrix[pos2[0,0],pos1[0,1]]
                cypher_wav+=letter1+letter2
        except:
            print(pair)
    with open(output_path, "w") as wav_file:
        wav_file.write(cypher_wav)
    return cypher_wav


def encode_wav_to_base64(wav_file_path,key,output_path):
    with open(wav_file_path, "rb") as wav_file:
        encoded_bytes = base64.b64encode(wav_file.read())
    return encode_wav_function(encoded_bytes.decode('utf-8'),key,output_path)


# encode_text_function("maro","sxvf")
# encode_image_to_base64("./image/image_3.jpg","deso2365","image_3_encoded.jpg")
