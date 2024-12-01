# Импортируем библиотеку для выполнения HTTP-запросов в интернет
import requests
# Импортируем функцию log из модуля math:
from math import log

# Читаем текстовый файл по url-ссылке
data = requests.get("https://raw.githubusercontent.com/SkillfactoryDS/Datasets/master/war_peace_processed.txt").text

# Предобрабатываем текстовый файл
data = data.split('\n')
data.remove('')
data = data + ['[new chapter]']

# Выводим первые 100 слов из книги
#print(data[:100])
# --------------------------------------------------------------------------------------------------
# Превращаем список в множество, удаляя дублирующиеся слова
word_set = set(data)
# Удаляем из множества слово, символизирующее раздел между главами
word_set.discard('[new chapter]')
# Выводим результаты
#rint('Общее количество слов: {}'.format(len(data)))
#print('Общее количество уникальных слов: {}'.format(len(word_set)))
# --------------------------------------------------------------------------------------------------
# Инициализируем пустой словарь
word_counts = {}
# Инициализируем количество глав
count_chapter = 0
# Создаем цикл по всем словам из списка слов
for word in data:
    # Проверяем, что текущее слово - обозначение новой главы
    if word == '[new chapter]':
        # Если условие выполняется, то увеличиваем количество глав на 1
        count_chapter += 1
        # Переходим на новую итерацию цикла
        continue
    # Проверяем, что текущего слова еще нет в словаре слов
    if word not in word_counts:
        # Если условие выполняется, инициализируем новый ключ 1
        word_counts[word] = 1
    else:
        # В противном случае, увеличиваем количество слов на 1
        word_counts[word] += 1

# Выводим количество глав
#print('Количество глав: {}'.format(count_chapter))

# Создаем цикл по ключам и их порядковым номерам полученного словаря
for i, key in enumerate(word_counts):
    # Выводим только первые 10 слов
    if i == 10:
        break
    #print(key, word_counts[key])
# --------------------------------------------------------------------------------------------------
# Инициализируем общий список, в котором будем хранить списки слов в каждой главе
chapter_data = []
# Инициализируем список слов, в котором будет хранить слова одной главы
chapter_words = []

# Создаем цикл по всем словам из списка
for word in data:
    # Проверяем, что текущее слово - обозначение новой главы
    if word == '[new chapter]':
        # Если условие выполняется, добавляем список со словами из главы в общий список
        chapter_data.append(chapter_words)
        # Обновляем (перезаписываем) список со словами из текущей главы
        chapter_words = []
    else:
        # В противном случае, добавляем текущее слово в список со словами из главы
        chapter_words.append(word)

# Проверяем, что у нас получилось столько же списков, сколько глав в произведении
#print('Вложенный список содержит {} внутренних списка'.format(len(chapter_data)))
# Выведем первые 100 слов 0-ой главы
#print(chapter_data[0][:100])
# --------------------------------------------------------------------------------------------------
# Инициализируем список, в котором будем хранить словари
chapter_words_count = []

# Создаем цикл по элементам внешнего списка со словами
for chapter_words in chapter_data:
    # Инициализируем пустой словарь, куда будем добавлять результаты
    temp = {}
    # Создаем цикл по элементам внутреннего списка
    for word in chapter_words:
        # Проверяем, что текущего слова еще нет в словаре
        if word not in temp:
            # Если условие выполняется, добавляем ключ в словарь
            temp[word] = 1
        else:
            # В противном случае, увеличиваем количество влождений слова в главу
            temp[word] += 1
    # Добавляем получившийся словарь в список
    chapter_words_count.append(temp)

# Выводим результат
#print(chapter_words_count)
# --------------------------------------------------------------------------------------------------
# Создаем цикл по ключам словаря - спискам слов и их порядковым номерам
for chapter_number, chapter_dict in enumerate(chapter_words_count):
    # Выводим только первые 5 глав
    if chapter_number == 5:
        break
    # Выводим номер главы
    #print('-' * 40)
    #print('Chapter: {}'.format(chapter_number))
    #print('-' * 40)
    # Создаем цикл по ключам - словам и их порядковым номерам
    for j, word in enumerate(chapter_dict):
        # Выводим первые 10 слов из главы
        if j == 10:
            break
        #print(word, chapter_dict[word])

# word_set - множество из всех слов, которые есть в книге
# count_chapter - количество глав в книге (171)
# word_counts - словарь, ключами которого являются слова, а значениями - количество вхождений этих слов в книгу
# chapter_data - список из 171 списка, где элементы вложенных списков - все слова из главы. Каждый список соответствует своей главе
# chapter_words_count - список из 171 словаря, где ключи - слова, а значения - количество слов в главе. Каждый словарь соответствует своей главе
# --------------------------------------------------------------------------------------------------
# Задание 1
# Напишите программу, которая позволит получать частоту употребления любого заданного слова target_word в заданной главе target_chapter.
# Постарайтесь сделать программу максимально обобщенной. То есть желательно рассчитать характеристику tf для всех слов из каждой главы, чтобы впоследствии 
# не было необходимости производить вычисления снова.
# Для этого вы можете для каждой главы создать словарь, ключами которого являются слова, а значения - частота употребления этого слова в этой главе
target_word = 'гостья'
target_chapter = 15

# Инициализация переменных
# n_word_chapter - частота употребления целевого слова target_word в главе target_chapter
n_word_chapter = chapter_words_count[target_chapter][target_word]

# n_chapter - количество слов в книге target_chapter
n_chapter = len(chapter_data[target_chapter])

# Вычислим term frequency для целевого слова target_word в главе target_chapter
tf = n_word_chapter / n_chapter

# Инициализация списка из 171 словаря, где ключи - слова, а значения - частота употребления этого слова в этой главе. Каждый словарь соответствует своей главе
tf_word_chapter = []

# Создаём цикл по списку chapter_words_count, где 
# chapter - номер главы;
# words_count_in_chapter - словарь, ключами которого являются слова, а значения - количество слов в главе
for chapter, words_count_in_chapter in enumerate(chapter_words_count):
    # Создадим пустой словарь, куда будем добавлять результаты
    tf_chapter = {}
    # Создаём цикл по словарю words_count_in_chapter
    for n_word in words_count_in_chapter:
        # Вычислим tf для каждого слова n_word по аналогии с расчётами, приведёнными выше
        # Полученные значения запишем в словарь tf_chapter
        tf_chapter[n_word] = words_count_in_chapter[n_word] / len(chapter_data[chapter])
    # Добавляем получившийся словарь в список
    tf_word_chapter.append(tf_chapter)

# Проверим корректность расчётов и выведем tf для целевого слова и целевой главы
# print(tf_word_chapter[target_chapter][target_word])
# --------------------------------------------------------------------------------------------------
# Задание 2
# Напишите программу, которая позволит вычислять document frequency для заданного слова target_word и выведить результат на экран.
# Пострайтесь сделать программу максимально обобщенной. То есть желательно рассчитать характеристику df для всех уникальных слов из книги, 
# чтобы впоследствии не было необходимости производить вычисления снова.
# Подсказка: Для этого вы можете создать словарь, ключами которого являются слова из книги, а значения - доля документов, содержащих эти слова

target_word = 'человек'

# Инициализация переменных
# n_word - число глав, содержащих слово целевое слово target_word
# Для вычисления n_word используем list comprehension
n_word = len([words for words in chapter_words_count if target_word in words])

# Вычислим document frequency для целевого слова target_word
df = n_word / count_chapter

# Инициализация словаря, ключами которого являются слова из книги, а значения - доли глав книги, содержащих эти слова
df_word = {}

# Создаём цикл по всем словам из списка
for word in data:
    # Получим число глав, содержащих слово word
    n_word_df = len([words for words in chapter_words_count if word in words])
    # Вычислим document frequency для каждого слова в книге
    df_word[word] = n_word_df / count_chapter

# Проверим корректность расчётов и выведем df для целевого слова
# print(df_word[target_word])
# --------------------------------------------------------------------------------------------------
# Задание 3
# Напишите программу, которая позволяет вычислять значение tf-idf для заданного слова target_word в заданной главе target_chapter.
# Постарайтесь сделать программу максимально оптимальной. То есть желательно рассчитать характеристику tf-idf для всех слов из каждой главы книги, 
# чтобы впоследствии не было необходимости производить вычисления снова.

target_word = 'анна'
target_chapter = 4

# Вычислим tf-idf для целевого слова target_word в главе target_chapter
tf_idf = tf_word_chapter[target_chapter][target_word] * log(1 / df_word[target_word])

# Инициализация списка из 171 словаря, где ключи - слова, а значения - величины tf-idf для соответствующего слова в этой главе. 
# Каждый словарь соответствует своей главе
tf_idf_word_chapter = []

# Создаём цикл по списку chapter_data
for chapter_num, chapter in enumerate(chapter_data):
    # Создадим пустой словарь, куда будет добавлять результаты
    tf_idf_chapter = {}
    # Создаём цикл по списку всех слов в chapter
    for word in chapter:
        # Вычислим tf-idf для каждого слова word по аналогии с расчётами, приведёнными выше
        # Полученные значения запишем в словарь tf_idf_chapter
        tf_idf_chapter[word] = tf_word_chapter[chapter_num][word] * log(1 / df_word[word])
    # Добавляем получившийся словарь в список
    tf_idf_word_chapter.append(tf_idf_chapter)

# Проверим корректность расчётов и выведем tf-idf для целевого слова и целевой главы
# print(tf_idf_word_chapter[target_chapter][target_word])

# Задание 4
# Напишите программу, которая позволяет вывести три слова, имеющие самое высокое значение tf-idf в заданной главе target_chapter 
# в порядке убывания tf-idf.

target_chapter = 3

# Осуществим сортировку по ранее созданному словарю tf_idf_word_chapter
# Выведем только три значения с наибольшими значениями tf-idf
tf_idf_contrast = sorted(tf_idf_word_chapter[target_chapter], key=tf_idf_word_chapter[target_chapter].get, reverse=True)[:3]
print(tf_idf_contrast)