from collections import Counter
import re
import time
from os import system

system("title " + ".txt file analyser")
FirstTime = True

def FileMenu():
    print("\033[H\033[J", end="")
    Words = text.split()
    WordCount = Counter(Words)

    x = "[()],"
    y = "    :"
    TranslateTable = str.maketrans(x, y)

    LongestWord = max(Words, key=len)
    SmallestWord = min(Words, key=len)

    Sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()] 
    # magic i came up with at 30 past midnight. Removes special chars and shit.
    SentenceCount = len(Sentences) - 1

    CharCountNS = sum(len(word) for word in Words)
    CharCount = len(text)
    print("====== Sentences =======")
    print(f"Number of sentences: {SentenceCount}")
    print(f"Longest sentence:    {max(Sentences, key=len)}")
    print(f"Shortest sentence:   {min(Sentences, key=len)}\n")
    print("======== Words =========")
    print(f"Number of words:  {len(Words)}")
    print(f"Longest word:     {LongestWord}")
    print(f"Shortest word:    {SmallestWord}\n")
    print("====== Characters ======")
    print(f"Character count (no spaces): {CharCountNS}")
    print(f"Character count:             {CharCount}\n")
    print("======== Other =========")
    print("The 5 most common words:")
    print(str(WordCount.most_common(5)).replace("), (", "\n  ").translate(TranslateTable))
    # i spent too much time here for what i should have...
    print("\n========================")
    print("Press enter to choose another file")
    input()


def MainMenu(): # amazing menu
    global text, FirstTime
    while True:
        print("\033[H\033[J", end="")
        if FirstTime == True:
            print("Welcome to the Xameren's text file analyser")
        FirstTime = False
        print("Please enter your file name (for example, \"xameren\", not \"xameren.txt\")")
        filechosen = input()
        try:
            with open(f'{filechosen}.txt', 'r') as file:
                text = file.read()
            FileMenu()
        except Exception as e:
            print("Please enter a valid file")
            print("error: ", e )
            print("\nIf it shows a \"file missing\" error, but file exists, please restart the app")
            time.sleep(5)

MainMenu()