# Get text from a file
def getBook(path):
    with open(path) as f:
        contents = f.read()
        return contents

# Sort by occurence key for sort()
def sortOccurence(dict):
    return dict["count"]

# Count words in text
def countWords(text):
    splitText = text.split()
    return len(splitText)

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

# Convert a dict to a sorted list of dicts (by occurence)
def convertToSortedList(dictionary):
    convertedList = []
    for key, value in dictionary.items():
        convertedList.append({"char": key, "count": value})
    convertedList.sort(reverse=True, key=sortOccurence)
    return convertedList

# Generate Report
def generateReport(path):
    print(f"======== REPORT for {path} ========")
    print("")
    print(f"    * Word Count: {countWords(getBook(path))}")
    print("")
    print("    * Character counts:")

    for dict in convertToSortedList(countChars(getBook(path))):
        if dict['char'].isalpha():
            print(f"       > {dict['char']} was found {dict['count']} times")
    
    print("==================================================")
        
# Main (WIP)
def main():
    generateReport("examplepath")

main()