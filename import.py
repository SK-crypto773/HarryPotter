import sys
import sqlite3
import csv


def main():

    # Error handling
    if (len(sys.argv) != 2):
        sys.exit("Usage: import.py characters.csv")

    filename = sys.argv[1]

    if not (filename.endswith(".csv")):
        sys.exit("You must provide a *.csv")

    # Connect with the .db file and make a cursor
    sqlite_file = "students.db"
    con = sqlite3.connect(sqlite_file)

    cur = con.cursor()

    # Open the csv file to import from
    with open(filename, "r") as characters:

        # Make a dictionary reader that iterates through rows
        reader = csv.DictReader(characters)

        for row in reader:
            names = []

            # Appending information
            for part in row["name"].split(" "):
                names.append(part)

            names.append(row["house"])
            names.append(row["birth"])

            # If the student has a middle name
            if (len(names) == 5):
                cur.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", names[:5])

            # If the student doesn't have a middle name
            if (len(names) == 4):
                cur.execute("INSERT INTO students (first, last, house, birth) VALUES(?, ?, ?, ?)", names[:4])

    con.commit()
    con.close()


main()