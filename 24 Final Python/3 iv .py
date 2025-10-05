charge=500
while True:
    route = input("Enter the Route (Up or Down ): ")
    starting_point = int(input("Enter the starting point number (1 to 5): "))
    ending_point = int(input("Enter the ending point number (1 to 5): "))
    user_input=input("Enter 'START' to calculate the bill: ")

    if (user_input == "START"):
        if(route == "Up"):
            stops = ending_point - starting_point
        else:
            stops = starting_point - ending_point
        Bill= stops * charge

    user_input=input("Bill Calculated Successfully, Enter 'END' to print the Bill: ")

    if (user_input == 'END'):
        print('Your Bill is ',Bill)

