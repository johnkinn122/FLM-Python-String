#Exercises - Day 4
"""
1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.(skip)
3. Declare a variable named company and assign it to an initial value "Coding For All".(skip)
4. Print the variable company using print().(skip)
5. Print the length of the company string using len() method and print().(skip)
6. Change all the characters to uppercase letters using upper() method.(skip)
7. Change all the characters to lowercase letters using lower() method.(skip)
8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.(skip)
9. Cut(slice) out the first word of Coding For All string.
10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
11. Replace the word coding in the string 'Coding For All' to Python.(skip)
12. Change Python for Everyone to Python for All using the replace method or other methods.(skip)
13. Split the string 'Coding For All' using space as the separator (split()) .
14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
15. What is the character at index 0 in the string Coding For All.(skip)
16. What is the last index of the string Coding For All.(skip)
17. What character is at index 10 in "Coding For All" string.(skip)
18. Create an acronym or an abbreviation for the name 'Python For Everyone'.(skip)
19. Create an acronym or an abbreviation for the name 'Coding For All'.(skip)
20. Use index to determine the position of the first occurrence of C in Coding For All.
21.Use index to determine the position of the first occurrence of F in Coding For All.(skip)
22. Use rfind to determine the position of the last occurrence of l in Coding For All People.(skip)
23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'(skip)
27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'(skip)
28. Does ''Coding For All' start with a substring Coding?
29. Does 'Coding For All' end with a substring coding?(skip)
30. ' Coding For All ', remove the left and right trailing spaces in the given string.
31. Which one of the following variables return True when we use the method isidentifier():
--> 30DaysOfPython
--> thirty_days_of_python
32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
33. Use the new line escape sequence to separate the following sentences.(skip)
--> I am enjoying this challenge.
--> I just wonder what is next.
34. Use a tab escape sequence to write the following lines.(skip)
  Name      Age     Country   City
  Asabeneh  250     Finland   Helsinki
35. Use the string formatting method to display the following:
  radius = 10
  area = 3.14 * radius ** 2
  The area of a circle with radius 10 is 314 meters square.(skip)
36. Make the following using string formatting methods:
  8 + 6 = 14
  8 - 6 = 2
  8 * 6 = 48
  8 / 6 = 1.33
  8 % 6 = 2
  8 // 6 = 1
  8 ** 6 = 262144
"""
#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
word_1 = 'Thirty'
word_2 = 'Days'
word_3 = 'Of' 
word_4 = 'Python'
print(f"{word_1} {word_2} {word_3} {word_4}")

#9. Cut(slice) out the first word of Coding For All string.
sentence = "Coding For All string."
word_to_remove = "Coding"
new_sentence = sentence.replace(word_to_remove, "")
print(new_sentence)

#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
text = "Coding For All string"
checking ="Coding" in text
print(checking)

#13. Split the string 'Coding For All' using space as the separator (split()) .
sentence_to_be_splited = 'Coding For All'
split_words = sentence_to_be_splited.split()
print(split_words)

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies_split_by_comma = companies.split(",") # but if you try w/out commma it is the same result
print(companies_split_by_comma)

#20. Use index to determine the position of the first occurrence of C in Coding For All.
text = "Coding For All"
result =text.index("C")
print(result)

#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text_one =  'You cannot end a sentence with because because because is a conjunction'
word_because = "because"
word_position = text_one.find(word_because)
print(word_position)

#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
word_rindex = text_one.rindex(word_because)
print(word_rindex)

#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
phrase = "because because because"

start = sentence.find(phrase)
end = start + len(phrase)

result = sentence[start:end]
print(result)

#28. Does ''Coding For All' start with a substring Coding?
text = "Coding For All"
substring = "Coding"

result = text.startswith(substring)
print(result)

#30. ' Coding For All ', remove the left and right trailing spaces in the given string.
text = "  Coding For All  "
cleaned_text = text.strip()
print(cleaned_text)

#31. Which one of the following variables return True when we use the method isidentifier():
#--> 30DaysOfPython
#--> thirty_days_of_python

print("30DaysOfPython".isidentifier())  
print("thirty_days_of_python".isidentifier()) 

#32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash(#) with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = " # ".join(libraries)
print(joined_libraries)

#36. Make the following using string formatting methods:
""" 
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""

a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")  # 2 decimal places
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")

