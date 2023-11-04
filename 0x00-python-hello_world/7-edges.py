#!/usr/bin/python3
word = "Holberton"
word_first_3 = slice(word[:3])
word_last_2 = slice(word[7:])
middle_word = slice(word[1:8]) 
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
