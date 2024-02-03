def outer(func):
    def inner(a,b):
        print('I got decorated')
        if(b==0):
            print('Cannot divide')
            return
        return func(a,b)
    return inner

@outer
def divide(a,b):
    print(a/b)

divide(2,6)
print()
divide(2,0)
