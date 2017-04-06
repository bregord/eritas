import csv


with open('onion_corpus.csv', 'r', encoding='utf-8') as csvfile:
    array = []

    for line in csvfile:
        #grab between first
        start_index = line.find("|")
        end_index = line[start_index+1:].find("|")

        array.append(line[start_index+1:end_index+1])




with open("onion_headlines.csv", 'w', encoding='utf-8') as f:
    for el in array:
        #f.write("|"+el[0]+"|,|"+el[1]+"|,|"+el[2]+"|\n")
        f.write(el + ",1\n")
