# Computing GC Content exercise

f = open("exampleGC.txt", "r")
max_GC_count = 0

with open('rosalind_gc.txt', 'r') as f:
    for line in f:
        if line[0] == ">":
            id = line
            id = id.lstrip('>')
            GC_count = 0
            total_count = 0
        else:
            seq = line
            seq = seq.rstrip('\n')
            for c in seq:
                if c == "C" or c == "G":
                    GC_count += 1
                total_count += 1
        if GC_count > max_GC_count:
            max_GC_count = GC_count
            max_total_count = total_count
            max_id = id
                
        if 'str' in line:
            break
    
print(max_id)
print((max_GC_count/max_total_count)*100)
