# Count chars in text
def countChars(text):
    charsDictionary = {}
    for char in text.lower():
        if char in charsDictionary:
            charsDictionary[char] += 1
        else:
            charsDictionary[char] = 1
    return charsDictionary

# Count vowels and consonants
def countVowelsAndConsonants(text):
    validVowels = ['a', 'e', 'i', 'o', 'u']
    vowelCount = 0
    consonantCount = 0

    for char in text.lower():
        if char in validVowels:
            vowelCount += 1
        else:
            consonantCount += 1
    return vowelCount, consonantCount