bus_no =  input("Enter the bus no: ")
file = open("example.txt","r")
file1 = open("abc.txt","w")
def func_1(file,file1,bus_no):
        data = file.readlines()
        for line in data:
             word = line.split()
             if bus_no in word:
                    a = " ".join(word[1:])
       
        print(a)
func_1(file,file1,bus_no)


