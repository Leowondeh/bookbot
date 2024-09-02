# Key sorts
def sortOccurence(dict):
    return dict["count"]

# Convert a dict to a sorted list of dicts (by occurence)
def convertToSortedList(dictionary):
    convertedList = []
    for key, value in dictionary.items():
        convertedList.append({"char": key, "count": value})
    convertedList.sort(reverse=True, key=sortOccurence)
    return convertedList