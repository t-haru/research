#print("Number of atoms ? ")
#natom = input('')

file = open("MolView.mol", "r")
lines = file.readlines()
file.close()

file = open("atom_coordinate.dat", "w")

atom = lines[3].split()
#print(atom)
natom = int(atom[0])

data = []
for i in range(4, 4+natom):
    data.append(lines[i])

coordinates = {}
for i in range(0, natom):
    temp = data[i].split()

    coordinates["atom"] = "\'" + temp[3] + "\'"
    coordinates["x"] = temp[0]
    coordinates["y"] = temp[1]
    coordinates["z"] = temp[2]

    file.write(coordinates["atom"] +"\t"+ coordinates["x"] +"\t"+ coordinates["y"] +"\t"+ coordinates["z"] + "\n")

file.close()
