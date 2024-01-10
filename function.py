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
# from typing import Any
# class myClass:
#     def __init__(self,x=0):
#         print("myClass method")
#         self.counter=x
        
#     def __call__(self,x=11):
#         print("Callmethod")
#         self.counter+=x
        
#     def myMethod(self,z=1):
#         print("myMethod")
#         self.counter+=z
        
# ObjInit=myClass()
# ObjCall=myClass()
# objMethod=myClass()
# myClass.__init__(ObjInit,20)
# myClass.__call__(ObjCall,10)
# myClass.myMethod(objMethod,30)
# ObjCall()
# print(ObjCall.counter)
# print(callable(myClass.myMethod))
# ObjCall()
# print(objMethod.counter)
# objMethod()
# print(objMethod.counter)
#_______________________________________________
##Iterable,Map,Generator,Zip
# lis=[2,4,6,8,0,12,14,16,18]
# iterator=iter(lis)
# print(iterator)
# for i in iterator:
#     print(i)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#_________________________________
##Map
# def fact(n):
#     return 1 if n<2 else n*fact(n-1)
# maplis=map(fact,range(6))
# for i in maplis:
#     print(i)
# print(next(maplis))
# print(next(maplis))

# lis1=[10,20,30,40,50,60]
# lis2=[1,2,3,4,5,6]
# maplis=map(lambda x,y:x+y,lis1,lis2)
# print(next(maplis))
# print(next(maplis))
# print(next(maplis))
# print(next(maplis))
# print(next(maplis))
#_________________________________
##
# def Gen():
#     data=1
#     while data<10:
#         square=data*data
#         yield square
#         data+=1
        
# Genlis=Gen()
# for i in Genlis:
#     print(i)
#___________________________________
##Zip and Filter
# lis1=[10,1,20,2,30,3,40]
# lis2=[11,11,22,22,33,33,44]
# zipout=zip(lis1,lis2)
# for i in zipout:
#     print(i) 

# lis1=["a","b","c","d","e","f","g","h","i","j"]
# def myFun(lis1):
#     lis2=["a","e","i"]
#     for i in lis1:
#         if i in lis2:
#             return False
#         else: return True
# filout=filter(myFun,lis1)
# filout
# for i in filout:
#     print(i)    
# for x in filout:
#     print(x)
#___________________________________________________________
##Reduce function
# from functools import reduce
# lis1=[1,8,9,2,3,4,5,6,7]
# result=reduce(lambda x,y: x if x>y else y,lis1)
# result=reduce(lambda x,y: x+y,lis1)
# print(result)
#___________________________________________________________
##PartialFunction
# def myFun(x,y,z):
#     print(x,y,z)
# def Pfn(yy,zz):
#     return myFun(yy,zz,10)
# result=Pfn(100,200)
# result

# from functools import partial
# def myFun(x,y):
#     print(x,y)
# def myFun2(fn,x,y):
#     return fn(x,y)
# result=partial(myFun2,myFun,10,20)
# result()
#__________________________________________________
##Scope
# x=10
# def myFun1():
#     global x
#     x=111
#     print(x)
# myFun1()
# print(x)

# x=10
# def outterFun():
#     global x
#     y=10
#     def innerFun():
#         nonlocal y
#         y+=10
#         return print(y)
#     innerFun()
#     print(y)
# print(x)
# outterFun()
#_______________________________________________________
##Closure
# def Outterfun(n):
#     def Innerfun(data):
#         add=data+n
#         return add
#     return Innerfun
# result=Outterfun(10)
# print(result(result(10)))
# print(result.__closure__[0].cell_contents)
##_______________________________________________
#@property
# def Outerfun1(fn):
#     print("Outer Output")
#     def Innerfun1(x,y):
#         result=x+y
#         print("Result of Inner output is {}".format(result))
#         return fn(x,y)
#     return Innerfun1
# def Outerfun2(fn):
#     print("Outer Output")
#     def Innerfun2(x,y):
#         result=x-y
#         print("Result of Inner output is {}".format(result))
#         return fn(x,y)
#     return Innerfun2
# x=2
# y=3
# @Outerfun1
# @Outerfun2
# def Fun(x,y):
#     print("final out result is {} and {}".format(x,y))
    
# result1=Outerfun1(Fun)
# result2=Outerfun2(Fun)
# result1(2,1)
# result2(2,1)
# result3=Outerfun2(Outerfun1(Fun))
# result3(2,4)
#______________________________________________________________
##@wraps
# from functools import wraps
# def outerFun(fn):
#     @wraps(fn)
#     def innerFun():
#         """Inner Fun Doc"""
#         return fn()
#     return innerFun
# @outerFun
# def fnName():
#     """fnName result"""
#     print("Hahaha")

# print(fnName.__doc__)
##_________________________________________________________________
# def logger(fn):
#     from functools import wraps
#     from datetime import datetime,timezone
#     @wraps(fn)
#     def inner(*args,**kwargs):
#         dt=datetime.now(timezone.utc)
#         result=fn(*args,**kwargs)
#         print('Calling This {} function is at {} '.format(fn.__name__,dt))
#         return result 
#     return inner
# def outer(fn):
#     from functools import wraps
#     from time import perf_counter
#     @wraps(fn)
#     def inner1(*args,**kwargs):
#         start=perf_counter()
#         result=fn(*args,**kwargs)
#         end=perf_counter()
#         runningtime=end-start
#         print('Running time of {} is {:.6f} long'.format(fn.__name__,runningtime))
#         return result
#     return inner1
# @logger
# @outer    
# def myFun2(x):
#     print ('this is my fun 2')       
# myFun2(10)        
# def memories(fn):
#     cahes={1:1,2:1}
#     def inner(n):
#         if n not in cahes:
#             cahes[n]=fn(n)
#         return cahes[n]
#     return inner 
# @memories    
# def fibo(n):
#     return 1 if n<2 else fibo(n-1)+fibo(n-2) 
# print(fibo(7))




