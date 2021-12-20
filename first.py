#F1 will open the file in read mode
f1 = open("input2.txt", "r")

#for i in range(0,3):  #This loop will run thrice, checking all the three lines written in the text file

def calculate():          # Function to calculate the given statement
    one = 0
    z = 0
    for j in range(3):          #This loop will run a maximum of 3 times
        f2 = [f1.readline()]    #Reading each character in a list
        length2 = len(f2)       #Takes the length of the sequence
        f3 = [f2]
        print(f2)
#        print("Length of the sequence is:",  length2)
#        print(f3)
#This loop will run while f2 == 0, If f2 becomes 1, it will add 1 in the variable one and continue searching for the next sequence
        for k in range(length2):
            while f3[k] == 0:
                one += 1
                if f3[k] == 1:
                    continue
                else:
                    one = one + 0
            #one = one + 1
        print("Sequence of 1's are: ", one)
        print(end="\n")

a = input()
print(calculate())
print("helloooohkjl"+str(2))
print("sssss")

#print(calculate(34))
