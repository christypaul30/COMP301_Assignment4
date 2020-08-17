"""
Program: generator.py
Generates and displays sentences using simple grammar
and vocabulary. Words are chosen at random.
"""

import random

#Implement getWords method
def getWords(filename):
    readFile = open(filename, "r")
    temporary_List = list()
    for line in readFile:
        line = line.strip()
        temporary_List.append(line)
    
    #List converted to Tuple
    allwords = tuple(temporary_List)
    readFile.close()
    return allwords

#Get text files from getWords method
articles = getWords('articles.txt')
nouns = getWords('nouns.txt')
verbs = getWords('verbs.txt')
prepositions = getWords('prepositions.txt')

articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL",)
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")
adjectives = ("FIT" "CALM" "ANGRY")
conjunctions = ("OR" "YET" "SO")

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

#After iterating loop, display statement and call main
if __name__ == "__main__":     
    main()