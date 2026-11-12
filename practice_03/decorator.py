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