###FUNCTION##
#Positional Argument
#Arbitrary Argument
#Keyword only Argument
#End of position Argument
# def myFun1(a,b,*c,d,e=10):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(e)
# myFun1("baba","haha",'sasa',5,d="keywordarg")
#_________________________________________________
##Doc strings
# def myFun (x,y):
#     'This is my function'
#     """This function return x*y"""
#     return x*y
# myFun(2,3)
# help(myFun)
# print(myFun.__doc__)
#_________________________________________________
##Doc string,Annotation
#doc -> body of function
#annotation -> parameter and return of function
# x=10
# y=22
# def myFun(a:'somevalue_from_call_function',b:'somevalue_from_call_function')->'return_value_of_return_a_multiply_by_b_(x+Y)':
#     """This is the body of myFunction"""
#     return (a*b)*(x+y)
# Data=myFun(2,2)
# print(Data)
# print(myFun.__annotations__)
# print(myFun.__doc__)
#_____________________________________________________________________________________________________________________________________
##Anonymus Function or Lambda Function
#lambda arguments : expression
# objj=lambda x,y: x*y
# print(objj(2,3))
# x=lambda x,y,*args,z,**kwargs:(x,y,args,z,kwargs)
# print(x('a','b','ab','ba',z='holy_cow',aa='hello',bb='world'))
#__________________________________________________________________
##Higher Oreder function
# def myFun(fn,x,y):
#     return fn(x,y)
# def multiply(x,y):
#     return x*y
# print(myFun(multiply,3,5))
# def myFun(fn,x,y):
#     return fn(x,y)
# print(myFun(lambda a,b:a*b,3,5))
#________________________________________________________________
##Function Introspection and Inspectomonitor
# import inspect
# from inspect import isfunction,ismethod
# def myFun(fn,x,y):
#     """Body of function"""
#     return fn(x,y)
# myFun.__name2__="Function name 2"
# print(myFun.__annotations__)
# print(myFun.__doc__)
# print(myFun.__dir__)
# print(dir(myFun))
# print(myFun.__name2__)
# print(myFun.__name__)
# print(myFun.__defaults__)
# print(myFun.__kwdefaults__)
# print(myFun.__code__.co_varnames)
# print(myFun.__code__.co_argcount)
# print(inspect.getsource(myFun))
# print(inspect.getcomments(myFun))
# print(inspect.getmodule(print))
# print(isfunction(myFun))
# print(ismethod(myFun))
#________________________________________________________
##Callable
from typing import Any


class myClass:
    def __init__(self,x=0):
        print("myClass method")
        self.counter=x
        
    def __call__(self,x=11):
        print("Callmethod")
        self.counter+=x
        
    def myMethod(self,z=1):
        print("myMethod")
        self.counter+=z
        
ObjInit=myClass()
ObjCall=myClass()
objMethod=myClass()

myClass.__init__(ObjInit,20)
myClass.__call__(ObjCall,10)
myClass.myMethod(objMethod,30)
ObjCall()
print(ObjCall.counter)
print(callable(myClass.myMethod))
ObjCall()
print(objMethod.counter)
objMethod()
print(objMethod.counter)
