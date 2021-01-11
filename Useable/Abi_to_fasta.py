from Bio import SeqIO
import os
import sys



#Function for User decision trees mosly for file deletion     
def ask_user(m):
    YES_SET = {'Y','y','yes','Yes'}
    NO_SET = {'N','n','No','no'}
    
    answer = input(m)
    try:
        while answer not in YES_SET and answer not in NO_SET:
            answer = input(m)
            print(answer)
        if answer in YES_SET:
            return True
        else:
            return False
    except:
        answer = ask_user(m)
    
    

#Converts all abi files in a folder into fasta files in a folder called fastaOut then calls a combined function to combine them
def folder_abi_to_fasta(folder):
    files = os.listdir(folder)        #List all files
    #Check for existing fastaOut file
    if os.path.exists(folder+"/fastaOut"):
        import shutil
        
        answer = ask_user("A fasta folder already exists. Do you wish to overwrite? (Y/N): ")
        
        if answer:
            shutil.rmtree(folder+"/fastaOut")
            #shutil.rmtree(folder+"/dateTime")
        elif not answer:
            input("Script ended by user. Fasta files could not be extracted")
            return
            
    os.mkdir(folder+"/fastaOut")    #Make a folder to seperate the fasta files
    #os.mkdir(folder+"/dateTime/")     #Testing for datetime
    for i in files:
        if i.endswith(".ab1"):    
            try:
        
                get_user_defined_sequence(folder,folder+"/"+i)
            except:
                raise
                print(i)
                
    
    #print("Number of files with errors: "+str(count))
    combine_fasta(folder+"/fastaOut")

#combines a list of fasta files into a file called combined.fasta in the same folder
def combine_fasta(folder):
#Check fo existing combined file
    if os.path.exists(folder+"/Combined.fasta"):
        
        answer = ask_user("A combined fasta file already exists. Do you wish to overwrite? (Y/N): ")
        
        if answer:
            os.remove(folder+"/Combined.fasta")
        
        elif not answer:
            input("Script ended by user. Combined file was not overwritten")
            return
    
    file_list = os.listdir(folder)
    with open(folder+"/Combined.fasta",'a') as file:
        for i in file_list:
            if i.endswith(".fasta"):
                try:
                    with open(folder+"/"+i,'r') as fastaF:
                        file.write(fastaF.read())
                except:
                    raise
                    

#In order to get user called sequence raw data must be grabbed and user defined sequence key is PBAS1
#Will manually create a fasta file from that and sample name
def get_user_defined_sequence(folder,fi):
    
    data = SeqIO.read(fi,'abi') 
    sequence = data.annotations['abif_raw']['PBAS1'].decode('utf-8')
    name = data.annotations['abif_raw']['SMPL1']
    date = data.annotations['abif_raw']['RUND1']
    #Output names from abi varies and can create some problems with encoding. Forcing odd characters to '?' then removing
    name = name.decode('utf-8').replace('?','')
    input(name)
    with open(folder+"/fastaOut/"+name+"_"+date+".fasta",'w') as file:
        
        print('#',name)
        file.write(">"+name+"_"+date+'\n')
        file.write(sequence+'\n')
    
    #with open(folder+"/dateTime/"+name+"_"+count+".txt",'w') as file:
    #    file.write(">"+name+"_"+count+'\n')
    #    file.write(date+'\n')
    #    file.write(sequence+'\n')
        
        
    

try:
    folder_abi_to_fasta(sys.argv[1])
except:
    #Put in information for running script
    answer = ask_user("Do you wish to extract fasta files from abi files? (Y/N): ")
    if answer:
        folder = input("Please provide a complete folder path: ")
        try:
            folder_abi_to_fasta(folder)
        except:
            print("stuff failed")
            raise
    
        


    
