def convert_bytes(stroka): 
    """ Функция кодирования в байт код
        
    Принимает значение 'stroka' и кодирует в 'utf_32_be'
    и возвращает закодированную страку 'byte_stroka'
        
    """
    byte_stroka = stroka.encode('utf_32_be') # для наглядности применил кодировку 'utf_32_be'
    print('Ваша закодированая строка: ', byte_stroka)
    return byte_stroka

def convert_stroca(byte_stroka): 
    """ Функция декодирования в байт код
        
    Принимает значение 'byte_stroka' и декодирует в 'utf_32_be'
    и возвращает раскодированую страку 'stroka'
        
    """          
    stroka = byte_stroka.decode('utf_32_be')
    print('Ваша раскодированая строка: ', stroka)  

stroka = ''    

while stroka != 'exit':    
    stroka = input('\n \nвведите страку для кодирования в байты \nдля выхода нажминте \"exit\": ')
    if stroka != 'exit':
        byte_stroka = convert_bytes(stroka)
        convert_stroca(byte_stroka)


