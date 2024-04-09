from HashTable import *
import csv

def create_studentDatabase(studentRecords):
    size = 7
    hashtable = create_hashtable(size)
    for record in studentRecords:
        hashtable, size = put(hashtable, record['ID'], record, size) # place those values to their respective keys
    return hashtable
    

def perform_Operations(H, operationFile):
    keys, values = H
    with open(operationFile, 'r') as file:
        lines = file.readlines()
    collision_path = {}
    for op_number, line in enumerate(lines): # enumerate to keep track of operation number
        line = line.strip().split(' ')
        if line[0] == 'Find':
            if len(line) == 2:
                print(get(H, line[1], len(keys), collision_path, op_number+1))
            else:
                print(get(H, line[1], len(keys), collision_path, op_number+1)[line[2]])
        elif line[0] == 'Update':
            Update(H, line[1], line[2], line[3], len(keys), collision_path, op_number+1)
        elif line[0] == 'Delete':
            H, size = delete(H, line[1], len(keys), collision_path, op_number+1)
    
    return collision_path

            

def main(filename):
    records = [] # list of dictionaries for hashtable
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headings = next(reader) # read the first line to get headings
        # print(headings)
        for line in reader: # read the rest of the lines
            dictionary = {}
            for i in range(len(headings)):
                dictionary[headings[i]] = line[i]
            records.append(dictionary)
    return records

    

studentRecords=main('data.csv')
# print(studentRecords)
H=create_studentDatabase(studentRecords)
# print(H)
print(perform_Operations(H, 'Operations.txt'))
