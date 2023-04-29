
string1=input("Enter the string :")#Enter the string
y=string1.lower()
#convert the string into lower so as to check for the duplicates
unique_character = []
#creating a list to store the unique characters in the string
for i in y:
    if i not in unique_character: 
        unique_character.append(i)
        #checking for the unique characgers in the string and appendong that to the list unique_character
print("unique characters in string are :", unique_character)
# printing the unique characters in the string 
