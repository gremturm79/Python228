# str1 = input('Напишите строку: ') этот способ берёт слово как элемент, а не символ
# str1 = input('Напишите строку: ')
str1 = 'Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последнего вхождения'
print(str1)
s_old = input('Введите любую букву из строки: ')
s_new = input('Введите любой букву или символ на который хотите поменять букву: ')
str2 = str1.split()  # получаем список элементов из строки
print(str2)
lst = []
a = 0
for i in range(len(str2)):
    if s_old in str2[i]:
        lst.append(i)  # добавляю индексы всех слов выбранных по s_old в список lst
        for j in range(len(lst)):
            a = len(lst) - 1
            if j != 0 and j != a:  # условие при котором отбираются индексы кроме первого и последнего
                str2[lst[j]] = str2[lst[j]].replace(s_old, s_new)
print(' '.join(str2))  # конвертируем список в строку
