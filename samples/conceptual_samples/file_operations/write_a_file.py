# this sample python program is for writing something into a file

filename=raw_input('enter the filename in which the contents that you will enter later will be stored : \t')
print '\n\nopening the file......\n';
target =open(filename,'w')

print'now iam going to ask you to enter three lines .\n'

line1=raw_input("enter your first line here:\n")
line2=raw_input("enter your second line here:\n")
line3=raw_input("enter your third line here:\n")

print "\niam going to write these to the file.\n";

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "\nand finally , we close it.";
target.close();

#the end . happy coding
