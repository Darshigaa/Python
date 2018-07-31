#Get sentence from user

original = input("Please enter a sentence: ").lower().strip()

#Split sentence into words

words =  original.split()

#Loop through the words
new_words = []
#If it starts with a vowel, add "yay" otherwise, move the first consonant to the end and add ay

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiouu":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
        
#Stick words back together

output = " ".join(new_words)

#Output the final string

print(output)
