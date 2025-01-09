import requests
import pprint
import numpy as np
import pandas as pd

#Библиотека requests


answer = requests.get('https://httpbin.org/')


#pprint.pprint(answer.headers) #Выводит в консоль заголовки полученного от сервера ответа
#pprint.pprint(answer.request.headers) # Выводит в консоль заголовки отправленного на сервер запроса

#for key, value in answer.headers.items():
    #print(f"{key}: {value}") #Выводит в консоль заголовки (ключ-значение) полученного от сервера ответа


#Метод Post
data2 = {'My name': 'Vasiliy'}
answer2 = requests.post('https://httpbin.org/post', data=data2)
#print(answer2.text) #Отправленные нами данные будут под ключом form


#Проверка подключения
#if answer.ok:
    #print("Подключение налажено, господин")
#else:
    #print("Я упал, подключения нет")

#Работа со сторонним api
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#pprint.pprint(response_json := response.json()) #Обращение к api которое сообщает курс биткоина в разных валютах
#print(response_json['disclaimer']) #Запрос отдельного значения из полученного json-ответа. В данном случае - пояснения

#Скачивание файла по адресу:
url = 'https://avatars.mds.yandex.net/i?id=03306bad8018eebce05ca89570b0e7c5457b1a23-9813974-images-thumbs&n=13'
response2 = requests.get(url)
#with open ('this_is_fine.png','wb') as picture:
    #picture.write(response2.content)




#Библиотека Numpy

#Создание готовых массивов
arr = np.zeros(6,dtype=int) #Массив из нулей
#print(arr)
arr2 = np.ones(6, dtype = int) #Массив из единиц
#print(arr2)
arr3 = np.full((2,7),4) #Матрица из семи четверок
#print(arr3)

#Создание массива из числового диапазона:
arr4 = np.arange(14)
#print(arr4)

#Преобразование массива:
arr5 = np.reshape(arr4,(2,7))
#print(arr5)

#Объединение матриц по осям
#Объединение матриц по оси 0
arr6 = np.concatenate((arr, arr2), axis=0)
#print(arr6)

#Объединение матриц по оси 2
arr7 = np.concatenate((arr3, arr5), axis=1)
#print(arr7)


#Pandas
#для выполнения задания мне потребуются дополнительные файлы:
#CSV1 и CSV2 - оба будут загружены на Github
distance_from_Moscow = pd.read_csv('Расстояние от Москвы.csv', sep=';',encoding='utf-8')
distance_from_SPB = pd.read_csv('Расстояние от Питера.csv', sep=';',encoding='utf-8')

#Проводим анализ какие города ближе к Москве, чем к Санкт-Петербургу
#Если в результате True - значит ближе к Москве, если False - ближе к СПб
#pprint.pprint(distance_from_SPB > distance_from_Moscow)

