import sys

def prime(n): 
    ln=range(n+1)[1:] 
    for k in range(n): 

        out=[] 
        for l in ln[:k+1]: 

             if ln[k]%l==0: 
                 out.append(1) 
             else: 
                 out.append(0) 
        
        if sum(out)==2: 
            print(ln[k]) 

if __name__ == '__main__':
    n=int(sys.argv[1])
    prime(n)