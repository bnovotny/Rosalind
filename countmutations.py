# Counting point mutations exercise

f = open("rosalind_hamm.txt", "r")
mutation_count = 0
seq2index = 0

seq1 = f.readline()
seq2 = f.readline()

print(seq1)
print(seq2)

for i in range(len(seq1)-1):
    if seq1[i] != seq2[i]:
        mutation_count += 1

print(mutation_count)
