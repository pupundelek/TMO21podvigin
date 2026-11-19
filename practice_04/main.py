#Вариант 20
#задание 1
x = 30
def show():
    x = 20
    print(x)

show()
print(x)

#Вывод программы
#20
#30 
#внутри функии внутренняя переменная x со значением 20, x которая вне фунцкии это глобальная переменная, при изменение внутренней x глобальная не поменяется

#2 задание
def total(*args):
    return sum(args)

print(total(20,21,22))
#3 задание
def person(**kwargs):
    name = kwargs.get("name", "Гость")
    age = kwargs.get("age", 0)
    return name, age
print(person(name = "Алла", age = 21))

#задание 4
def increase(x):
    return x + 5

def apply(func,value):
    return func(value)

print(apply(increase,5))
#задание 5
def countown(n):
    if n == 0:
        return
    print(n)
    countown(n - 1)

countown(5)