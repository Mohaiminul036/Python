def FindFalseCoin(coin,low,high):
    sum1=0
    sum2=0
    sum3=0
    if low+1==high:
        if coin[low]>coin[high]:
            return high
        else:
            return low
    elif (high+low+1)%2==0:#如果硬币数量是偶数
        for i in range(low,low+(high-low)//2+1):
            sum1=sum1+coin[i] #前半段求和
        for i in range(low+(high-low)//2+1,high+1):
            sum2=sum2+coin[i] #后半段求和
        print(low,high)
        if sum1>sum2:
            result=FindFalseCoin(coin,low+(high-low)//2+1,high)
            return result
        else:
            result=FindFalseCoin(coin,low,low+(high-low)//2)
            return result
    else: #如果硬币数量是奇数
        for i in range(low,low+(high-low)//2):
            sum1=sum1+coin[i]  #前半段求和
        for i in range(low+(high-low)//2+1,high+1):
            sum2=sum2+coin[i]  #后半段求和
        sum3=coin[low+(high-low)//2]
        if sum1>sum2:
            result=FindFalseCoin(coin,low+(high-low)//2+1,high)
            return result
        elif sum1<sum2:
            result=FindFalseCoin(coin,low,low+(high-low)//2-1)
            return result
        else:
            result=low+(high-low)//2+1
            return result

def main():
    coin=[1,2,2,2,2,2,2,2]
    res=FindFalseCoin(coin,0,7)
    print("第"+str(res+1)+"个硬币是假的！")
    
main()

        
                
