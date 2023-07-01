file1="Z:\\WhiteHat Project\\Pro 2\\txt1.txt"
file2="Z:\\WhiteHat Project\\Pro 2\\txt2.txt"

with open(file1,'r')as a:
    data1=a.read()
    a.close()

with open(file2,'r')as b:
    data2=b.read()
    a.close()

with open(file1,'w')as a:
    a.write(data2)
    a.close()

with open(file2,'w')as a:
    a.write(data1)
    a.close()