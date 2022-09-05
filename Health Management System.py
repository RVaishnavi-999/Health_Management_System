"""
Instructions:
* Take 3 clients - Harry, Rohan and Hammad
* Create a food log file for each client
* Create an exercise log file for each client.
* Ask the user whether they want to log or retrieve client data.
* Write a function that takes the user input of the client's name.
* After the client's name is entered, it will display a message as
    "What you want to log- Diet or Exercise".
* Use function
def getdate():
           import datetime
           return datetime.datetime.now()

* The purpose of this function is to give time with every record of food
    or exercise added in the file.
* Write a function to retrieve exercise or food file records for any client.

"""
import datetime


def gettime():
    return datetime.datetime.now()


def take(user):
    if user == 1:
        log = int(input("Enter 1 for exercise and 2 for food :\n"))
        if log == 1:
            content = input("Type here\n")
            with open("harry-ex.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + content + "\n")
            print("Successfully written")
        elif log == 2:
            content = input("Type here\n")
            with open("harry-food.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + content + "\n")
            print("Successfully written")

    elif user == 2:
        log = int(input("Enter 1 for exercise and 2 for food :\n"))
        if log == 1:
            content = input("Type here\n")
            with open("rohan-ex.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + content + "\n")
            print("Successfully written")
        elif log == 2:
            content = input("Type here\n")
            with open("rohan-food.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + content + "\n")
            print("Successfully written")

    elif user == 3:
        log = int(input("Enter 1 for exercise and 2 for food :\n"))
        if log == 1:
            content = input("Type here\n")
            with open("hammad-ex.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + content + "\n")
            print("Successfully written")
        elif log == 2:
            content = input("Type here\n")
            with open("hammad-food.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + content + "\n")
            print("Successfully written")

    else:
        print("Please enter valid input : 1(harry),2(rohan),3(hammad)")


def retrieve(user):
    if user == 1:
        read_data = int(input("Enter 1 for exercise and 2 for food"))
        if read_data == 1:
            with open("harry-ex.txt") as f:
                for i in f:
                    print(i, end="")
        elif read_data == 2:
            with open("harry-food.txt") as f:
                for i in f:
                    print(i, end="")

    elif user == 2:
        read_data = int(input("Enter 1 for exercise and 2 for food"))
        if read_data == 1:
            with open("rohan-ex.txt") as f:
                for i in f:
                    print(i, end="")
        elif read_data == 2:
            with open("rohan-food.txt") as f:
                for i in f:
                    print(i, end="")

    elif user == 3:
        read_data = int(input("Enter 1 for exercise and 2 for food"))
        if read_data == 1:
            with open("hammad-ex.txt") as f:
                for i in f:
                    print(i, end="")
        elif read_data == 2:
            with open("hammad-food.txt") as f:
                for i in f:
                    print(i, end="")
    else:
        print("Please enter valid input (harry,rohan,hammad)")


print("------------- Health Management System ---------------")
take_input = int(input("Press 1 for Log the value and 2 for Retrieve :\n"))

if take_input == 1:
    b = int(input("Press 1 for 'Harry' 2 for 'Rohan' 3 for 'Hammad' :\n"))
    take(b)
elif take_input == 2:
    b = int(input("Press 1 for 'Harry' 2 for 'Rohan' 3 for 'Hammad' :\n"))
    retrieve(b)
else:
    print("Wrong choice")
