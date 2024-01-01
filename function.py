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



