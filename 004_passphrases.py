import csv

correct_pps = 0
with open('004_input_test.txt') as infile:
    reader = csv.reader(infile, delimiter=' ')
    for line in reader:

        correct = True
        for i, word1 in enumerate(line[:-1]):
            if not correct:
                break

            for word2 in line[i+1:]:
                if not correct:
                    break

                if word1 == word2:
                    correct = False

        if correct:
            correct_pps = correct_pps + 1

print(correct_pps)
