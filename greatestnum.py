#code to check the greatest of the three numbers


#taking inputs from the user
number_1= input("Enter 1st Number: ")
number_2= input("Enter 2nd Number: ")
number_3= input("Enter 3rd Number: ")

if number_1>number_2 and number_1>number_3:     #Checking whether number 1 is greatest
    print("The greatest number is", number_1)

elif number_2>number_1 and number_2>number_3:   #Checking whether number 2 is greatest
    print("The greatest number is", number_2)

else: print("The greatest number is", number_3) #Checking whether number 3 is greatest