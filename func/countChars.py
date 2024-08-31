# Count chars in text
def countChars(text):
    lowerText = text.lower()
    charsDictionary = {}
    for char in lowerText:
        if char in charsDictionary:
            charsDictionary[char] += 1
        else:
            charsDictionary[char] = 1
    return charsDictionary