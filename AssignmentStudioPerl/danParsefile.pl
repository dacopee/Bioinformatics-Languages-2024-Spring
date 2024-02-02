



$dir = "YeastGenes"; 
opendir(DIR,$dir) or die "can't open directory $dir:$!"; #open the dir with yeast genes
print"\n"; 

while ($filename = readdir DIR){ # loop through alignment files
  $ORFname = substr($filename, 0, 7);
  print "\nFile Name: "."$ORFname\n";
  $filelocation = "./YeastGenes/"."$filename";
if (length $ORFname == 7){
   open(INFILE, $filelocation) or die "Cannot open file";}

while (<INFILE>){

my $DNACount = 0;
my $GCPCT = 0;
my $CGCount = 0;
my $DNA = <INFILE>;
    #print"$DNA\n"; #test what is seen from DNA
    $CGCount = $DNA =~ tr/CG//;
    $DNACount = $DNA =~ tr/CGAT//;

    if ($DNACount != 0) {
    $GCPCT = ($CGCount / $DNACount)*100;
    print "GC Percentage: ", $GCPCT, "%";}
    else {
    print "N/A\n";
}
}                  
}  # end while loop
print "\n\nEnd Program\n";  
