#Вариант 20
def km_per_day(km,days):
   if days == 0:
      return "На ноль делить нельзя"
   return km/days

assert km_per_day(210,7) == 30
assert km_per_day(210,0) == "На ноль делить нельзя"
assert km_per_day(140,20) == 7

words = ["путь","маршрут","путешествие"]
print(sorted(words,key=lambda word:len(word)))
