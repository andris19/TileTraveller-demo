
#Skilgreinum fasta
x_hnit,y_hnit = 1,1 

def hreyfa(x_hnit,y_hnit ,move):
    if loglegt_check(x_hnit,y_hnit,move) is True:
        if move == 'n':
            y_hnit += 1
        elif move =='s':
            y_hnit -= 1
        elif move =='e':
            x_hnit += 1
        else:
            x_hnit -= 1
    else:
        print("Not a valid direction!")
    return x_hnit,y_hnit


def loglegt_check(x,y,move):
    if x ==1 and y ==1:
        if move == 'n':
            return True
    elif x==1 and y==2:
        if move == 'n' or move ==  's' or move ==  'e':
            return True
    elif x==1 and y==3:
        if move == 's' or move ==  'e':
            return True
    elif x==2 and y==1:
        if move == 'n':
            return True
    elif x==2 and y==2:
        if move == 's' or move == 'w':
            return True
    elif x==2 and y==3:
        if move == 'w' or move ==  'e':
            return True
    elif x==3 and y==1:
        if move == 'n':
            return True
    elif x==3 and y==2:
        if move == 's' or move ==  'w':
            return True
    elif x==3 and y==3:
        if move == 'w' or move ==  's':
            return True
    return False

def sigur():
    if x_hnit == 3 and y_hnit == 1:
        return True
    else:
        return False



def moguleg_moves(x,y):
    if x == 1 and y ==1:
        print("You can travel: (N)orth")
    elif x== 1 and y ==2:
        print("You can travel: (N)orth or (E)ast or (S)outh")
    elif x== 1 and y ==3:
        print("You can travel: (E)ast or (S)outh")
    elif x== 2 and y ==1:
        print("You can travel: (N)orth")
    elif x== 2 and y ==2:
        print("You can travel: (S)outh or (W)est")
    elif x== 2 and y ==3:
        print("You can travel: (E)ast or (W)est")
    elif x== 3 and y ==3:
        print("You can travel: (S)outh or (W)est")
    elif x== 3 and y ==2:
        print("You can travel: (N)orth or (S)outh")
    else:
        pass
    


while 1:
    moguleg_moves(x_hnit,y_hnit) 
    print("Direction: ", end='')
    att = input().lower()
    x_hnit,y_hnit = hreyfa(x_hnit,y_hnit,att) 

    if sigur() is True:
        print("Victory!")
        break

    