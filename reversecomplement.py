# Complementing a Strand of DNA exercise

nucleotide_string = input("Input a string of nucleotides: ")

rev_comp_out = open('revcomp.txt', 'w')

reverse_string = nucleotide_string[::-1]
print(reverse_string)


for i in reverse_string:
    if i == 'A':
        rev_comp_out.write('T')
    elif i == 'T':
        rev_comp_out.write('A')
    elif i == 'C':
        rev_comp_out.write('G')
    else:
        rev_comp_out.write('C')
    
        
        

