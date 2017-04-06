import csv



array = []

with open('reddit.csv', 'r') as f:
    reader = csv.reader(f)
    lines = list(reader)
    for el in lines:
        print(el[4])
        array.append(el[4])
        #print(el)
    #print (lines)
    #for row in reader:
    #    print(row)

with open("reddit_headlines.csv", 'w', encoding='utf-8') as f:
    for el in array:
        #f.write("|"+el[0]+"|,|"+el[1]+"|,|"+el[2]+"|\n")
        f.write(el + ",0\n")

