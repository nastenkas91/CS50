# TODO
import sys
import csv
from cs50 import SQL
db = SQL("sqlite:///students.db")

if len(sys.argv) != 2:
    print("Wrong command-line!")
    sys.exit(1)

rows = db.execute("SELECT first, middle, last, birth from students where house = ? order by last asc, first asc", sys.argv[1])
for row in rows:
    if row["middle"] != None:
        print(row["first"], " ", row["middle"], " ", row["last"], ", ", "born", " ", row["birth"], sep = "")
    else:
        print(row["first"], " ", row["last"], ", ", "born", " ", row["birth"], sep = "")

