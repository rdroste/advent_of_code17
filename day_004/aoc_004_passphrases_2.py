
from collections import Counter

correct_pps = 0
with open('004_input.txt','r') as f:
    for line in f:
        words = line.strip().split()

        correct = True
        for i, word1 in enumerate(words[:-1]):
            if not correct:
                break

            for word2 in words[i+1:]:
                if not correct:
                    break

                if Counter(word1) == Counter(word2):
                    correct = False

        correct_pps += int(correct)

print(correct_pps)
