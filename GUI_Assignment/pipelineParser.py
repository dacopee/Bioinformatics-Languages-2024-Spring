import csv
import os

output_directory = "C:\\RIT Classes\\BIO 230 Bioinformatic Lang\\GUI Pipeline"
foldername = 'YeastGenes'

def main():
    header = ['Gene', 'Chromosome', 'GC_Percentage', 'GC_Count']
    data = []

    for filename in os.listdir(foldername):
        file_path = os.path.join(foldername, filename)
        with open(file_path, 'r') as file: #reads file
            next(file) #Skip first line
            content = file.read() #read rest of file
            count, gc_pct, = gcContent(content) # Calculate GC content
            second_letter = filename[1]
            curr_data = [filename, second_letter, gc_pct, count] #count is the GC number
            data.append(curr_data)

    csv_file = os.path.join(output_directory, 'gc_results.csv') #create the csv file & open it
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file) #Create a CSV writer object
        writer.writerow(header)
        writer.writerows(data)

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
    return count, final

if __name__ == '__main__':
    main()
    print("Python Parser Finished")
    exit
