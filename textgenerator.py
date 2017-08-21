from histogram import Dictogram
import random
from collections import deque
import re
import textprocessor
import markov
import sys

def generate_random_start(model):
    return random.choice(list(model.keys()))

def generate_random_sentence(length, markov_model):
    current_word = generate_random_start(markov_model)
    sentence = [current_word]

    for i in range(0, length):

        current_dictogram = markov_model[current_word]
        random_weighted_word = current_dictogram.return_weighted_random_word()
        current_word = random_weighted_word
        sentence.append(current_word)

    sentence[0] = sentence[0].capitalize()

    return " ".join(sentence) + "."

def main():
   
    length = 10

    if len(sys.argv) > 1:
        length = int(sys.argv[1])

    dataset = textprocessor.process_text("dataset.txt")
    model = markov.make_markov_model(dataset)
    print(generate_random_sentence(length, model))
  
if __name__ == "__main__":
    main()

