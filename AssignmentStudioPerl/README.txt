FOR THE LIST OF MY DOCUMENTS PLEASE SKIP TO LINE 25!

This weeks assignment is to:
1. Use your own commenting to properly annotate the parsefile.pl script and remove Dr. Babbit's comments/questions

2. In geneparse.pl, reduce the amount of ‘printing to the screen’. Does the script seem to
run faster? Time it and find out. Rewrite the script so that its behavior on your screen
is cleaner....and faster.

3. Using a procedural style of coding, make a new Perl script that will read the directory
entitled ‘YeastGenes’, retrieve the name of each file and print it to your screen, parse
and read only the DNA sequence of each file and calculate GC content, print GC content
to your screen. (note- you can use the smaller directory YeastGenesA to more quickly
test code during development)

4. Add feature to your loop that returns something measured from the gene that is more
novel. Advanced option: find the correct log2transcription values for each ORF/gene
from the RNA-seq data provided and return it with you GC content value for each gene
(hint: use split() function and a specific character or RegEx to break the number out of
the string for the whole line in the RNA-seq results file)

5. Now add the creation of an ‘output’ file and folder where the information from #4 and
#5 is printed and saved for each ORF/gene

THE FOLLOWING FILES ARE: 
1. parsefile.pl - Own commenting to properly annotate
2. geneparse.pl - reduced printing to screen. This does run faster, but I kept one line to make sure the program was working through every file. 
3. danParsefile.pl - procedural style of coding to make a new script 
4. danParsefilePT4.pl - New script with DNA -> Protein sequence with 1-letter AAs.
5. 
