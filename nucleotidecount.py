# Counting DNA Nucleotides exercise

base_dict = {'A':0, 'C':0, 'T':0, 'G':0}

nucleotide_str = input("Please input a string of nucleotides: ")

for base in nucleotide_str:
    base_dict[base] += 1
    
print(base_dict['A'], base_dict['C'], base_dict['G'], base_dict['T'])


