# Searching the Psalter with psalter-search!

This repository contains useful resources for those interested to do automated searches on the Psalms of the Bible.

### psalterreduced.txt
This text file contains all the psalms in Latin only, according to a regular pattern: every line contains a line of the psalter, 
every line opens with the psalm **chapter** number, a colon, the psalm **verse** number, a semi-colon, immediately followed (no space)
by the verse. The verse itself is fully in lower case without any punctuation. Ligatures like æ have been simplified to two characters, ae.

For example:
```
4:1;in finem in carminibus psalmus david
```

### latinvocab.txt
This text contains a list of Latin words (a new word on each line) that are likely known to Churchgoers. These words are from 
the propers of Mass and some other well-known parts of Mass such as Eucharistic Prayer II. Additionally, the list contains 
cognates that appear in the Psalter.

It is likely that you may wish to tailor this list to your own needs.

### psaltersearch.py
This script loads the Psalter and the word list and has several functions.
1. It has a function to read the number of characters a line in the Psalter has.
2. It has a true/false check if a Psalm-verse consists entirely of words from the word list.
3. It has a function to return all words of a Psalm-verse not contained in the word list.
4. And finally it has a function that will give back all Psalm-verses that are made up of words from the word list, with *x* amount of 
allowed words in the verse that do not occur in the list. This function has three modes: to return the numbers of verses that match the 
criteria, to return the texts of verses that meet the criteria, or to return both.


### psalter.txt
For those wishing to sink their teeth in automated searches on the Psalms of the Bible using their own scripts, this file may be a useful starting point. It contains the full Psalter in both Latin and English. It has not been reduced yet, meaning that the chapter/verse numbers are in between curly brackets with spaces around them and the text has capitals, punctuation and characters like æ. You can reduce this file to a regular form for your own needs using regular expressions and a Find/Replace function in e.g. Sublime Text or Visual Studio Code.

### Future development
I am not planning right now to develop this further, but obviously a lot more can be done. Feel free to pick up where I left it!
