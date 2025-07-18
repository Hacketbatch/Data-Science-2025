# -*- coding: utf-8 -*-
"""bismark_midterm

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w1G7sgQFiwDrayzr_snAHnhj43dP4eH9
"""

#11.GRADE CONVERTER
#Asks for user input
user_input = input("Enter your results:")
grade = int(user_input)
#Prints corresponding letter grade
if grade >= 90:
    print(f"{user_input} A")
elif grade >= 80:
    print(f"{user_input} B")
elif grade >= 70:
    print(f"{user_input} C")
elif grade >= 60:
    print(f"{user_input} D")
else:
    print(f"{user_input} F")

#12.VOWEL COUNTER
#Asks the user to enter a sentence
sentence = input("Write a sentence:")

def count_vowels(sentence):
    #Makes the programm case insensitive
    vowels = "aeiouAEIOU"
    count = 0
    # The following lines were not indented correctly
    for ch in sentence:
        if ch in vowels:
            count += 1
    return count

#Gives a total count of the vowels.
print (count_vowels(sentence))

#13.DECIMAL TO BINARY CONVERTER
n = input("Enter a decimal number:")
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary
print(decimal_to_binary(int(float(n))))

#14.SUM OF DIGITS.
#Ask 4 user input
userinput = input("Enter a number: ")
def sumofdig(number):
 total_sum = 0
#Ensures that if a negative number is entered its absolute value is used
 number = abs(number)
#Converts the input number into a string
 num_str = str(number)
#For loop iterates through each character
 for digit in num_str:
   total_sum += int(digit)
 return total_sum
try:
  number = int(userinput)
  result = sumofdig(number)
  print(f"The sum of the digits of {number} is: {result}")
except ValueError:
  print("Invalid input. Please enter an integer.")

