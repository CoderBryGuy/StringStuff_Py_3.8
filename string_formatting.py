# name = "friggy"
#
# age = 21
#
# print("hi {} and age is {}".format(name, age))
#
# info = "hi I am " + name + " i work in a button factor"
# sliced = info[8:13:]
# print(name + " sliced still spells " + sliced)
#
# var = "hello"
# print(var[::-1])

runningInputLoop = True
runningOuterLoop = True

# random letter not y/n
again = "x"

while runningOuterLoop:

    while runningInputLoop:
        email = input("enter email: ")

        for letter in email:
            if letter == "@":
                runningInputLoop = False

    print(email[:email.index("@"):])

    while (again.lower() != "y") or (again.lower() != "n"):
        again = input("run again? y/n :")
        if again == "n":
            runningOuterLoop = False
        elif again == "y":
            runningInputLoop = True
            break


