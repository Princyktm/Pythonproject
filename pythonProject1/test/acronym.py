'''it is simple project in nlp to understand the acronym generation
'''
input_string = str(input("Enter a Phrase: "))
splittext = input_string.split()
acronym = " "
for text in splittext:
    acronym= acronym+str(text[0]).upper()
print(acronym)