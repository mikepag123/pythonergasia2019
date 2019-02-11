textfile1 = raw_input('Dwste arxeio txt gia anagnwsh: ')

def get_words():
    with open(textfile1, "r") as f:
        for word in f.readline().split(" "):
            yield word.replace(",", "").replace(".", "")

with open("output.txt", "w") as f:
    it = get_words()
    current = [""] + [next(it) for _ in range(2)]
    for word in it:
        current = current[1:] + [word]
        f.write(" ".join(current) + "\n")

import random
count = 0
for line in open('output.txt').readlines(  ):
    count += 1
    lines = open('output.txt').read().splitlines()
    myline =random.choice(lines)
    with open('output2.txt', 'a') as f:
        f.write(myline + " ")
