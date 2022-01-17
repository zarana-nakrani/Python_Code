#import array as arr
# Enter your code here. Read input from STDIN. Print output to STDOUT
def No_Idea(lst,a,b):
    happiness = 0 
    for i in lst:
        if i in a:
            happiness+=1
        elif i in b:
            happiness-=1
        else:
            pass
    return happiness
#reading input
if __name__ == "__main__":
    n,m = input().split(" ")
    lst = list(map(int, input().split(" ")))
    a = set(map(int, (input().split(" "))))
    b = set(map(int,input().split(" ")))
    # print(lst)
    # print(a)
    # print(b)
    print(No_Idea(lst,a,b))
    
