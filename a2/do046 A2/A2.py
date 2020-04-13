#packages
from kanren import Relation, fact, run, var, facts #package for logic programming
import docx2txt #package for turning .docx to .txt

#function for counting how many times a word was used
def word_count(str):
    counts = dict() #counts is a dictionary variable
    words = str.split() #parses the words into a string

    #counts the number of repeated words
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts #returns dictionary to be used outside of function

#function to convert .docx to .txt file
def convert_doc_to_text(str):
    MY_TEXT = docx2txt.process(str) #function call to process .docx file

    fileName = str.split('.')[0] #obtains file name

    #creates a .txt file with the file name
    with open(fileName + '.txt', "w") as text_file: 
        print(MY_TEXT, file=text_file) #prints the information into the text file
        
#declared variables
synonym = Relation() #create a relation variable to identify synonym words
no_synonym = Relation() #create a variable to identify if no synonyms are stored in the word bank
x = var() #holds the value of run()
y = var() #holds the value of run()

# Threshold levels (small, medium, high)
s_threshold = 10
m_threshold = 18
h_threshold = 25

#opens the .txt file in order to obtain the synonym words
with open('synonyms.txt') as file:
    synlist = [line.strip().split(',') for line in file
                                       if line and line[0].isalpha()]

#for loop function creates the word to synonym word relation
for L in synlist:
    head, tail = L[0], L[1:]

    #head is the main word
    #tail are the synonym words
    for state in tail:
        fact(synonym, head, state)

#holds the value when no synonyms are found
empty = (run(1, x, no_synonym("", x)))

#a prompt for the user to understand what this program is, and how to use it
print("######################################################################")
print("Hello, this program will help elevate the writer's paper by providing")
print("different word suggestions. Before proceeding any further,")
print("please import wanted .docx files into this directory first")
print("######################################################################\n")

#the user inputs what file he/she wants to check for improvement
user_input = input("Please input doc name: ")

#function call to create a .docx file to a .txt file
convert_doc_to_text(user_input)

#put the text file into a string
user_input = user_input.split('.')[0] # extracts the file name before '.'
with open(user_input + ".txt") as f: # open the txt file with the file name 
    data = f.read() #.read() puts creates a string out of the txt file

#word_count function returns the number of times each word is used
count = word_count(data)

#creates a file called, "UPDATE_SYNONYM.txt" to hold words that are not found
#in the word bank of synonyms
suggestionfile = open("UPDATE_SYNONYM.txt", "a")

#creates a report with the words the paper used alot along with it's count
reportfile = open(user_input + "_report.txt", "a")
reportfile.write("Words                Times Used")
reportfile.write("\n####################################\n")

#checks how many times the words are used and applies the adequate
#amount of syonyms for the word based on threshold
#the threshold is divided into small, medium, and high
for word in count:
    #checks if the count is greater than small threshold

    if count[word] > s_threshold:
        print("\"", word, "\"", " was used,", count[word], "times.")
        reportfile.write(word + "......................" + str(count[word]) + "\n")

        #checks if the count is less than medium threshold
        if(count[word] < m_threshold):
            suggested_num = 3

        #checks if the count is greater than medium but less than high threshold
        elif(count[word] > m_threshold and count[word] < h_threshold):
            suggested_num = 4

        #checks if the word is greater than high threshold
        elif(count[word] >= h_threshold):
            suggested_num = 5

        #holds the value on how many synonomists words should be suggested
        suggestion = (run(suggested_num, x, synonym(word, x)))
        if(suggestion == empty):
            print("Suggestion is NULL. Updated,", "\"", word, "\" into needed synonym word bank\n")            
            suggestionfile.write(word + ", ")
        else:
            print("Try using other words such as: ", suggestion, "\n")
            
#close files
suggestionfile.close()
reportfile.close()

#notifies the user that a file was created
print(user_input + "_report.txt was created")
