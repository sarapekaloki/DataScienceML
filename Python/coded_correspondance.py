alphabet = 'abcdefghijklmnopqrstuvwxyz'

def caesar_decode(message, offset):
    decoded_message = ''
    for char in message:
        if char in alphabet:
            char_idx_plus_offset = alphabet.index(char) + offset 
            decoded_char_idx = char_idx_plus_offset if char_idx_plus_offset == 0 else char_idx_plus_offset % len(alphabet)
            decoded_message += alphabet[decoded_char_idx]                
        else: 
            decoded_message += char
        
    return decoded_message
message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'

print(caesar_decode(message, 10))

def caesar_encode(message, offset):
    encoded_message = ''
    for char in message:
        if char in alphabet:
            encoded_message += alphabet[alphabet.index(char) - offset]
        else:
            encoded_message += char
    return encoded_message

message = 'hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!'
print(caesar_encode(message, 10))

print(caesar_decode('jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.', 10))
print(caesar_decode('bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!', 14))


brute_force_message = 'vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx'
for i in range(20):
    print(f"{caesar_decode(brute_force_message, i)}, {i} offset")
    
    
def vigenere_cipher(message, key_word, cipher_function):
    cipher_message = ''
    key_word_idx = 0
    for char in message:
        if char in alphabet:
            key_word_char = key_word[key_word_idx%len(key_word)]
            decoded_char = cipher_function(char, alphabet.index(key_word_char))
            key_word_idx += 1
            
            cipher_message += decoded_char
        else:
             cipher_message += char
    return cipher_message

message = 'txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!'
key_word = 'friends'
print(vigenere_cipher(message, key_word, caesar_decode))

my_message = 'chiwinky is asleep right now shes really lazy'

key_word = 'peka'

print(vigenere_cipher(vigenere_cipher(my_message, key_word, caesar_decode), key_word, caesar_encode))
