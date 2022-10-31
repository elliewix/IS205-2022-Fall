import csv

infile = open('horse csv example.csv', 'r', encoding='utf-8')
csvin = csv.reader(infile)
headers = next(csvin) #reads just the first line and waits
print(headers)
data = []
for row in csvin: # now iterate over the rest, saving them to data
    data.append(row)
# print(data)

# to see it better....
# for row in data:
#     print(row[:2])
# get a smaller amount of the columns
horses_ltd = []
headers_ltd = headers[:2]
for row in data:
    ltd = row[:2]
    horses_ltd.append(ltd)
print(horses_ltd)
print(headers_ltd)

# to write out the file

outfile = open('horses_limited.csv', 'w', encoding='utf-8', newline = '')
csvout = csv.writer(outfile)
# write out one line
csvout.writerow(headers_ltd) #1d list
# write out many lines...
csvout.writerows(horses_ltd) #2d list of data

# nested loops....

for row in data:
    for cell in row:
        print(cell)
