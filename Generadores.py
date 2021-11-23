# def my_gen():
#     #Un ejemplo de generadores
    
#     print('Hello World!')
#     n = 0
#     yield n
    
#     print('Hello heaven!')
#     n = 1
#     yield n
    
#     print('Hello  hell!')
#     n = 2
#     yield n
    
# a = my_gen()

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# De esta manera podemos realizar azucar sintactica a los iteradores

# Generator expression
my_list = [0,1,4,7,9,10]

my_second_list = [x*2 for x in my_list] #List comprehension
my_second_gen = (x*2 for x in my_list) # Generator Expression

