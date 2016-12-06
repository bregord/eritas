import csv
import time
import re

#whitespace = re.compile(r"\n")
#empty
empty = re.compile(r"\s\n")
pagebreak = re.compile(r"\s+\[pagebreak\]")
#result = prog.match(string)

para = re.compile(r"\n$")
empty = re.compile(r"\n")
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

    #only get things that are bounded by headers, and remove the [pagebreak] and \n



    temp = []

    cur_termin = 0

    for line in csvfile:
        count = count + 1
        print ("COUNT IS" + str(count) )

        line_term_cnt = line.count("|")

        cur_termin += line_term_cnt

        temp.append(line)

        if cur_termin is 6:

            full_art = " ".join(temp)

            full_art = re.sub(empty, "", full_art) + "\n"

            print (full_art)

            array.append(re.sub(pagebreak, "", full_art))

            cur_termin = 0
            temp = []
            #append all lines in temp, and remove \n and [pagebreak]

print("WRITING ARRAY")
#print (array)

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
