# def hello(name = 'Trace'):
#     print('THIS HELLO() FUNCTION HAS BEEN RUN')
#     def greeting():
#         return "THIS IS IN GREETING() FUNCTION"
#     def welcome():
#         return "THIS IS IN WELCOME() FUNCTION"
#     # print(greeting())
#     # print(welcome())
#     # print("This is the end of Hello()")

#     if name == 'Trace':
#         return greeting
#     else: return welcome

# # welcome()
# x= hello()
# print(x())

def new_decorator(func):
    def wrap_func():
        print( "THIS IS BEFORE EXCUTING FUNC")
        func()
        print('AFTER EXCUTING FUNC')
    return wrap_func
    # wrap_func()

@new_decorator
def func_need_decorate():
    print('THIS FUNCTION NEED DECORATE')

# f = func_need_decorate()

# f = new_decorate(func_need_decorate)
func_need_decorate()
# f()



