



$dir = "YeastGenesA"; 
opendir(DIR,$dir) or die "can't open directory $dir:$!"; #open the dir with yeast genes
print"\n"; 

while ($filename = readdir DIR){ # loop through alignment files
  $ORFname = substr($filename, 0, 7);
  print "\nFile Name: "."$ORFname\n";
  $filelocation = "./YeastGenesA/"."$filename";
if (length $ORFname == 7){
   open(INFILE, $filelocation) or die "Cannot open file";}

while (<INFILE>){

my $CGCount = 0;
my $DNA = <INFILE>;
    #print"$DNA\n"; #test what is seen from DNA
    for (my $i=0; $i )

}

         
                  
}  # end while loop
