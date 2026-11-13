#Вариант20
g = (x + 1 for x in range(0,7))
print(list(g))



def announce(func):
    def wrapper():
        result = func()
        print("Сейчас вызов")
        return result
    return wrapper

@announce
def hello():
    print("Привет!")

hello()

