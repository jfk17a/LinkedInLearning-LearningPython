

def main():
    total = 0
    test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.", "Race car!"]

    for word in test_words:
        total += is_palindrome(word)
    
    print(total)

def is_palindrome(teststr):
    holder = ""
    for letter in teststr:
        if letter.isalpha():
            holder += letter

    if holder[::1].upper() == holder[::-1].upper():
        return True
    else:
        return False


if __name__ == "__main__":
    main()