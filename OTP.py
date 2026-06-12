## pletter= Per input string, apply transformation based on char
def shiftLetter(letter, amount):
    assert isinstance(letter, str)
    assert len(letter) == 1

    if letter.isupper():
        base = ord('A')
        return chr((ord(letter) - base + amount) % 26 + base)

    elif letter.islower():
        base = ord('a')
        return chr((ord(letter) - base + amount) % 26 + base)

    else:
        return letter


def getShift(letter):
    assert isinstance(letter, str)
    assert len(letter) == 1
    if letter.isupper():
        return ord(letter) - ord('A')
    elif letter.islower():
        return ord(letter) - ord('a')
    else:
        raise ValueError("Fucked up key my slime")


def processKey(key, subject):
    ## wraparound logic to ensure key is length of word
    return (key * (len(subject) // len(key) + 1))[:len(subject)]


## YOU ONLY NEED TO CARE ABOUT THE CODE INBETWEEN THESE LINES
def Encryption(word, key): ##THIS IS WHERE YOU WANT TO PUT YOUR CODE!!!
    index = 0
    result = []

    for letter in word:
        shift = getShift(key[index])
        ## now you want to do use the shiftLetter function passing in (letter, shift) and
        ## stick it in a list. Ask AI if u dont understand.
        result.append(shiftLetter(letter, shift))
        index += 1

    return "".join(result)
    ## YOU ONLY NEED TO CARE ABOUT THE CODE INBETWEEN THESE LINES


## Main
word = input("Please input a word to encrypt")
key = processKey(input("Please input a key to encrypt by"), word)
print(Encryption(word, key))
assert len(Encryption(word, key)) == len(word) ##if these error ur logic is wrong
assert Encryption("AAAAA", "B") == "BBBBB"
assert Encryption("abc", "B") == "bcd"