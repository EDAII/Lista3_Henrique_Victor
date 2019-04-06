def merge_sort(v):
  if len(v) >1: 
        mid = len(v)//2
        L = v[:mid]  
        R = v[mid:]

        merge_sort(L)
        merge_sort(R)
  
        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                v[k] = L[i] 
                i+=1
            else: 
                v[k] = R[j] 
                j+=1
            k+=1
          
        while i < len(L): 
            v[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            v[k] = R[j] 
            j+=1
            k+=1


def particao(v, low, high): 
    i = low-1
    pivot = v[high]
  
    for j in range(low , high): 
        if v[j] <= pivot: 
            i = i+1 
            v[i],v[j] = v[j],v[i] 
  
    v[i+1],v[high] = v[high],v[i+1] 
    return ( i+1 )


def quick_sort_recursivo(v, low, high): 
    if low < high: 
        pi = particao(v,low,high) 

        quick_sort_recursivo(v, low, pi-1) 
        quick_sort_recursivo(v, pi+1, high)


def quick_sort_estavel(v):
    if len(v) <= 1: 
        return v 
   
    else: 
        mid = len(v)//2
        pivot = v[mid] 
        smaller,greater = [],[]  

        for indx, val in enumerate(v): 
            if indx != mid: 
                if val < pivot: 
                    smaller.append(val) 
                elif val > pivot: 
                    greater.append(val) 
                else: 
                    if indx < mid: 
                        smaller.append(val) 
                    else: 
                        greater.append(val)
                        
        return quick_sort_estavel(smaller)+[pivot]+quick_sort_estavel(greater)