class Solution:
	def findMaximum(self,arr, n):
		# code here
		return max(arr)
#{ 
 # Driver Code Starts

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1
# } Driver Code Ends