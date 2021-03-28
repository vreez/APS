def solution(v):
    arr1 = []
    arr2 = []
    result = []
    for i in range(len(v)):
        if v[i][0] not in arr1:
            arr1.append(v[i][0])
        elif v[i][0] in arr1:
            arr1.remove(v[i][0])
    for i in range(len(v)):
        if v[i][1] not in arr2:
            arr2.append(v[i][1])
        elif v[i][1] in arr2:
            arr2.remove(v[i][1])    
    result = [arr1[0], arr2[0]]        
    return result