# (C) L.W. Cornelis van Lit 2017. The Digital Orientalist.
# Dependencies
import codecs

# Importing Psalter
psalterNumberAndText = list()
with codecs.open("psalterreduced.txt", encoding="utf-8", mode="r") as ps:
    psalter = ps.readlines()
    for verse in psalter:
        verseNumberAndText = verse.strip().split(";")
        psalterNumberAndText.append(verseNumberAndText)

# Importing Word List
with codecs.open("latinvocab.txt", encoding="utf-8", mode="r") as wl:
    wordList = wl.read().splitlines()
    wordSet = set(wordList)

#-----------------------------------------------------------------------------------------------------------------------

## Length of psalm verse
def lengthOfVerse(psNumber):
    print("{0} is the length of Psalm {1}, which reads {2}".format(len(psalterNumberAndText[psNumber][1]), psalterNumberAndText[psNumber][0], psalterNumberAndText[psNumber][1]))

#Example:
#lengthOfVerse(23)
#-----------------------------------------------------------------------------------------------------------------------

#Simple check if verse consists of known words
def simpleVerseMadeOfKnownWords(psNumber):
    verseToList = psalterNumberAndText[psNumber][1].split()
    verseToSet = set(verseToList)
    if verseToSet < wordSet:
        print("Yes, {0} is made up of known words.".format(psalterNumberAndText[psNumber][0]))
    else:
        print("No, {0} does not.".format(psalterNumberAndText[psNumber][0]))
# Example:
#simpleVerseMadeOfKnownWords(1998)

#-----------------------------------------------------------------------------------------------------------------------

#More advanced check, with certain number of unknown words allowed and with variations of spelling.

#Return all unknown words
def unknownWordsInVerse(psNumber):
    verseToList = psalterNumberAndText[psNumber][1].split()
    unknownWords = list()
    for word in verseToList:
        if word not in wordList:
            unknownWords.append(word)
    return(unknownWords)


#Return all verses that have an allowable number of unknown words
def allowedNumberUnknownWords(allowedNumber, numberOrText):
    if numberOrText == "number":
        total = 0
        for verse in range(0, len(psalterNumberAndText)):
            if len(unknownWordsInVerse(verse)) <= allowedNumber:
                print(psalterNumberAndText[verse][0])
                total = total + 1
        print("Number of verses: {0}".format(total))

    elif numberOrText == "text":
        total = 0
        for verse in range(0, len(psalterNumberAndText)):
            if len(unknownWordsInVerse(verse)) <= allowedNumber:
                print("{0} has {1} unknown words, namely: {2}".format(psalterNumberAndText[verse][1], len(unknownWordsInVerse(verse)), unknownWordsInVerse(verse)))
                total = total + 1
        print("Number of verses: {0}".format(total))
    elif numberOrText == "both":
        total = 0
        for verse in range(0, len(psalterNumberAndText)):
            if len(unknownWordsInVerse(verse)) <= allowedNumber:
                print("\n{0} \nHas {1} unknown words, namely: {2}".format(psalterNumberAndText[verse], len(unknownWordsInVerse(verse)), unknownWordsInVerse(verse)))
                total = total + 1
        print("\n \n   Number of verses: {0}".format(total))
    else:
        print("Error, argument requires \'number\', \'text\', or \'both\'!")



# Example
allowedNumberUnknownWords(1,"both")

#-----------------------------------------------------------------------------------------------------------------------