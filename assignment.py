def findalpha():
    let = input("Enter the Alphabet: ")

    if let == "a" or let == "e" or let == "1" or let == "o" or let == "u":
        print("The alphabet is a vowel")

    else:
        print("The Alphabet is a consonant")

x = 1

while x <= 27 :

    x += 1
    findalpha()
    print("you have", 27 - x, "chances left")