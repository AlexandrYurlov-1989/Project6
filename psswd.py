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
        
    
        return you_password + ' Хороший пароль'


    def test():
        """ Функция тест проверки паролей и вывода их соответствия
        
        Проверяет наличие в пароле цифр букв верхнего и нижнего регистра, а также совподений с 'password' используя функцию 'chek'
        
        """             # эта функция содержит блок паролей для проверки. Вы можете изменять пароли внутри блока для проверки либо написать вручную при старте программы
        a = chek("Sword")
        b = chek(12345678)
        c = chek("Eskaliburus")
        d = chek("123DKLSDFGS")
        e = chek("123eskaliburus")
        f = chek("PaSSworD1")  # пароль заведомо не проходил проверку из-за отсутствия цифр пришлось для примера работы функции добавить одну цифру
        g = chek("eskaliburus") 
        h = chek("KHFHJKJJ")  
        print("пример недопустимых паролей:")
        print("пароль неверный - Sword - ", a)
        print("пароль неверный - 12345678 -", b)
        print("пароль неверный - Eskaliburus -", c)
        print("пароль неверный - 123DKLSDFGS -", d)
        print("пароль неверный - 123уskaliburus -", e)
        print("пароль неверный - PaSSworD1 -", f)
        print("пароль неверный - eskaliburus -", g)
        print("пароль неверный - KHFHJKJJ -", h)

    def input_password():
        """ Функция набора пароля и его вывода
        
        Введите любой пароль
        
        """
        you_password = chek(input("введите пароль: "))
        print("Вашь пароль -", you_password)

    test()
    input_password()


password()