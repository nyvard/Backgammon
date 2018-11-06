
"""
Use: f = features(board)
Input: board is is a 29-vector
Output: f is a 198-vector of features that follows Tesauro's procedure.
        See p. 423 in Sutton & Barto
"""
def features(board, player):
    f = np.zeros(198)
    
    # define features for points on board
    p = 0
    for i in range(1,25):
        point = board[i]
        print('point:', point)
        print('p: ', p)
        if (point != 0):
            print('Not 0')
            if(point > 0):
                if (point == 1):
                    f[p] = 1
                elif (point == 2):
                    f[p+1] = 1
                elif (point == 3):
                    f[p+2] = 1
                else:
                    f[p+3] = (point-3)/2
            else:
                if (point == -1):
                    f[p+4] == 1
                elif (point == -2):
                    f[p+5] = 1
                elif (point == -3):
                    f[p+6] = 1
                else:
                    f[p+7] = (-point-3)/2
        p += 8
    
    f[192] = board[25]/2
    f[193] = board[26]/2
    f[194] = board[27]/15
    f[195] = board[28]/15
    f[196] = int(player == 1)
    f[197] = int(player == -1)
    return f
    
    