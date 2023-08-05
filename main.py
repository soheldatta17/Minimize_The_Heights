
class Solution:
    def getMinDiff(self, arr, n, k):
        # code here 
        if(len(arr)==1):
            return 0
        arr=sorted(arr)
        d=arr[n-1]-arr[0]
        maximum=arr[n-1]
        minimum=arr[0]
        for i in range(1,n):
            if(arr[i]-k<0):
                continue
            maximum=max(arr[i-1]+k,arr[n-1]-k)
            minimum=min(arr[i]-k,arr[0]+k)
            d=min(d,maximum-minimum)
        return d