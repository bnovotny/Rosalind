# Rabbits and Recurrent Relations exercise

months_int = int(input("Please input the number of months: "))
litter_int = int(input("Please input the litter size in pairs: "))

bunnies_int = 0

n_list = [0,2]

i = 1

while i in range(months_int):
    
    nlist_temp = n_list[1]
    
    bunnies_int = n_list[0]*litter_int + n_list[1]
    
    n_list[0]=n_list[1]
    
    n_list[1] = bunnies_int
    
    i = i+1

print(bunnies_int/2)