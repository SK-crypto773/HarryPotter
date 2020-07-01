import sys
import sqlite3
import csv

def main():

    # Error handling
    if (len(sys.argv) != 2):
        sys.exit("Usage:roster.py house_name")

    # Change the house inputted to lowercase
    h = sys.argv[1].lower()

    # Valid houses
    houses = ["gryffindor", "hufflepuff", "ravenclaw", "slytherin"]

    if h not in houses:
        print("The House you entered was incorrect. Please choose from Gryffindor, Hufflepuff, Ravenclaw or Slytherin")
        exit(1)

    # Connect with the .db file and make a cursor
    sqlite_file = "students.db"
    con = sqlite3.connect(sqlite_file)

    cur = con.cursor()

    # Order the students alphabetically per house
    cur.execute('SELECT first, middle, last, birth FROM students WHERE lower(house) = "{}" ORDER BY last, first;'.format(h))

    # Fetchall gives us all the rows of the table as a list of tuples with strings.
    houseroster = cur.fetchall()

    # Printing the students
    for row in houseroster:

        # If the student doesn't have a middle name
        if not row[1]:
            print("{} {} , born {}".format(row[0], row[2], row[3]))

        # If the student has a middle name
        else:
            print("{} {} {} , born {}".format(row[0], row[1], row[2], row[3]))

    con.close()


main()