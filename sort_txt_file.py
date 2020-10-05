import random

classperiods = ["1A", "2A", "3A", "4A", "1B", "2B", "3B", "4B"]
names = ["Dylan", "David", "Eli", "Hunter"]
randomc = random.choice(classperiods)
randoms = random.randint(1, 100)
randomn = random.choice (names)
Randoms = str(randoms)

text = randomc + " " + randomn + " " + Randoms
Text = str(text)


file = open('scores.txt', 'a')
file.write(Text+"\n")   
file.close()

names = list() 
filename = 'scores.txt'

with open(filename) as fin:
  for line in fin:
    names.append(line.strip())


names.sort()
filename = 'names_sorted.txt'
with open(filename, 'w') as fout:
  for name in names:
    fout.write(name + '\n')

#1A Sorting
names.sort()
a1list = names.copy()
a1 = '1A'
a1match = [s for s in a1list if "1A" in s]
A1 = len(a1match)
A1r = len(a1list) + 1
A1delete = A1 + 1
del a1list [A1: A1r]
#print(A1)

filename = 'names_1A.txt'
with open(filename, 'w') as fout:
  for class1A in a1list:
    fout.write(class1A + "\n")

#1B Sorting
b1list = names.copy()
b1 = '1B'
b1match = [s for s in b1list if "1B" in s]
B1 = len(b1match)
B1r = len(b1list) + 1
B1delete = B1 + 1
del b1list [0: A1]
del b1list [B1: B1r]
#print(B1)

filename = 'names_1B.txt'
with open(filename, 'w') as fout:
  for class1B in b1list:
    fout.write(class1B + "\n")


#2A Sorting
names.sort()
a2list = names.copy()
a2 = '2A'
a2match = [s for s in a2list if "2A" in s]
A2 = len(a2match)
A1delete = A1 + 1
A1B1 = A1 + B1
del a2list [0: A1B1]
A2r = len(a2list) + 1
del a2list [A2:A2r]
#print(A2)

filename = 'names_2A.txt'
with open(filename, 'w') as fout:
  for class2A in a2list:
    fout.write(class2A + "\n")


#2B Sorting
names.sort()
b2list = names.copy()
b2 = '2B'
b2match = [s for s in b2list if "2B" in s]
B2 = len(b2match)
B1delete = B1 + 1
A1B1A2 = A1 + B1 + A2
del b2list [0: A1B1A2]
B2r = len(b2list) + 1
del b2list [B2:B2r]
#print(B2)

filename = 'names_2B.txt'
with open(filename, 'w') as fout:
  for class2B in b2list:
    fout.write(class2B + "\n")


#3A Sorting
names.sort()
a3list = names.copy()
a3 = '3A'
a3match = [s for s in a3list if "3A" in s]
A3 = len(a3match)
A3delete = A3 + 1
a3f = A1 + B1 + A2 + B2
del a3list [0: a3f]
A3r = len(a3list) + 1
del a3list [A3:A3r]
#print(A3)

filename = 'names_3A.txt'
with open(filename, 'w') as fout:
  for class3A in a3list:
    fout.write(class3A + "\n")


#3B Sorting
names.sort()
b3list = names.copy()
b3 = '3B'
b3match = [s for s in b3list if "3B" in s]
B3 = len(b3match)
B3delete = B3 + 1
b3f = A1 + B1 + A2 + B2 + A3
del b3list [0: b3f]
B3r = len(b3list) + 1
del b3list [B3:B3r]
#print(B3)

filename = 'names_3B.txt'
with open(filename, 'w') as fout:
  for class3B in b3list:
    fout.write(class3B + "\n")


#4A Sorting
names.sort()
a4list = names.copy()
a4 = '4A'
a4match = [s for s in a4list if "4A" in s]
A4 = len(a4match)
A4delete = A4 + 1
a4f = A1 + B1 + A2 + B2 + A3 + B3
del a4list [0: a4f]
A4r = len(a4list) + 1
del a4list [A4:A4r]
#print(A4)

filename = 'names_4A.txt'
with open(filename, 'w') as fout:
  for class4A in a4list:
    fout.write(class4A + "\n")



#4B Sorting
names.sort()
b4list = names.copy()
b4 = '4B'
b4match = [s for s in b4list if "4B" in s]
B4 = len(b4match)
B4delete = B4 + 1
b4f = A1 + B1 + A2 + B2 + A3 + B3 + A4
del b4list [0: b4f]
B4r = len(b4list) + 1
del b4list [B4:B4r]
#print(B4)

filename = 'names_4B.txt'
with open(filename, 'w') as fout:
  for class4B in b4list:
    fout.write(class4B + "\n")

#letter = input ("Which class period would you like to sort through? >> ")
