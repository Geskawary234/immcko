import csv #импорт модуля csv

def read_file():

    #эта функция откывает и форматирует csv файл products.csv как мне нужно
    
    products = [] #список со всеми данными из файла
    with open('products.csv', encoding='UTF-8') as db:#открываем файл
        db.readline() #убираем первую строку
        for l in db: #читаем каждую строку из csv файла
            #category, product, date, price per unit, count
            r = [w.replace('\n','') for w in l.split(';')] #форматируем
            products.append(r) #добавляем в список
    return products


#1 задание
db=read_file()
total = 0
total_all = 0
for r in db: #читаем каждую строку из csv файла
    #category, product, date, price per unit, count
    cat = r[0] #категория
    prod = r[1] #продукт
    date = r[2] #дата
    price = float(r[3]) #цена за шт
    count = float(r[4])#кол-во продукта
    if cat == 'Закуски': #если категория "Закуски" то прибавляем к переменной total итоговую цену
        total += price*count
    total_all += price*count #по-любому прибовляем цену к переменной total_all
print(total_all) #вывод цены за все продукты
        
with open('products_new.csv', mode='w', encoding='UTF-8') as pn:
    fw=csv.writer(pn,delimiter=';',lineterminator='\r') #открываем csv файл и читаем его
    fw.writerow(['total']) #пишем в него первым рядом строку "total"
    fw.writerow([str(total)]) #пишем вторым рядом цену за категорию "Закуски"

#2 задание
products = sorted(read_file()) #сортируем по алфавиту данные из файла
target_cat= (products[0])[0] #находим первую категорию
max_name = '' #название самого дорогого товара
max_price = 0 #его цена

for r in products: # перебирем товары

    if r[0] == target_cat: #сравниваем категорию с нужной нам
        price = float(r[3]) #цена
        name = r[1] #название
        
        if price > max_price: #если цена текущего товара больше максимальной что мы нашли, происходит следующее:
            max_price = price #меняем цену самого дорогого товара на текущий товар
            max_name = name #то же самое с именем
            
print(f'В категории: {target_cat} самый дорогой товар: {max_name} его цена за еденицу товара составляет {max_price}')
#^выводим ответ как полагается(как я егэ по русскому сдавать буду капец)        

#3
db = read_file() #данные из файла

cats=[] #все категории которые присутствуют в файле
for i in db:
    if i[0] not in cats:
        cats.append(i[0])
#отбор этих категорий^
print('Доступные категории: ') 
print('; '.join(cats)+'.') # какие категории есть
while True: #основной цикл
    target_cat = input('Введите искомую категорию: ') #ввод категории, которую хочет найти пользователь
    min_sold = 10000 #переменная, отвечающая за минимальное количество товара
    min_name = '' #его название
    if target_cat == 'молоко': #условие выхода из программы
        break
    if target_cat not in cats: #проверка на наличие искомой категории в базе данных
        print('Такой категории не существует в нашей БД')
    else:
        #основной функционал
        for r in db: #перебираем базу данных
            if r[0] == target_cat: #проверяем, подходит ли текущая категория под нужную нам
                name = r[1] #название текущего продукта
                bought = float(r[4]) #сколько раз его купили
                if bought < min_sold: #проверяем, меньше ли его раз купили чем наш минимум
                    min_name = name
                    min_sold = bought
                    #если да, то теперь этот продукт и есть наш минимум
        print(f'В категории: {target_cat} товар: {min_name} был куплен {int(min_sold)} раз') #вывод ответа

#4
#Промокод должен состоять из первых 2-ух
#букв названия + день поступления + 2 предпоследних буквы
#названия в обратном порядке + месяц поступления
#в обратном порядке.
def promocode_gen(name,date):

    #Эта функция призвана для генирации промокода
    #На вход ей нужно название и дата продукта
    #она форматирует переменные подобающим образом и возварщает готовый промокод
    
    fname = name[:2]
    day = date[:2]
    n1 = (name[:len(name)])[-2:]
    n1 = n1[::-1]
    month = (date.split('.')[1])[::-1]
    code = fname+day+n1+month
    return code.upper()

db = read_file() #открываем датабазу
codes = [] #список с кодами
for r in db: #преобразуем каждый продукт в промокод
    name = r[1]
    date = r[2]
    code = promocode_gen(name,date)
    codes.append(code)
db += codes #добавляем в датабазу промокоды

with open('product_promo.csv', mode='w') as pn:
    fw=csv.writer(pn,delimiter=';',lineterminator='\r') #открываем csv файл и читаем его
    fw.writerow(['promocode'])  #пишем первую строку "promocode"
    for i in db: #перебираем базу данных
        if type(i) is str: #если текущий объект - строка
            fw.writerow([i]) #пишем ее в файл, это наш промокод!
                    
