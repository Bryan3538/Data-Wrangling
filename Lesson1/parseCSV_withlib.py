import os
import pprint
import csv

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_csv(datafile):
    data = []
    with open(datafile, "r") as sd:
    	data = []
    	r = csv.DictReader(sd)
   
    	for line in r:
    		data.append(line)

    return data


if __name__ == '__main__':
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_csv(datafile)
    pprint.pprint(d)

# def test():
#     # a simple test of your implemetation
#     datafile = os.path.join(DATADIR, DATAFILE)
#     d = parse_file(datafile)
#     firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
#     tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

#     #DEBUG 
#     print(firstline)
#     print(d[0])
#     #DEBUG
#     #assert d[0] == firstline
#     #assert d[9] == tenthline
#     #print("success!")

    
# test()