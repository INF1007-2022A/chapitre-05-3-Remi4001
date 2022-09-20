#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_num_letters(text):
    num = 0
    for i in text:
        if i.isalnum():
            num += 1

    return num


def get_word_length_histogram(text: str):
    histogramme = [0]

    words = text.split()

    # Trouver le plus grand nombre de lettres
    max_num_letters = get_num_letters(max(words, key=get_num_letters))

    histogramme += [0] * max_num_letters

    for word in words:
        histogramme[get_num_letters(word)] += 1

    return histogramme


def format_histogram(histogram):
    ROW_CHAR = "*"
    width = len(histogram) // 10 + 1
    histo_form = ""

    for i, num in enumerate(histogram[1:]):
        i += 1
        histo_form = "\n".join([histo_form, f"{i:>{width}} {ROW_CHAR * num}"])

    return histo_form


def format_horizontal_histogram(histogram):
    BLOCK_CHAR = "|"
    LINE_CHAR = "¯"
    histo_form = ""

    for i in range(max(histogram), 0, -1):
        histo_form += "".join([BLOCK_CHAR if num >=
                              i else " " for num in histogram[1:]]) + "\n"

    # Ajouter la ligne en bas
    histo_form += LINE_CHAR * len(histogram)
    return histo_form


if __name__ == "__main__":
    spam = "Stop right there criminal scum! shouted the guard confidently."
    eggs = get_word_length_histogram(spam)
    print(eggs, "\n")
    print(format_histogram(eggs), "\n")
    print(format_horizontal_histogram(eggs))
