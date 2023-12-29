def get_time_stamp(): #Creating Function to get the curent time
    getcurrenttime = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") #getting time and storing that in a variable
    return getcurrenttime # Returning the time

def write_to_file(ts): # creating function to write the name of the text file
    timestampfile = open(ts + ".txt", "w")
    timestampfile.close()
    with open(ts + ".txt", "a", newline='') as file_write:
        writer = csv.writer(file_write)
        writer.writerow([ts])


#Question number 2:
def read_from_file(filename): #Creating a function to read the input of the file
    with open(filename + ".txt", 'r') as file_read:
        filecontent = file_read.readlines()
    return filecontent


#Program to call all the functions and get the desired output
import datetime
import csv
time_stamp = get_time_stamp()
write_to_file(time_stamp)
print("Enter the file name to be read:")
file_to_read = input()
content_from_file = read_from_file(file_to_read)
for content in content_from_file:
    print(content.rstrip("\n"))
