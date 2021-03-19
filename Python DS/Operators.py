# First class objects, using functions as arguments

def func1(name):
    return f"Hello {name}"

def func2(name):
    return f"{name}, how you doing?"

def func3(func4):
    return func4("Dear Learner")

print(func3(func1))
print(func3(func2))


# Inner functions or Nested function
def func():
    print("First function.")
    def func1():
        print("First child function")
    def func2():
        print("Second child function")
    
    func2()
    func1()        
    
func()


def func(n):
    def func1():
        return "Edureka"
    def func2():
        return "Python"
    if n == 1:
        return func1()
    else:
        return func2()
    
a = func(1)
b = func(3)

print (a)
print (b)

# Decorator functions

def header(name):
    def wrapper():
        print("Hello")
        name()
        print("Welcome to Python Course.")
    return wrapper
def returnName():
    print("User")

returnName = header(returnName) #wrapper text

returnName()

#Using Syntactic Sugar in Decorator

def header(name):
    def wrapper():
        print("Hello")
        name()
        print("Welcome to Python Course.")
    return wrapper
@header           #Syntactic Sugar
def returnName():
    print("User")

returnName()
 
   
# Using arguments in function
def header(name):
    def wrapper(*args, **kwargs):
        print("Hello")
        name(*args, **kwargs)
        print("Welcome to Python Course.")
    return wrapper
@header           #Syntactic Sugar
def returnName(name):
    print(f"{name}")

returnName("Google")
    

# Returning arguments

def header(name):
    def wrapper(*args, **kwargs):
        print("Hello")
    return wrapper
@header           #Syntactic Sugar
def returnName(name):
    print(f"{name}")

returnName("Google")




























