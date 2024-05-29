#import pandas as pd
#import matplotlib.pyplot as plt
import time
import subprocess
import re
import os
import os.path
from os import path

def helpCMD(): #DOnt forget to add when making new commands
    print(f'Hello, {os.getlogin()}! Welcome to the help section of Dans Bioinformatic tool')
    print('Here is a list of available commands:\n')
    print('\tcodon finder: Searches for codons throughout a single chromosome or all chromosomes\n')
    print('\texit or e: Exits the program\n')
    print('\tgc percentage: Reports the GC Percentage of the sequences\n')
    print('\thello: Says hi!\n')
    print('\thelp: A general description of this program\n')
    print('\tparrot: Try it out!\n')
    print('\tthird codon: Finds and reports the nucleotide percentag in the third position in each codon\n')
    print('\ttranslator: Translates your genes into an Amino Acid Sequence\n')

def main():

    foldername = folderpath()
    while True:
        command = input("\nEnter a command or type help for more resources: ")
        if command == 'hello':
            print(f'Hello, World! and {os.getlogin()} of course!')
        elif (command =='exit' or command == 'e'):
            print('Exiting the program... Have a good day')
            break
        elif command == 'gc percentage':
            gc_calculator(foldername)
        elif command == 'help':
            helpCMD()
        elif command == 'parrot':
            cool_parrot()
        elif command == 'translator':
            final_translator(foldername)
        elif command == 'third codon':
            thirdCodon(foldername)
        elif command == 'codon finder':
            codon = input("\nPlease input a codon you are looking to search for:").upper()
            if (contains_invalid_characters(codon, valid_DNA_nucleotide) == False):
                codon_finder(foldername,codon)
            else:
                print("Error: Invalid Codon, please use only chars: A, T, C, or G")
        else:
            print('Unknown command. Please try again.')

def folderpath():
    folder_path = input("\nYeastGenes is the default folder, leave this box blank or\nenter the name of the folder containing genes in FASTA file format that you want to analyze: ") #Validate if the provided path is a directory
    if folder_path == "":
        folder_path = "./YeastGenes"
    else:
        folder_path = "./" + folder_path
    if not os.path.isdir(folder_path):
        print("Error: The provided path is not a valid folder.")
        exit(1)
    else:
        print(f"\nValid Folder! path: {folder_path}")
    return folder_path

def final_translator(foldername):
    real_seq = ""
    target_files, chrom, cORf = chrom_or_file(foldername)
    if cORf == True:
        for file in target_files:
            temp_seq = []
            file_path = os.path.join(foldername, file)
            with open(file_path, 'r') as file: #reads file
                fastacheck = file.read(1)
                if fastacheck == '>':
                    next(file) #Skip first line
                    content = file.read() #read rest of file
                else:
                    content = file.read()
                temp_seq = translator(content)
                real_seq += temp_seq
        print_or_save(chrom, real_seq)
    else:
        file_path = os.path.join(foldername, target_files)
        with open(file_path, 'r') as file: #reads file
            fastacheck = file.read(1)
            if fastacheck == '>':
                next(file) #Skip first line
                content = file.read() #read rest of file
            else:
                content = file.read()
            real_seq = translator(content)
        print_or_save(chrom, real_seq)

def translator(sequence):
    AA_Seq_temp = ""
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        AA_Seq = codon_to_AA.get(codon, 'Unknown')
        AA_Seq_temp += AA_Seq
    return AA_Seq_temp

def print_or_save(chrom, AAseq):
    username = os.getlogin()
    choice = input("\nPlease type 'print', 'save', or 'both' to:\n\tprint the results to screen (WARNING: HARD TO READ AND WILL TAKE UP LOTS OF SPACE),\n\tand/or save to your desktop under the name: sequence.txt\n\t(WARNING: This will overwrite all previous file save attempts),\n\tor press enter to return to the command prompt:\n")
    if choice == 'print':
        print(f"Amino Acid Sequence for Chromosome {chrom}: {AAseq}")
    elif choice == 'save':
        output_path = "C:\\Users\\" + username + "\\Desktop\\sequence.txt"
        with open(output_path, 'w') as file:
            file.write(AAseq)
    elif choice == 'both':
        output_path = "C:\\Users\\{username}\\Desktop\\sequence.txt"
        with open(output_path, 'w') as file:
            file.write(AAseq)
        print(f"Amino Acid Sequence for Chromosome {chrom}: {AAseq}")
    else:
        print("Unknown input, returning to start")

def gc_calculator(foldername):
    G_pct = 0
    C_pct = 0

    target_files, chrom, cORf = chrom_or_file(foldername)
    if cORf == True:
        for file in target_files:
            file_path = os.path.join(foldername, file)
            with open(file_path, 'r') as file: #reads file
                fastacheck = file.read(1)
                if fastacheck == '>':
                    next(file) #Skip first line
                    content = file.read() #read rest of file
                else:
                    content = file.read()
                A_pct, T_pct, G_pct, C_pct = AA_check(content, False)
                G_pct += G_pct
                C_pct += C_pct
        GC_calc_pct = G_pct + C_pct
        print(f"GC Percentage on Chromosome {chrom} is: {GC_calc_pct}%")
    else:
        file_path = os.path.join(foldername, file)
        with open(file_path, 'r') as file: #reads file
            fastacheck = file.read(1)
            if fastacheck == '>':
                next(file) #Skip first line
                content = file.read() #read rest of file
            else:
                content = file.read()
        A_pct, T_pct, G_pct, C_pct = AA_check(content, False)
        GC_calc_pct = G_pct + C_pct
        print(f"GC Percentage for Gene {target_files} on Chromosome {chrom} is: {GC_calc_pct}%")

def thirdCodon(foldername): #Find ratio of AUGC as third amino acid in seq
    A_pct = 0
    T_pct = 0
    G_pct = 0
    C_pct = 0
    tot_file = 0
    target_files, chrom, cORf = chrom_or_file(foldername)
    if cORf == True:
        for file in target_files:
            tot_file += 1
            file_path = os.path.join(foldername, file)
            with open(file_path, 'r') as file: #reads file
                fastacheck = file.read(1)
                if fastacheck == '>':
                    next(file) #Skip first line
                    content = file.read() #read rest of file
                else:
                    content = file.read()
                A_pct_temp, T_pct_temp, G_pct_temp, C_pct_temp = AA_check(content, True)
                A_pct += A_pct_temp
                T_pct += T_pct_temp
                G_pct += G_pct_temp
                C_pct += C_pct_temp
        A_pct = round((A_pct/tot_file), 2)
        T_pct = round((T_pct/tot_file), 2)
        G_pct = round((G_pct/tot_file), 2)
        C_pct = round((C_pct/tot_file), 2)

        print(f"\nNucleotide Percentage for Chromosome {chrom}:\n A = {A_pct}%, T = {T_pct}%, G = {G_pct}%, C = {C_pct}%.")

    else:
        file_path = os.path.join(foldername, target_files)
        with open(file_path, 'r') as file: #reads file
            fastacheck = file.read(1)
            if fastacheck == '>':
                next(file) #Skip first line
                content = file.read() #read rest of file
            else:
                content = file.read()
            A_pct_temp, T_pct_temp, G_pct_temp, C_pct_temp = AA_check(content, True)
            A_pct += A_pct_temp
            T_pct += T_pct_temp
            G_pct += G_pct_temp
            C_pct += C_pct_temp
        A_pct = round((A_pct/tot_file), 2)
        T_pct = round((T_pct/tot_file), 2)
        G_pct = round((G_pct/tot_file), 2)
        C_pct = round((C_pct/tot_file), 2)

        print(f"\nNucleotide Percentage for Gene {target_files} on Chromosome {chrom}:\n A = {A_pct}%, T = {T_pct}%, G = {G_pct}%, C = {C_pct}%.")

def AA_check(content,isThree): #does repeated process over and over again for third AA
    Acount = 0
    Tcount = 0
    Gcount = 0
    Ccount = 0
    tot = 0

    len_is = 1
    if isThree == True:
        len_is = 3

    for i in range(2, len(content), len_is):
        if content[i] == "A":
            Acount += 1
            tot += 1
        elif content[i] == "T":
            Tcount += 1
            tot += 1
        elif content[i] == "G":
            Gcount += 1
            tot += 1
        elif content[i] == "C":
            Ccount += 1
            tot += 1
        i += i
    if(tot != 0):
        A_pct = round(((Acount/tot)*100), 2)
        T_pct = round(((Tcount/tot)*100), 2)
        G_pct = round(((Gcount/tot)*100), 2)
        C_pct = round(((Ccount/tot)*100), 2)
    else:
        print("ERROR: AA Checker is not working correctly")
    return A_pct, T_pct, G_pct, C_pct

def codon_finder(foldername, codon): #finds specific codons and reports number of instances IN THE FUTURE, report positions as csv file
    codon_length = len(codon)
    tot_codon_count = 0
    amino_acid = codon_to_AA.get(codon, 'Unknown Amino Acid')
    print(f'You are searching for codon: {codon} that corresponds to {amino_acid}')
    target_files, chrom, cORf = chrom_or_file(foldername)
    if cORf == True: #checks for multiple files
        for file in target_files:
            file_path = os.path.join(foldername, file)
            with open(file_path, 'r') as file: #reads file
                fastacheck = file.read(1)
                if fastacheck == '>':
                    next(file) #Skip first line
                    content = file.read() #read rest of file
                else:
                    content = file.read()
                codoncounter = 0
                for i in range(len(content) - len(codon)): #go over chars in sequences
                    testCodon = content[i:i+codon_length]
                    if testCodon == codon: #checks to see if the codons are the same as the one asked
                        codoncounter += 1
                tot_codon_count += codoncounter
        print(f"\nCodon {codon} Count for Chromosome {chrom}: {tot_codon_count}")
    elif cORf == False:
        file_path = os.path.join(foldername, target_files)
        with open(file_path, 'r') as file: #reads file
            fastacheck = file.read(1)
            if fastacheck == '>':
                next(file) #Skip first line
                content = file.read() #read rest of file
            else:
                content = file.read()
            codoncounter = 0
            for i in range(len(content) - len(codon)): #go over chars in sequences
                testCodon = content[i:i+codon_length]
                if testCodon == codon: #checks to see if the codons are the same as the one asked
                    codoncounter += 1
        print(f"\nCodon {codon} count for Gene {target_files} on Chromosome {chrom}: {codoncounter}")

def codonAsker(): #this block asks the user to input the codon they requested, turns it to uppercase and then checks to see if the codon is all valid nucleotides
    validCodon = False
    while not validCodon:
        codonIn = input("Enter your codon: ").upper() #to uppercase
        validNucleotide = True
        for char in codonIn:
            if char not in ['A', 'C', 'G', 'T']:
                validNucleotide = False
                break  # Exit loop early if an invalid nucleotide is found
        if not validNucleotide:
            print("Error: Please input a valid codon.")
        else:
            validCodon = True
    return codonIn

def choose_chrom(foldername):
    while True:
        chrom = input("State the letter of your chromosome, or type 'all' to analyze all chromosomes in your folder: ").upper()
        if chrom == 'ALL':
            target_files = os.listdir(foldername)
            return target_files, chrom
        elif len(chrom) == 1:
            files_in_folder = os.listdir(foldername)
            target_files = [file for file in files_in_folder if len(file) > 1 and file[1] == chrom]
            return target_files, chrom
        else:
            print("Error: Invalid Chromosome Letter. Please try again.")

    #when implementing into methods use this:
    """
    for file in target_files:
        file_path = os.path.join(foldername, file)

        with open(file_path, 'r') as file: #reads file
            fastacheck = file.read(1)
            if fastacheck == '>':
                next(file) #Skip first line
                content = file.read() #read rest of file
            else:
                content = file.read()"""

def chrom_or_file(foldername):
    print("\nWould you like to analyze Chromosomes (one or all) or a single Yeast Gene File?")
    choice = input("Please type 'chromosome' for Chromosome Data or type 'single file' for a single gene: ")
    choice_matrix = {'chromosome': 'Chromosome Data', 'single file': 'Data from a Single Gene'}
    choice_type = choice_matrix.get(choice, 'Unknown')
    print(f"You chose {choice} and requested to see {choice_type}")
    chosen = True
    while chosen == True:
        if choice == 'chromosome':
            target_files, chrom = choose_chrom(foldername)
            cORf = True
            chosen = False
            return target_files, chrom, cORf
        elif choice == 'single file':
            target_file = input("Please type the name of the file you would like to analyze (example: YAL001C.txt): ")
            chrom = target_file[1]
            cORf = False
            chosen = False
            return target_file, chrom, cORf
        else:
            print("Error: Invalid choice. Please try again.")


def contains_invalid_characters(input_str, valid_DNA_nucleotide):
    pattern = f"[^{valid_DNA_nucleotide}]"
    return bool(re.search(pattern, input_str))

def cool_parrot():
    powershell_command = "curl parrot.live"
    print("\tPlease wait... Press command + c to return to the command line")
    time.sleep(5)
    try:
        subprocess.run(powershell_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running parrot.live: {e}")

codon_to_AA = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': 'Stop', 'TAG': 'Stop',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'TGT': 'C', 'TGC': 'C', 'TGA': 'Stop', 'TGG': 'W',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}


AAcode_to_full = {'A': 'Alanine','R': 'Arginine','N': 'Asparagine','D': 'Aspartic Acid',
    'C': 'Cysteine','Q': 'Glutamine','E': 'Glutamic Acid','G': 'Glycine',
    'H': 'Histidine','I': 'Isoleucine','L': 'Leucine','K': 'Lysine',
    'M': 'Methionine','F': 'Phenylalanine','P': 'Proline','S': 'Serine',
    'T': 'Threonine','W': 'Tryptophan','Y': 'Tyrosine','V': 'Valine'}

valid_DNA_nucleotide = 'ACGTatcg'

if __name__ == '__main__':
    main()
