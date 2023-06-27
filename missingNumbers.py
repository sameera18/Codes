class Solution:
    def missingNumber(self,array,n):
        sum1=(n*(n+1))//2
        sum2=sum(array)
        ans=sum1-sum2
        return ans
#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends