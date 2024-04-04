#this code is to prepare a csv file so that r can read and analyze
#path to folder "C:\\RIT Classes\\BIO 230 Bioinformatic Lang\\RCode\\YeastGenes"

import csv
import os
import datetime

current_time = datetime.datetime.now().time()

def main():
    output_directory = "C:\\RIT Classes\\BIO 230 Bioinformatic Lang\\RCode"
    foldername = 'YeastGenes'

    groups = grouper(foldername)
    gc_counts = {}

    for group_name, files in groups.items(): # Process each file in the group
        for filename in files:
            file_path = os.path.join(foldername, filename)
            with open(file_path, 'r') as file: #
                next(file) #Skip first line
                content = file.read() # Read rest of file
                gc_pct = gcContent(content) # Calculate GC content

                if group_name not in gc_counts:
                    gc_counts[group_name] = []
                gc_counts[group_name].append(gc_pct)

        csv_file = os.path.join(output_directory, 'gc_results.csv') #create the csv file & open it
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file) #Create a CSV writer object

            writer.writerow(gc_counts.keys()) #Write the column headers
            num_rows = max(len(gc_counts[column]) for column in gc_counts.keys()) #Determine the maximum number of rows

            for i in range(num_rows):
                row = []
                for column in gc_counts.keys():
                    values = gc_counts.get(column, [])
                    if i < len(values):
                        row.append(values[i])
                    else:
                        row.append(None)  # Append None if index exceeds the length of the list
                writer.writerow(row)


def grouper(dir):
    if not os.path.isdir(dir):
        return None  #Return None if directory does not exist

    groups = {}
    for filename in os.listdir(dir):
        second_letter = filename[1] #Get chromosome in second letter of the filename

        if second_letter not in groups: #Check if a group already exists
            groups[second_letter] = [] #Create a new group

        groups[second_letter].append(filename) #Add file to the corresponding group
    return groups

#get gc content function to repeat use
def gcContent(seq):
    count = 0
    tot = 0
    final = 0
    for i in seq:
        if((i == "C") or (i == "G")):
            count = count + 1
        if((i == "A") or (i == "T")):
            tot = tot + 1
    tot = tot + count
    if(tot !=0):
        final = (count/tot) * 100
    return final

if __name__ == "__main__":
    main()
    print ("\nended RCodePython.py at:", current_time) #end script with time
    exit