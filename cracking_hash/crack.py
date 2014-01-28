import string
import itertools
import hashlib
import time
import pp
import pdb

def generate_key(length):
    charset = string.ascii_letters + string.digits + string.punctuation
    wordlist = []
    for combination in itertools.product(charset, repeat=length):
        word = ''.join(combination)
        wordlist.append(word)
    return wordlist

def check_encryption(password):
    if len(password) == 32:
        return 'md5'
    elif len(password) == 40:
        return 'sha1'
    elif len(password) == 56:
        return 'sha224'
    elif len(password) == 128:
        return 'sha512'

def encrypt(word, encryption):
    if encryption == 'md5':
        return hashlib.md5(word).hexdigest()
    elif encryption == 'sha1':
        return hashlib.sha1(word).hexdigest()
    elif encryption == 'sha224':
        return hashlib.sha224(word).hexdigest()
    elif encryption == 'sha512':
        return hashlib.sha512(word).hexdigest()

def process(input_password, input_panjang):
    encryption = check_encryption(input_password)
    #pdb.set_trace()
    result = []
    for length in range(1, input_panjang + 1):
        wordlist = generate_key(length)
        for word in wordlist:
            print word
            if encrypt(word, encryption) == input_password:
            #result = encrypt(word, encryption) == input_password
            #if result:
                print "passwordnya :", word
                return word
                #print "password adalah : %s " % (word)
                #break 
            else:
                pass
                #return word
                #print "sedang proses"
    return None

if __name__ == "__main__":
        #mywordlist = generate_key(i)
        '''input_password = raw_input('Masukkan password untuk di crack : ' )
        input_panjang = int(raw_input('masukkan kemungkinan panjang charater password :'))
        start_time = time.time()
        hasil = process(input_password, input_panjang)
        print hasil
        if hasil:
            print "password nya adalah : " , hasil
        else:
            print "password tidak ditemukan"
        print "waktu :", time.time() - start_time, "s"'''
