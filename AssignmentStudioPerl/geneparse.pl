#!/usr/bin/perl


# here is a Perl script that runs through each file in the 'YeastGene' folder and extracts the sequence, calculates GC content, and prints it out to a new folder

# please annotate the functioning code below
#...replacing the questions below with what you think the code right below it does

# This line creates a new folder
$filecount = 0;
$file_iteration = 0;

mkdir 'ProcessedGenes';
# opens the folder to create new files
$dir = "YeastGenes"; opendir(DIR,$dir) or die "can't open directory $dir:$!"; print"\n"; #DIR is called a "file handle"
open(OUTFILE2, ">myGC+TransLevels.txt") or die "can't open file\n";

# reads the directory and adds one after each file has been read
while ($filename = readdir DIR){ # loop through alignment files
  $ORFname = substr($filename, 0, 7);
  #print "\nmy ORF name is "."$ORFname\n";
  $filelocation = "./YeastGenes/"."$filename";
  if (length $ORFname == 7){
    open(INFILE, $filelocation) or die "Cannot open file";
  }else {next;}
    open (OUTFILE, ">"."./ProcessedGenes/"."$filename") || die " could not open output file\n";
  $ORFname = substr($filename, 0, 7);
  $fileRNA = "./Yeast_RNAseq/"."Nagalakshmi_2008_5UTRs_V64.gff3";
  open(INFILE2, $fileRNA) or die "Cannot open file";
  @RNAfile = <INFILE2>;

  for (my $i = 0; $i<scalar @RNAfile; $i++){
         my $line = @RNAfile[$i];
         #print "hi Dr B\n";
         #print $line;
         @line_segments = split(/\s+/, $line); # split on whitespace
         $line_segment = @line_segments[8];
         $ORFtest = substr($line_segment, 3, 7);
         #@transLevel_test = split(/;/, $line_segment);
         @transLevel_test = split(";", $line_segment);  #split on semicolon
         $transLevel_test = @transLevel_test[2];
         $transLevel_test = substr($transLevel_test, 25, 5);  # just get numbers
         #$transLevel_test = int($transLevel_test);
         #print $filename."\t".$ORFname."\t".$ORFtest."\t".$transLevel_test."\n";
         if($ORFname eq $ORFtest){$transLevel = $transLevel_test;
                print $filename."\t".$ORFname."\t".$ORFtest."\t".$transLevel_test."\n";}
         #alternatively
         if($line =~ m/$ORFname/){$transLevel = $transLevel_test;
                print $filename."\t".$ORFname."\t".$ORFtest."\t".$transLevel_test."\n";
                print OUTFILE2 $filename."\t".$ORFname."\t".$ORFtest."\t".$transLevel_test."\n";
               }
                  
         }  # end for loop
  #print @RNAfile;
  close INFILE2;
  
  
  
  
# this is another while loop nested in the previous while loop
#  what does it basically do?
# This is used to cut down on some of the extra spaces and characters 
  while(<INFILE>){
    #print "in counting while loop\n";
    chomp;
    my $totalCount = 0;
    my $CGCount = 0;
    my $DNA = <INFILE>;
    
    
    # print($DNA . "\n");
    print OUTFILE ($DNA . "\n");
    #exit;
    my $position = 0;
    my $DNAsize = length($DNA);
    my $counter = 0;
    while($counter !=  $DNAsize){
      my $base = substr($DNA, $position, 1);
      #print $position . "position\n";
      #print($base . "base\n");
      if($base eq "A" || $base eq "T"  || $base eq "C"  ||  $base eq "G" ){
        #print($base . "base first condition\n");
        $totalCount++;
        #print($str . "\n");
        #print $totalCount . "total Count \n";
      }
      if($base eq "G" || $base eq "C"){
        #print($base . "base second condition\n");
        $CGCount++;
        #print $CGCount . "CG count\n";
      }
      #print "$CGCount";
      $position++;
      $counter++;
    }
    #print "out of part reading to eof\n";
#print "countGC "."$ORFname\t"."$CGCount\n";
#print "countTTL "."$ORFname\t"."$totalCount\n";
$freqGC = $CGCount/$totalCount;
#print "transLevel and freqGC "."$ORFname\t"."$transLevel\t"."$freqGC\n";
print OUTFILE "countGC "."$ORFname\t"."$CGCount\n";
print OUTFILE "countTTL "."$ORFname\t"."$totalCount\n";
print OUTFILE "freqGC "."$ORFname\t"."$freqGC\n";
print OUTFILE "transLevel "."$ORFname\t"."$transLevel\n";
#sleep(1);
#print "\n\n";

close OUTFILE;
close INFILE;


               

                
  }

} # end while loop
print "end program\n";
close OUTFILE2;
exit;