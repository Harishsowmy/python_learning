file_1=open("test.tst")
file_2=open("test2.pxt", 'a')

for line in file_1:
    file_2.write(line)
    file_2.write("\n")

file_1.close()
file_2.close()