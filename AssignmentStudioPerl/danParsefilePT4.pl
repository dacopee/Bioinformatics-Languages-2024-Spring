


%genetic_code = (
    'TTT' => 'F', 'TTC' => 'F', 'TTA' => 'L', 'TTG' => 'L',
    'TCT' => 'S', 'TCC' => 'S', 'TCA' => 'S', 'TCG' => 'S',
    'TAT' => 'Y', 'TAC' => 'Y', 'TAA' => '*', 'TAG' => '*',
    'TGT' => 'C', 'TGC' => 'C', 'TGA' => '*', 'TGG' => 'W',
    'CTT' => 'L', 'CTC' => 'L', 'CTA' => 'L', 'CTG' => 'L',
    'CCT' => 'P', 'CCC' => 'P', 'CCA' => 'P', 'CCG' => 'P',
    'CAT' => 'H', 'CAC' => 'H', 'CAA' => 'Q', 'CAG' => 'Q',
    'CGT' => 'R', 'CGC' => 'R', 'CGA' => 'R', 'CGG' => 'R',
    'ATT' => 'I', 'ATC' => 'I', 'ATA' => 'I', 'ATG' => 'M',
    'ACT' => 'T', 'ACC' => 'T', 'ACA' => 'T', 'ACG' => 'T',
    'AAT' => 'N', 'AAC' => 'N', 'AAA' => 'K', 'AAG' => 'K',
    'AGT' => 'S', 'AGC' => 'S', 'AGA' => 'R', 'AGG' => 'R',
    'GTT' => 'V', 'GTC' => 'V', 'GTA' => 'V', 'GTG' => 'V',
    'GCT' => 'A', 'GCC' => 'A', 'GCA' => 'A', 'GCG' => 'A',
    'GAT' => 'D', 'GAC' => 'D', 'GAA' => 'E', 'GAG' => 'E',
    'GGT' => 'G', 'GGC' => 'G', 'GGA' => 'G', 'GGG' => 'G',
);

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

my $DNACount = 0;
my $GCPCT = 0;
my $CGCount = 0;
my $DNA = <INFILE>;
my $protein_sequence= '';
    #print"$DNA\n"; #test what is seen from DNA
    $CGCount = $DNA =~ tr/CG//;
    $DNACount = $DNA =~ tr/CGAT//;

    if ($DNACount != 0) {
      $GCPCT = ($CGCount / $DNACount)*100;
      print "GC Percentage: ", $GCPCT, "%";}
    else {
      print "N/A\n";}

      print "\nEncoded Protein: \n";

    for (my $i = 0; $i < length($DNA); $i += 3) {
        my $codon = substr($DNA, $i, 3); # Extract three characters
        if (exists $genetic_code{$codon}) {
            my $amino_acid = $genetic_code{$codon};
            #print "$amino_acid";
            $protein_sequence .= $amino_acid;
        } else {
            print "Error: Incorrect codon: $codon\n";
        }
    }

}                 

}  # end while loop



print "\n\nEnd Program, each '*' was a Stop Codon\n";  
