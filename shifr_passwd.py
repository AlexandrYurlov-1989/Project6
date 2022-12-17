import math


def password():
    """ Функция ввода пароля с праверкой на соответствие 
        
    Ввод страки содержащию не мение 6 символов, наличие цифры, быквы нижнего и верхнего регистров и не содержащего строки 'password'
        
    """     
    def numbers(you_password): 
        """ Функция проверки наличия цифр в пароле 
        
        Проверяет циклом каждую страку пароля на наличие цифры и возвращает отличное от нуля значение
        
        """
        z = 0                  
        for x in you_password: 
            if x.isdigit():       # isdigit возвращает True, если символ цифра, если верхнего то будет False
                z += 1         
        return z               
    
    def lower_case(you_password): 
        """ Функция проверки наличия строчных букв в пароле
        
        Проверяет циклом каждую страку пароля на наличие строчной буквы и возвращает отличное от нуля значение
        
        """        
        z = 0                     
        for x in you_password:    
            if x.islower():       # islower возвращает True, если символ буква  нижнего регистра, если верхнего то будет False
                z += 1            
        return z                  

    def upper_case(you_password):
        """ Функция проверки наличия Заглавных букв в пароле
        
        Проверяет циклом каждую страку пароля на наличие буквы в верхнем регистре и возвращает отличное от нуля значение
        
        """ 
        z = 0
        for x in you_password:
            if x.isupper():       # isupper возвращает True, если строка является буквой в верхнем регистре, в противном случае значение False.
                z += 1
        return z
                
    def chek(you_password):
        """ Функция проверки пароля на допустимость
        
        Проверяет наличие в пароле цифр букв верхнего и нижнего регистра, а также совподений с 'password'
        
        """
        you_password = str(you_password)
    
        if len(you_password) < 6: # Len Возвращает количество элементов в контейнере.
            return "Ваш пароль должен состоять не менее чем из 6 символов."
        if numbers(you_password) <= 0:
            return "Ваш пароль должен содержать хотя бы одну цифру."
        if lower_case(you_password) <= 0:
            return "Ваш пароль должен содержать буквы нижнего регистра."
        if upper_case(you_password) <= 0:
            return "Ваш пароль должен содержать заглавные буквы." 

        if you_password.lower().find('password') != -1: # Lower Возвращает копию строки, преобразованной в нижний регистр.
            return "Ваш пароль не должен содержать слово “password1” в любом регистре."
        
    
        return you_password 
    
    def input_password():
        """ Функция набора пароля и его вывода
        
        Введите любой пароль
        
        """
        password = chek(input("введите пароль: "))
        print("Вашь пароль -", password)
        return password
    
    return input_password()

def enc_XOR(text, key):
    """ Функция шифрования
        
    функция enc_XOR получает 2 параметра: text, key.

    XOR известен как « исключающее или », который сравнивает два двоичных числа побитово. 
    Если оба бита одинаковы, XOR выводит 0. Если оба бита различны, XOR выводит 1.
        
    """
    return ''.join([chr(ord(c1)^ord(c2)) for (c1, c2) in zip(text, key)])




key = password()  # воспользуюсь своей ранее созданной функцией паролей....пока без загрузки из класса
text = open('test1.txt', 'r', encoding="utf-8").read()

symbols = 0     # посчитаю во сколько раз текст больше пароля чтобы во столько раз увеличить пароль для кодирования
symbolskey = 0

for line in text:
    symbols += len(line.strip('\n'))
for line in key:
    symbolskey += len(line.strip('\n'))

x = symbols/symbolskey

# увеличение ключа чтоб покрыть весь текст для шифрования. 
# Возможно для наименьших ресурсных затрат нужно выполнить 
# разбиение текста на длинну пароля, но так тоже работает
if x > 1:       
    x = math.ceil(x)
    key = key * x

encryp_text = enc_XOR(text, key)
encryp_text2 = encryp_text

f = open('test2.txt', 'w', encoding="utf-8")    # откроем файл только на запись
f.write(encryp_text)          # записываю в файл
print('Зашифрованный текст из файла \"test1.txt\" помещен в файл \"test2.txt\"')
f.close()                     # закрываю файл

decryp_text = enc_XOR(encryp_text2, key)

f = open('test3.txt', 'w', encoding="utf-8")    # откроем файл только на запись

f.write(decryp_text)          # записываю в файл
print('Расшифрованый текст помещен в файл \"test3.txt\"')
f.close()                     # закрываю файл