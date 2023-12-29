def get_time_stamp():
    getcurrenttime = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    return getcurrenttime

def write_to_file(ts):
    timestampfile = open(ts + ".txt", "w")
    timestampfile.close()
    with open(ts + ".txt", "a", newline='') as file_write:
        writer = csv.writer(file_write)
        writer.writerow([ts])

def read_from_file(filename):
    with open(filename + ".txt", 'r') as file_read:
        filecontent = file_read.readlines()
    return filecontent

import datetime
import csv
time_stamp = get_time_stamp()
write_to_file(time_stamp)
print("Enter the file name to be read:")
file_to_read = input()
content_from_file = read_from_file(file_to_read)
for content in content_from_file:
    print(content.rstrip("\n"))
