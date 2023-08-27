# O(N**2)
# def strcounter(s):
#     for i in set(s):
#         count=0           #Самый худшй вариант из написаных
#         for a in s:
#             if i == a:
#                 count += 1
#         print(f'{i} - {count}')


# O(N)
# def strcounter(s):
#    for i in set(s):               #Лучший вариант
#         print(f'{i} - {s.count(i)}')


def strcounter(s):
    sym_dict={}
    for sym in set(s):     #Перебираем все буквы
        sym_dict[sym] = sym_dict.get(sym, 0) + 1            #Вариант со словарём

    for sym, count in sym_dict.items():    #Перебираем все значения словаря
        print(f'{sym} - {count}')

strcounter('abcc')  
