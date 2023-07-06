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

#Exercicio 03
def find_longest_palindroma(name):
    result = ''
    for i in range(len(name)):
        for j in range(len(name)):
            if j <= i:
                continue
            aux = name[i:j + 1]
            if aux == aux[::-1]:
                if len(aux) > len(result):
                    result = aux
    return result

#Exercicio 04
def capitalize_sentences(name):
    delimiters = ['? ', '. ', '! ', ': ', '; ']
    def capitalize(string, delimiter):
        sentences = string.split(delimiter)
        capitalized_sentences = [sentence[0].upper() + sentence[1:] for sentence in sentences]
        capitalized_string = delimiter.join(capitalized_sentences)
        return capitalized_string

    for delimiter in delimiters:
        name = capitalize(name, delimiter)
    return name

#Exercício 05
def is_polindroma(name):
    if name == name[::-1]:
        return True
    else:
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(reverse_sentence('Ola PWC, eu me chamo Raphael'))
    print(remove_duplicates('Banana'))
    print(find_longest_palindroma('babdbabd'))
    print(capitalize_sentences('olá. como você está? tudo bem? eu estou bem! obrigado.'))
    print(is_polindroma('racecar'))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

