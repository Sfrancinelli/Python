#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

f = open("Udemy/24-day/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r")
txt = f.readlines()

names = open("Udemy/24-day/Mail Merge Project Start/Input/Names/invited_names.txt", "r")
name_list = names.readlines()

print(name_list)

letter1_name = f"{txt[0].replace('[name],', name_list[0])} {txt[1]} {txt[2]} {txt[3]} {txt[4]} {txt[5]} {txt[6]}"

letter1 = open("Udemy/24-day/Mail Merge Project Start/Output/ReadyToSend/letter_aang.txt", "w")

letter1.write(letter1_name)

count = 0

for i in name_list:
    j = i.replace("\n", "")

    letter_name = f"{txt[0].replace('[name],', name_list[count])} {txt[1]} {txt[2]} {txt[3]} {txt[4]} {txt[5]} {txt[6]}"


    letter = open(f"Udemy/24-day/Mail Merge Project Start/Output/ReadyToSend/letter_{j}.txt", "w")

    letter.write(letter_name)

    count += 1