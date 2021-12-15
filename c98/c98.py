def countWords():
    fileName = input("enter the file name")
    noOfWords = 0 
    file = open(fileName,'r')
    for line in file:
        words = line.split()
        noOfWords = noOfWords + len(words)
    print("number Of Words")
    print(noOfWords)

countWords()