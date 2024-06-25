import glob
def main():
    options = glob.glob("books/*")
    selection = selectText(options)
    with open(options[selection]) as f:
        file_contents = f.read()

        # Manipulation
        createReport(options[selection], file_contents, getTotal=True, getChar=True, getWord=True)

def selectText(options):
    selection = None

    input_message = "Pick an option:\n"

    for index, option in enumerate(options):
        input_message += f'{index + 1}) {option}\n'

    input_message += "Your choice (select a number): "

    while selection is None:
        _selection = int(input(input_message)) - 1

        if options[_selection] in options:
            selection = _selection

    print("You picked: " + options[int(selection)])

    return selection

def getTotalWordCount(fc):
    return len(fc.split())

def getCharCount(fc, alphabetOnly = False):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    characters = {}
    for char in fc.lower():
        if alphabetOnly:
            if char in alphabet:
                if char in characters.keys():
                    characters[char] = characters[char] + 1
                else:
                    characters[char] = 1
        else:
            if char in characters.keys():
                characters[char] = characters[char] + 1
            else:
                characters[char] = 1
    return characters

def getWordUsage(fc):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    words = {}
    for word in fc.lower().split():
        if word in words.keys():
            words[word] = words[word] + 1
        else:
            words[word] = 1
    return words

def createReport(fn, fc, getTotal = False, getChar = False, getWord = False):
    text = fn.replace("books/", "").replace(".txt", "")
    f = open(f'{text}-report.txt', "a")
    values = {
        "total": getTotalWordCount(fc) if getTotal else None,
        "charCount": getCharCount(fc, alphabetOnly=True) if getChar else None,
        "wordCount": getWordUsage(fc) if getWord else None
    }

    f.write("######################\n")
    f.write("Text Semantic Analysis\n")
    f.write("######################\n\n")
    if values["total"] != None:
        f.write("Total Word Count of Book - " + str(values["total"]) + "\n\n\n")
    
    f.write("Single Character Count\n")
    f.write("######################\n\n")
    if values["charCount"] != None:
        for k, v in values["charCount"].items():
            f.write('"' + k + '"' + " is written " + str(v) + " times.\n\n\n")
    
    f.write("Word Appearance Count\n")
    f.write("######################\n\n")
    if values["wordCount"] != None:
        for k, v in values["wordCount"].items():
            f.write('"' + k + '"' + " is written " + str(v) + " times.\n")

    print("Report Created Successfully.")
main()