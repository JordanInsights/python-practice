a = "test"
b = 0
def fun1():
    b = b + 1
    print(b) # No local b variable. Attempted manipulation throws errors

def fun2(val):
    def fun3():
        val = 3000 
        print(val)
    fun3()
    print(val) # can access values from parent scope, but can't maniplulate
    print(a) # example of accessing from parent scope 

def fun4():
    global b
    b = b + 1 # can manipulate global values by specifying
    print(b)

fun4()