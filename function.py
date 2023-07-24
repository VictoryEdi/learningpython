def my_function():
    print("Hello from a function")

def my_function():
    print("Hello from a function")

my_function()

def my_function(fname):
    print(fname + " Refsnes")

my_function("edikan")
my_function("Tobias")
my_function("Linus")




def my_function(*kids):
    print("The youngest child is" + kids[2])

my_function("emil", "Tobias", "Linus")


def my_function(country   =  "Nigeria"):
    print("I am from" +   country)

my_function("Japan")
my_function("USA")
my_function()



def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "beans"]
my_function(fruits)


def my_function(x):
    return 5 * x
print(my_function(9))
print(my_function(7))
print(my_function(8))


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k -1)
        print(result)
    else:
        result = 0
        return result


def fib2(n):
    """Return a list containing the fibonacci series up to 2000."""
    result = []
    a , b = 21, 1000
    while a < n:
        result.append(a)
        a , b = a+b




def my_function():
    print("Hello come let me teach you python")

my_function()







        
