# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    l = []
    
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i+j+k != n:
                    l1 = []
                    l1.append(i)
                    l1.append(j)
                    l1.append(k)
                    l.append(l1)
                    
    print(l)