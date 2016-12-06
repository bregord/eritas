import csv
import time
import re

#whitespace = re.compile(r"\n")
#empty
empty = re.compile(r"\s\n")
pagebreak = re.compile(r"\s+\[pagebreak\]")
#result = prog.match(string)

para = re.compile(r"\n$")

beg = re.compile(r"^\n")

has_break = re.compile(r"^.+\n")
has_end = re.compile(r"^.+\|\n")



FILENAME = "cleaned_" + str(time.time()) + ".csv"
with open(FILENAME, 'w', encoding='utf-8') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_NONE, delimiter=",")
    wr.writerow(["|title|", "|subheader|", "|article|"])



pageapp = False

with open('corpus3.csv', 'r', encoding='utf-8') as csvfile:
    array = []

    count = 0
    for line in csvfile:
        count = count + 1
        print ("COUNT IS" + str(count) )

        #NEW MLG LEET STRAT. find first section. call that head. find second
        if empty.match(line):# or para.match(line):
            #print ("FOUND LINE")
            #print (line)
            continue

        elif pagebreak.match(line):
            pageapp = True

            #print ("broke")

        elif has_break.match(line) and not has_end.match(line):

            array.append(line)
            pageapp = True

        elif pageapp:

            #print (has_break.match(array[-1]))
            #array[-1] = re.sub("\n","\\n", array[-1]) +" " + line
            array[-1] = array[-1].replace("\n","") + line
            #print (array[-1])
            #print (array[-1])
            pageapp = False

        else:
            array.append(line)
        #concat


print("WRITING ARRAY")
print (array)

with open(FILENAME, 'a', encoding='utf-8') as f:
    #wr = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar="|",dialect='excel', delimiter=",")
    #wr.writerows(to_write)
    for el in array:
        #f.write("|"+el[0]+"|,|"+el[1]+"|,|"+el[2]+"|\n")
        f.write(el)




        #print (array)


def concat_pg_brk(lines):

    return



    #NEED: WAY TO STRIP

    #if a line has a page break and whitespace, remove the whitespace and stuff

    #remove all with no ARTICLE


    #spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #for row in spamreader:
    #    print ', '.join(row)
