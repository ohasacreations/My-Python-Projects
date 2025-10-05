current_number=1
user_number=int(input("Enter a number"))
while(current_number<=user_number):
    if(current_number%3==0 and current_number%5==0):
        print("FizzBuzz")
    elif(current_number%5==0):
        print("Buzz")
    elif(current_number%3==0):
        print("Fizz")
    else:
        print(current_number)
    current_number=current_number+1