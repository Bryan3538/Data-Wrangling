"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

#starts on row 4 (3)
#example value: 1989-01-01T00:00:00+02:00
#substring 0,10
def process_file(input_file, output_good, output_bad):
    good_records = []
    bad_records = []

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        for row in reader:
            #if the URI is from dbpedia.org
            if row["URI"].startswith("http://dbpedia.org"):
                #if it's a year
                if row["productionStartYear"][:4].isdigit():
                    #convert year to JUST year
                    row["productionStartYear"] = row["productionStartYear"][0:4]
                    #check if year is in range
                    year = int(row["productionStartYear"])
                    if year >= 1886 and year <= 2014:
                        good_records.append(row)
                    else:
                        bad_records.append(row)
                else: #add NULL values and the like to bad records
                    bad_records.append(row)              
    #END READ

    #Write output files
    with open(output_good, "w") as g:
        good = csv.DictWriter(g, delimiter=",", fieldnames= header, lineterminator="\n")
        good.writeheader()
        for row in good_records:
            good.writerow(row)

    with open(output_bad, "w") as b:
        bad = csv.DictWriter(b, delimiter=",", fieldnames=header, lineterminator="\n")
        bad.writeheader()
        for row in bad_records:
            bad.writerow(row)


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()