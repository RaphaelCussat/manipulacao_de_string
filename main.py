# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import logging

#Exercício 01
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(words[::-1])
    return reversed_sentence
#Exercício 02

def remove_duplicates(string):
    unique_chars = ""
    for char in string:
        if char not in unique_chars:
            unique_chars += char
    return unique_chars.lower()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(reverse_sentence('Ola PWC, eu me chamo Raphael'))
    print(remove_duplicates('Banana'))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

