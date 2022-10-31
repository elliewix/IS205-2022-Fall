import csv

infile = open('horse csv example.csv', 'r', encoding='utf-8')
csvin = csv.reader(infile) # act only on csvin after this
# gets the first row
headers = next(csvin) # force it to iterate once
# now we need to get the rest
data = [] # our base
for row in csvin:
    data.append(row)

# print(data)
# for row in data: # loop to print it and make it more readable
#     print(row[1])

# you're likely to see something like this online....
# so don't google for stuff use my notes
# don't use this
with open('horse csv example.csv', 'r', encoding='utf-8') as infile:
    csvin = csv.reader(infile)
    # headers = next(csvin)
    # data = [r for r in csvin]
    headers, *data = csvin

# print(headers)

# writing out csv files

# our headers are in headers
# out data is in data
# maybe we do something to the data

horses_ltd = []
headers_ltd = headers[:2]
for row in data:
    horses_ltd.append(row[:2])

outfile = open('new_horses.csv', 'w', encoding= 'utf-8', newline = '')
csvout = csv.writer(outfile)
# to write out one row
csvout.writerow(headers_ltd)
# to write out many rows
csvout.writerows(horses_ltd)

