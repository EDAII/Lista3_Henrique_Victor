import math


def merge_sort(v):
    if len(v) > 1:
        mid = len(v)//2
        L = v[:mid]
        R = v[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                v[k] = L[i]
                i += 1
            else:
                v[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            v[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            v[k] = R[j]
            j += 1
            k += 1


def particao(v, low, high):
    i = low-1
    pivot = v[high]

    for j in range(low, high):
        if v[j] <= pivot:
            i = i+1
            v[i], v[j] = v[j], v[i]

    v[i+1], v[high] = v[high], v[i+1]
    return (i+1)


def quick_sort_inst_rec(v, low, high):
    if low < high:
        pi = particao(v, low, high)

        quick_sort_inst_rec(v, low, pi-1)
        quick_sort_inst_rec(v, pi+1, high)


def quick_sort_est_rec(v):
    if len(v) <= 1:
        return v

    else:
        mid = len(v)//2
        pivot = v[mid]
        smaller, greater = [], []

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

        return quick_sort_est_rec(smaller)+[pivot]+quick_sort_est_rec(greater)


def quick_sort_inst_iterat(v, l, h): 
    size = h - l + 1
    stack = [0] * (size) 
    top = -1 
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h 

    while top >= 0: 
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
        p = particao(v, l, h) 

        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1

        if p+1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


def bucket_sort(v):
    bucketSize = len(v) // 2
    if(len(v) == 0):
        print('Vetor está vazio!')
        return

    minValue = v[0]
    maxValue = v[0]

    for i in range(0, len(v)):
        if v[i] < minValue:
            minValue = v[i]
        elif v[i] > maxValue:
            maxValue = v[i]

    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    for i in range(0, len(v)):
        buckets[math.floor((v[i] - minValue) /
                           bucketSize)].append(v[i])

    sortedvay = []
    for i in range(0, len(buckets)):
        buckets[i].sort()
        for j in range(0, len(buckets[i])):
            sortedvay.append(buckets[i][j])

    return sortedvay