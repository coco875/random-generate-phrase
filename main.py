import json
import random

with open("themedb-en.json", "r", encoding="utf-8") as f:
    data = json.load(f)

all_words = {}
first_words = []

for i in (data if type(data) == dict else range(len(data))):
    if data[i].startswith("#"):
        continue
    l = data[i].split(" ")
    first_words.append(l[0])
    for j in range(len(l)-1):
        if l[j] not in all_words:
            all_words[l[j]] = []
        if l[j+1] != "":
            all_words[l[j]].append(l[j+1])

def generate_sentence():
    string = ""
    last_word = None
    while True:
        if last_word in all_words:
            word = random.choice(all_words[last_word])
            string += word + " "
            last_word = word
        elif last_word == None:
            last_word = random.choice(first_words)
            string = last_word + " "
        else:
            break
        if not last_word in all_words or all_words[last_word] == []:
            break
    return string

with open("sentences.txt", "w", encoding="utf-8") as f:
    for i in range(100):
        f.write(generate_sentence() + "\n")