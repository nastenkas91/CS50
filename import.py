# TODO
import sys
import csv
from cs50 import SQL
db = SQL("sqlite:///students.db")

if len(sys.argv) != 2:
    print("Wrong command-line!")
    sys.exit(1)
#print(sys.argv)
with open(sys.argv[1]) as csvfile:
    charact_list = csv.DictReader(csvfile)
    for row in charact_list:
        #string = row.split(",")
        names = row["name"].split(" ")
        house = row['house']
        birth = row['birth']
        #print(names)
        #for partname in name.split(" "):
         #   print(partname, partname[0], partname[1])
        if len(names) == 2:
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, null, ?, ?, ?)", names[0], names[1], house, birth)
        if len(names) == 3:
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", names[0], names[1], names[2], house, birth)
print("end")