#Вариант 20
#Функция
def km_per_day(km,days):
   if days == 0:
    return "На ноль делить нельзя"
   return km/days
#Проверка
print(km_per_day(140,7))
#Сортировка
words = ["путь","маршрут","путешествие"]
#проверка
print(sorted(words,key=lambda word:len(word)))
