def bbSort(nlist):
    for passn in range(len(nlist)-1,0,-1):
        for i in range(passn):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

nlist = [1,12,64,34,27,56,45,94,85,72]
bbSort(nlist)
print(nlist)
