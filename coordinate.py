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

coordinates = ["atom", "x", "y", "z"]
for i in range(0, natom):
    temp = data[i].split()

    coordinates[0] = "\'" + temp[3] + "\'"
    coordinates[1] = temp[0]
    coordinates[2] = temp[1]
    coordinates[3] = temp[2]

    file.write("\'" + temp[3] + "\'" + "\t" + temp[0] + "\t" + temp[1] + "\t" + temp[2] + "\n")

file.close()
