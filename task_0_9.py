def string_to_vowel(word):
    vowels = []
    for letter in word.lower():
        if letter in ("aeiou"):
            if letter not in vowels:
                vowels.append(letter)

    print("Vowels: " + ", ".join(vowels))


string_to_vowel("Thandiwe Khalaki")