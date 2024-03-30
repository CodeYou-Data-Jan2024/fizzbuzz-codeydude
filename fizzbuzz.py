# def fizzbuzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "Fizzbuzz"
#     elif number % 3 == 0:
#         return "Fizz"
#     elif number % 5 == 0:
#         return "Buzz"
#     else:
#         return number
    
# for i in range(1,101):
#     print(fizzbuzz(i))

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


    
