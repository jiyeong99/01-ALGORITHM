a = list(map(int,input().split()))
b = list(map(int,input().split()))
scoreA = 0
scoreB = 0
win = []
for i in range(10):
    A = a[i]
    B = b[i]
    if A > B:
        scoreA += 3
        win.append(['A',scoreA,scoreB])
    if B > A:
        scoreB += 3
        win.append(['B',scoreA,scoreB])
    if B == A:
        scoreA += 1
        scoreB += 1        
        win.append(['D',scoreA,scoreB])

print(scoreA,scoreB)

if scoreA > scoreB:
    print('A')
if scoreA < scoreB:
    print('B')
if scoreA == scoreB:
    if win[9][0] != win[8][0]:
        print('D')
    elif a == b:
        print('D')
    else:
        for i in win[::-1]:
            # print(i)
            if i[0] != 'D':
                print(i[0])
                break
