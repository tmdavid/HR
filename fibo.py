# Enter your code here. Read input from STDIN. Print output to STDOUT

prev = 0
current = 1


N = int(raw_input())
a = []
for i in range (N):
    a.append(int(raw_input()))

for i in range (N):
    result = 0
    prev = 0
    current = 1
    while result < a[i]:
        result = prev + current
        if(result == a[i]): 
            print "IsFibo"
            break
        prev = current
        current = result
    if(result>a[i]): print "IsNotFibo"
