# Define the target atom
target_atom = "/6m0j/B/E/501/CA" #change target residue at this line

distances_dict = {}

# Iterate through all A,I,L,V methyl atoms and calculate distances
alanine_cb_selection = "resn ALA and name CB"
isoleucine_cd1_selection = 'resn ILE and name CD1'
leucine_cd1_selection = 'resn LEU and name CD1'
valine_cg1_selection = 'resn VAL and name CG1'

for A in cmd.get_model(alanine_cb_selection).atom: #alanine_cb
    atom_id = A.id
    residue_number = A.resi  
    distance_value = cmd.distance(f"tmp_{atom_id}", target_atom, f"ID {atom_id}")
    if residue_number in distances_dict:
        distances_dict[residue_number].append(distance_value)
    else:
        distances_dict[residue_number] = [distance_value]
    cmd.delete(f"tmp_{atom_id}")

for I in cmd.get_model(isoleucine_cd1_selection).atom: #isoleucine_cd1
    atom_id = I.id
    residue_number = I.resi  
    distance_value = cmd.distance(f"tmp_{atom_id}", target_atom, f"ID {atom_id}")
    if residue_number in distances_dict:
        distances_dict[residue_number].append(distance_value)
    else:
        distances_dict[residue_number] = [distance_value]
    cmd.delete(f"tmp_{atom_id}")

for L in cmd.get_model(leucine_cd1_selection).atom: #leucine_cd1
    atom_id = L.id
    residue_number = L.resi  
    distance_value = cmd.distance(f"tmp_{atom_id}", target_atom, f"ID {atom_id}")
    if residue_number in distances_dict:
        distances_dict[residue_number].append(distance_value)
    else:
        distances_dict[residue_number] = [distance_value]
    cmd.delete(f"tmp_{atom_id}")

for V in cmd.get_model(valine_cg1_selection).atom: #valine_cg1
    atom_id = V.id
    residue_number = V.resi  
    distance_value = cmd.distance(f"tmp_{atom_id}", target_atom, f"ID {atom_id}")
    if residue_number in distances_dict:
        distances_dict[residue_number].append(distance_value)
    else:
        distances_dict[residue_number] = [distance_value]
    cmd.delete(f"tmp_{atom_id}")

# output a file
with open("N501Y_methyl_distance.txt", "w") as file: #change file name
    for residue_number, distances in distances_dict.items():
        for distance_value in distances:
            data = f"Residue {residue_number}: {distance_value:.2f} Å\n"
            file.write(data)




