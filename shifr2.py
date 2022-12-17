from cryptography.fernet import Fernet


def write_key():
    """ Функция генирации ключа
        
    генирируется ключ и записывается в файл 'crypto.key'
        
    """ 
    key = Fernet.generate_key()
    with open('crypto.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    """ Функция принимет значения ключа
        
    load_key() принимет значения ключа из файла 'crypto.key'
        
    """ 
    return open('crypto.key', 'rb').read()


def encrypt(filename, key, filename2):
    """ Функция шифрования
        
    шифруется текст аргумента 'filename' ключом 'key' и зашифрованый текст передается в 'filename2' 
        
    """
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    with open(filename2, 'wb') as file2:
        file2.write(encrypted_data)


def decrypt(filename2, key, filename3):
    """ Функция дешифрования
        
    дешифруется текст аргумента 'filename2' ключом 'key' и  текст передается в 'filename3'
        
    """
    f = Fernet(key)
    with open(filename2, 'rb') as file2:
        encrypted_data = file2.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename3, 'wb') as file3:
        file3.write(decrypted_data)

# раскомментируйте следующую строку, если запускаете код впервые, чтобы сгенерировать ключ
write_key()
# загрузить ключ
key = load_key()
# имя шифруемого файла
file = 'test1.txt'
file2 = 'test2.txt'
file3 = 'test3.txt'
# зашифровать файл
encrypt(file, key, file2)
print('Зашифрованный текст из файла \"test1.txt\" помещен в файл \"test2.txt\"')
decrypt(file2, key, file3)
print('Расшифрованый текст помещен в файл \"test3.txt\"')