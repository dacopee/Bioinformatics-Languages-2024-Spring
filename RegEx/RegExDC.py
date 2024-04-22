#yeast gene RegEx sequence searcher for ORF Genes
#Assignment - Design a Python script that retrieves all ORFs from YeastGenes directory that contain matches to an input consensus sequence.

import re
import os

output_directory = "C:\\RIT Classes\\BIO 230 Bioinformatic Lang\\GUI Pipeline"
foldername = 'YeastGenes'

def main():
    usrInput = input("Enter your input sequence: ") #asks for seq to search for
    usrInput = usrInput.upper()
    print("You Entered: ", usrInput)

    occurrences = [] #initialize response structure


    for filename in os.listdir(foldername):
        file_path = os.path.join(foldername, filename)
        with open(file_path, 'r') as file: #reads file
            next(file) #Skip first line
            content = file.read() #read rest of file

            for match in re.finditer(re.escape(usrInput), content):
                matchPos = match.start()
                gene = filename[0:7]
                occurrences.append((gene, matchPos))


    print("Number of occurrences found:", len(occurrences))
    for filename, matchPos in occurrences:
        print(f"Found in '{filename}' at position {matchPos}")

if __name__ == '__main__':
    main()
    print("\nRegExDC Complete")
    exit