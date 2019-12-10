#S
def SPath(n):
    cx = 0
    cy = 0
    path = []
    xincr = 1
    while(len(path) < n*n):
        path.append((cx, cy))
        cx = cx + xincr
        if(cx == n-1 or cx == 0):
            path.append((cx, cy))
            cy = cy +1
            xincr = -xincr
    
    return path

#Spiral
def SpiralPath(n):
    import numpy as np
    cx = 0
    cy = 0
    path = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    i = 0
    vis = np.zeros((n, n), dtype = bool)
    
    while(len(path) < n*n):
        vis[cx][cy] = True
        path.append((cx, cy))
        cx = cx + dx[i]
        cy = cy + dy[i]
        
        if(cx + dx[i] > n-1 or cx + dx[i] < 0 or cy + dy[i] > n-1 or cy + dy[i] < 0 or vis[cx+dx[i]][cy+dy[i]]):
            i = (i+1)%4
    
    return path
            
#QuarterSpiral
def QSpiralPath(n):
    cx = 0
    cy = 0
    path = []
    dx = [0, 1, 0, 1, 0, -1]
    dy = [1, 0, -1, 0, 1, 0]
    dist = [1, 1, 1, 1, 2, 2]
    curl = 1
    i = 0
    dleft = dist[i]
    
    while(len(path) < n*n):
        path.append((cx, cy))
        if(dleft > 0):
            cx = cx + dx[i]
            cy = cy + dy[i]
            dleft = dleft - 1
        elif(dleft == 0 and i != 5):
            i = i+1
            dleft = dist[i] - 1
            cx = cx + dx[i]
            cy = cy + dy[i]
        else:
            i = 0
            curl = curl + 1
            dist = [1, curl, curl, 1, curl+1, curl+1]
            dleft = dist[i] - 1
            cx = cx + dx[i]
            cy = cy + dy[i]
    
    return path

#Rowwise zigzag
def RowZigZagPath(n):
    cx = 0
    cy = 0
    path = []
    
    if(n%2 == 1):
        for j in range(int((n-1)/2)):
            if(j%2 == 0):
                dx = [0, 1, 0, 1]
                dy = [1, 0, -1, 0]
                for i in range(2*n-1):
                    path.append((cx, cy))
                    cx = cx + dx[i%4]
                    cy = cy + dy[i%4]
                path.append((cx, cy))
                cy = cy + 1
            else:
                dx = [0, -1, 0, -1]
                dy = [1, 0, -1, 0]
                for i in range(2*n-1):
                    path.append((cx, cy))
                    cx = cx + dx[i%4]
                    cy = cy + dy[i%4]
                path.append((cx, cy))
                cy = cy + 1
        
        if(cx == 0):
            while(cx != n-1):
                path.append((cx, cy))
                cx = cx + 1
            path.append((cx, cy))
        else:
            while(cx != 0):
                path.append((cx, cy))
                cx = cx - 1
            path.append((cx, cy))
    else:
        while(len(path) < n*n):
            dx = [0, 1, 0, 1]
            dy = [1, 0, -1, 0]
            i = 0
            while(cx < n-2):
                path.append((cx, cy))
                cx = cx + dx[i%4]
                cy = cy + dy[i%4]
                i = i + 1
            
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, 1]
            for j in range(4):
                path.append((cx, cy))
                cx = cx + dx[j]
                cy = cy + dy[j]
            
            if(len(path) == n*n):
                break;
            
            dx = [1, 0, -1, -1]
            dy = [0, 1, 0, 0]
            for j in range(4):
                path.append((cx, cy))
                cx = cx + dx[j]
                cy = cy + dy[j]
            
            dx = [0, -1, 0, -1]
            dy = [-1, 0, 1, 0]
            j = 0
            while(cx != 0):
                path.append((cx, cy))
                cx = cx + dx[j%4]
                cy = cy + dy[j%4]
                j = j + 1
            for j in range(2):
                path.append((cx, cy))
                cy = cy + 1
            
            if(len(path) == n*n):
                break;
    
    return path        
                
#util: euclidean distance
def Dist(p1, p2):
    return ( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )**0.5

#finding errors
def FindError(path):
    toterr = 0
    l = len(path)
    for i in range(l-1):
        for j in range(i+1, l):
            eudist = Dist(path[i], path[j])
            pdist = j-i
            toterr = toterr + abs(eudist - pdist)
        
    pairs = l*(l-1)/2
    avgerr = toterr/pairs
    return avgerr

#errors for various sizes for all 3 - 2D return list - [0] is s, [1] is spiral, [2] is qspiral
def ErrorList(maxn):
    l = [[],[]]
    for i in range(2, maxn+1):
        #l[0].append(FindError(SPath(i)))
        #l[1].append(FindError(SpiralPath(i)))
        l[0].append(FindError(QSpiralPath(i)))
        l[1].append(FindError(RowZigZagPath(i)))
    return l