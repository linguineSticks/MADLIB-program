####################################
# Kelsey Wanket
# MADLIB.py
# 10/03/2020
#####################################

"""Create 3 different mad lib stories with
blank spaces for  several words. Take user
input and replace the blank words in order
to create a new madlib."""


def madLib1():
    madlib1 = "I am going for a ride on my BLANK and then I will go to my grandma's house and BLANK the BLANK in the kitchen."
    list1 = madlib1.split(" ")

    # ask the user for words with corresponding parts of speech
    noun1a = input("Enter a noun: ")
    Presentverb = input("Enter a present tense verb: ")
    noun1b = input("Enter another noun: ")

    # replace the blanks with user input
    list1[8] = noun1a
    list1[-6]= Presentverb
    list1[-4] = noun1b

    #recreate string
    newLib1 = " ".join(list1)

    #show result
    print(newLib1)


def madLib2():
    madlib2 = "Sheila and her BLANK were driving to the BLANK in their BLANK pickup truck, when they saw a BLANK with a BLANK walk across the street."
    list2 = madlib2.split(" ")

    # ask the user for words with corresponding parts of speech
    noun2a = input("Enter a noun: ")
    noun2b = input("Enter a noun: ")
    adj2a = input("Enter an adjective: ")
    noun2c = input("Enter another noun: ")
    noun2d = input("Enter another noun: ")

    # replace the blanks with user input
    list2[3] = noun2a
    list2[8] = noun2b
    list2[11] = adj2a
    list2[18] = noun2c
    list2[21] = noun2d

    # recreate string
    newLib2 = " ".join(list2)

    # show result
    print(newLib2)


def madLib3():
    madlib3 = "The cutest BLANK BLANK in the world is fighting a BLANK and winning."
    list3 = madlib3.split(" ")

    # ask the user for words with corresponding parts of speech
    adj3a = input("Enter an adjective: ")
    noun3a = input("Enter a noun: ")
    noun3b = input("Enter another noun: ")

    # replace the blanks with user input
    list3[2] = adj3a
    list3[3] = noun3a
    list3[-3] = noun3b

    # recreate string
    newLib3 = " ".join(list3)

    # show result
    print(newLib3)


def main():
   # print("Welcome to MADLIBS")
   # print("By Linguine Stix")
   while (True):

        ask = input("Which MADLIB do you want to do? 1, 2, or 3?")
        ask = int(ask)
        if ask == 1:
           madLib1()
        elif ask == 2:
           madLib2()
        elif ask == 3:
           madLib3()
        y = input("Enter to continue or x to quit: ")
        if y == "x":
            break

main()
