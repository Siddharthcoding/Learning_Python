def removeWords(wordList, word):
    newList = []
    for w in wordList:
        if w != word:
            newList.append(w.strip(word))   # strip removes leading and trailing characters
    return newList

l = ["harry", "rohan", "subham", "an"]

print(removeWords(l, "an"))