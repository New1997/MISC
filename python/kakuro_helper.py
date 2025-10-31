wrong = True
while wrong :
    total_depth = int(input("Please enter how many variables you need (1-9) : "))
    wrong = total_depth<1 or total_depth>9
wrong = True
while wrong :
    number = int(input("Please enter the sum that you seek (1-45) : "))
    wrong = number<1 or number>45
solution = [[] for i in range(45)]
vals = [i+1 for i in range(total_depth)]
def recurr(depth,val,sol):
    if depth == 0:
            sol[sum(val)-1]+=[val.copy()]
    else :
        indice_val = len(val)-depth
        for i in range(val[indice_val],11-depth):
            val[indice_val]=i
            if depth > 1:
                val[indice_val+1]=i+1
            recurr(depth-1,val,sol)
    return
    
recurr(total_depth,vals,solution)

print("The",len(solution[number-1]),"ways to sum up to",number,"with",total_depth,"numbers are :")    
for i in solution[number-1]:
    print(i)
    
