fname = input("please enter file  name ");
fileref = open(fname,'r');
sline = fileref.readline();
listofwords=[];
while sline!="":
    for sstr in sline.split():
        listofwords.append(sstr.lower());
    sline = fileref.readline();
print("words seperated by whitespace")
print(listofwords)

#initializing dictionary
dict={}

#counting words and adding in dictionary using word as key
for lword in listofwords:
    dict[lword]=dict.get(lword,0)+1

#writing into file
writefile=input("enter the file name to write back the wordcount")
with open(writefile, 'w') as f:
    for item in dict.keys():
        f.write(str(item))
        f.write(":")
        f.write(str(dict[item]))

        print(item)
        print(dict[item])