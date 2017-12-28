

def main(n):
    arr = { }
    
    ret = []
    for i in n:
        arr[bin(i).count("1")] = []

    for i in n:
        arr[bin(i).count("1")].append(i)
        
    for i in n:
        arr[bin(i).count("1")] = sorted(arr[bin(i).count("1")])
        
    for item in arr:
        for ch in arr[item]:
            ret.appent(ch)
            
    return ret
    


main()
