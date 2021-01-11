

def main():
    infile = input("Input Fasta Location: ")
    outfile = input("Output File Location: ")
    fasta_to_csv(infile,outfile)


def fasta_to_csv(infile,outfile):

    #Fasta file to be read in 
    with open(infile,"r") as fileIn:
        data = fileIn.readlines()

    #Output file
    with open(outfile,"w") as fileOut:
        combined = ""
        for line in data:
         
            if line[0] == ">":
                
                combined = line[1:len(line)-2] + ","
            else:
                
                for i in range(len(line)):
                    if i == len(line) - 1:
                        combined = combined + line[i]
                    else:
                        combined = combined + line[i] + ","
                    
                fileOut.write(combined)
                combined = ""

main()