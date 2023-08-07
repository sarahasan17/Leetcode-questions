def Solve (N, A):
    n=len(A)
    close=A[0]
    for i in range(1,n):
        if(A[i]>=0):
            diff=A[i]
        else:
            diff=0-A[i]
        if(diff<close and close>=0):
            close=A[i]
        elif(diff<=-1*close and close<0):
            close=A[i]
            
    return close

    # Write your code here
    
N = input()
A = list(map(int, input().split()))
out_ = Solve(N, A)
print (out_)
