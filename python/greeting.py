# -*- coding: euc-kr -*-
def greeting( dir):
    with open( dir + '\\'  + 'greeting.txt', 'w+' , encoding='utf-8') as f:
        f.write('안녕하세요. 객체 호출')
    return '성공'