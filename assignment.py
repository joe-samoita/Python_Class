
#  Checking if a number is a vowel or consonant


def findalpha():
    let = input("Enter the Alphabet: ")

    if let == "a" or let == "e" or let == "1" or let == "o" or let == "u":
        print("The alphabet is a vowel")

    else:
        print("The Alphabet is a consonant")

x = 1

while x <= 27 :

    x += 1
    #  findalpha()
    #  print("you have", 27 - x, "chances left")


#  Checking if the year is a leap year or not

def checkLeap():
    year = input("Enter the year: ")

    if int(year) % 4 == 0 or int(year) % 400 == 0:
        print("This is a leap year")

    else:
        print("This is not a leap year")

y = 1
while y <= 5:
    y += 1
    checkLeap()

