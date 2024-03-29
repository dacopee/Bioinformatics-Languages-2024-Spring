#!/usr/bin/perl


# here is a Perl script that runs through each file in the 'Yeast Alignment' folder
# and extracts the sequence, reverse complements it if needed and prints it out to a new folder

# please annotate the functioning code below
#...replacing the questions below with what you think the code right below it does

# what does this line do?
# makes new directory for output files to store them 
mkdir "ProcessedYeastAlns"; #or die "\nProcessedYeastAlns folder already exists. Delete it and try again.\n";
$filecount = 0;
$file_iteration = 0;

# what do these four variables represent? How are they used later in the code?  
# these four variables are possible headings in the gene files that need to be ignored as they are not valid nucleotides
$sp1_heading = "Scer";
$sp2_heading = "Spar";
$sp3_heading = "Smik";
$sp4_heading = "Sbay";

# what does this part do?
# Opens a directory called YeastAlignments or kills the code if the directory cannot be found or opened
# $dir is a variable named for the folder
$dir = "YeastAlignments";
opendir(DIR,$dir)or die "can't open directory $dir:$!";
print"\n";
print "Alignment files in $dir are:\n";

# what generally happens as result of the following while loop?
# allignment files (yeast genes) are looked over and opened until the program goes through every file in the dir 
while ($filename = readdir DIR){ 

$filecount = $filecount + 1;

# what does the following substring return? Is it used later in the code...where?
# the name of the open reading frame
# they are used later to name the outputs to their respective DNA 
$ORFname = substr($filename, 1, 7);
print "ORFname = "."$ORFname\n";

# what does the following substring return?  what does it tell you about the gene?
# this returns a substring of the file name starting at position 7 (8th char as perl is zero-indexed) and goes one char further
# the 4 yeast species
$WatsonCrick = substr ($filename, 7, 1);
#print "$WatsonCrick\n";

# what do the next five lines of code do?
# Opens a file in the yeast alignments folder if the name is 7 char long, or goes to next and then opens the folder and creates a new file for output data
$filelocation = "./YeastAlignments/"."$filename";
if (length $ORFname == 7){
open (INFILE, $filelocation) or die "Cannot open file";
}
else {next;}
open (OUTFILE, ">"."./ProcessedYeastAlns/"."$filename") || die " could not open output file\n";


# the next four variables initiate empty strings that will grow later in the loop  
  $flat1 = "";
  $flat2 = "";
  $flat3 = "";
  $flat4 = "";
  
# this is another while loop nested in the previous while loop
# what does it basically do?
# This splits up the DNA strands at white spaces and matches the sequences to concatonate into genes of other yesat species 
  while(<INFILE>){
    chomp;
    # we talked about this split array function in class today
    # here it is associated with regular expressions..we will cover them later in course
    # look in our Perl pocket guide to find out what 's+' and 'm' and 'tr' do
        # s+ - this splits our string at a white space char
        # m - matches a char in your string 
        # tr - this replaces an entire string
    @a = split(/\s+/, $_);
    #print "$_\n";
    # the if statements below are used to grab lines of sequence matching each
    # of the 4 yeast species and concatenate them together into a single sequence
    # What is the Perl symbol that indicates concatenation?
      # '.'
    if($_ =~ m/^$sp1_heading/){
      $flat1 = $flat1.$a[1];
      }
    elsif($_ =~ m/^$sp2_heading/){
      $flat2 = $flat2.$a[1];
      }
    elsif($_ =~ m/^$sp3_heading/){
      $flat3 = $flat3.$a[1];
      }
    elsif($_ =~ m/^$sp4_heading/){
      $flat4 = $flat4.$a[1];
      }
  }
  
  # the large block of code below reverse complements genes if needed? - Yes?
  # How are these genes files recognized by the code?
    # the gene files are reccognized by thier formatting
  # What does the command 'reverse' do to a string variable?
    # this reverses a string
  # what does the 'tr' n the regular expression do?...look it up if needed
    #relplaces characters in a string by their respective told position
  
  # sequence 1
  if ($WatsonCrick eq "C"){my $revcom = reverse $flat1; $revcom =~ tr/ACGTacgt/TGCAtgca/; $sequenceA = $revcom;}
  if ($WatsonCrick eq "W"){$sequenceA = $flat1;}
  print OUTFILE "$sp1_heading\t"."$sequenceA\n";
  # sequence 2
  if ($WatsonCrick eq "C"){my $revcom = reverse $flat2; $revcom =~ tr/ACGTacgt/TGCAtgca/; $sequenceB = $revcom;}
  if ($WatsonCrick eq "W"){$sequenceB = $flat2;}
  print OUTFILE "$sp2_heading\t"."$sequenceB\n";
  # sequence 3
  if ($WatsonCrick eq "C"){my $revcom = reverse $flat3; $revcom =~ tr/ACGTacgt/TGCAtgca/; $sequenceC = $revcom;}
  if ($WatsonCrick eq "W"){$sequenceC = $flat3;}
  print OUTFILE "$sp3_heading\t"."$sequenceC\n";
  # sequence 4
  if ($WatsonCrick eq "C"){my $revcom = reverse $flat4; $revcom =~ tr/ACGTacgt/TGCAtgca/; $sequenceD = $revcom;}
  if ($WatsonCrick eq "W"){$sequenceD = $flat4;}
  print OUTFILE "$sp4_heading\t"."$sequenceD\n";
  
  # what does the remainder of the code do?
    # this code gets the length of the strings after they have been "worked through" by the code and stores it in their variable, this is able to be printed later
  $sequencelengthA = length $sequenceA;
  $sequencelengthB = length $sequenceB;
  $sequencelengthC = length $sequenceC;
  $sequencelengthD = length $sequenceD;
  
#print "\nlocal alignments\n";
#print "sequence A\n";
#print "$sequenceA\n";
#print "sequence B\n";
#print "$sequenceB\n";
#print "sequence C\n";
#print "$sequenceC\n";
#print "sequence D\n";
#print "$sequenceD\n";
#print "\n";
#print "sequence lengths\n";
#print "$sequencelengthA\t"."$sequencelengthB\t"."$sequencelengthC\t"."$sequencelengthD\n";
#print "\n\n";
close OUTFILE;

} # end while loop
print "end program\n";
exit;
