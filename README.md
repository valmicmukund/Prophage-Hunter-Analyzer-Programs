ProphageHunterAnalyzer.py is a script that allows the user to obtain phage nucleotide sequences within a .txt file with summarized information within the names. The .txt file is based on (1) the bacterial take in a whole genome .fasta sequence (input to Prophage Hunter) and (2) the main Prophage Hunter output.

ProphageHunterAnalyzer.py 

After running Prophage Hunter on a bacterial whole genome sequence, use this program to create a .txt file in fasta format that contains the phage nucleotide sequences and, within the names, the strain name, candidate number, and phage status (active, ambiguous) of found phages. The program takes in the file directory of a folder containing &#39;sequence&#39; and &#39;output&#39; files - referring to the input whole genome .fasta sequence and Main_output.txt from Prophage Hunter, respectively. Whole genome sequence inputs only. Only ambiguous and active phages are reported by this program currently.
