#The formula is hereby transformed into python (Fully written by Lau Long Yat Damian)
#functional without importing numpy (To demonstrate its efficency without external libraries)
#covering all 2x2 matrices that have 2 or 4 distinct roots
#glitches may occur in the program, it is therefore suggested to use the formulas by hand

M=[0,0],[0,0]
P=[0,0],[0,0]
#The matrix P here is to save the original data from matrix M to find the 2nd pair of roots

for i in range (0,2):
    for j in range (0,2):
        print("Row", str(i+1), "Column", str(j+1))
        M[i][j]=float(input("= "))
for i in range (0,2):
    print(M[i])

def case1a(i):
    r=(P[0][1]*P[1][0]+(1-2*i)*a*det**0.5)/(P[1][1]**2-det)
    M[1][1]=(a/(r**2-1))**0.5
    M[0][0]=r*M[1][1]
    b=((r-1)/(a*(1+r)))**0.5
    for j in range (0,2):
        M[j][1-j]=P[j][1-j]*b
        print(M[j])

def case1b(i):
    r=(P[0][1]*P[1][0]+(1-2*i)*a*det**0.5)/(P[0][0]**2-det)
    M[0][0]=(a/(1-r**2))**0.5
    M[1][1]=r*M[0][0]
    b=((1-r)/(a*(1+r)))**0.5
    for j in range (0,2):
        M[j][1-j]=P[j][1-j]*b
        print(M[j])

def case1c(i):
    M[i][i]=0
    M[1-i][1-i]=(2*P[1-i][1-i])**(0.5)
    b=(2*P[1-i][1-i])**(-0.5)
    for j in range (0,2):
        M[j][1-j]=P[j][1-j]*b
        print(M[j])

def case2(i):
    p=P[1][1]+(1-2*i)*det**0.5
    if p!=0:
        for j in range(0,2):
            M[j][j]=(p/2)**0.5
            M[j][1-j]=P[j][1-j]*(2*p)**(-0.5)
            print(M[j])
    else:
        print("No solutions or only 1 pair of solution(Press 2 if you haven't pressed it)")
        
c=True
while c==True :
    
    det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    a=M[0][0]-M[1][1]
    d=2

    for i in range (0,2):
        for j in range (0,2):
            P[i][j]=M[i][j]

    print("The square root of the matrix is: ")
    for i in range (0,2):
        if d==2:
            if a!=0:
                if P[1][1]**2-det!=0:
                    case1a(i)
                elif P[0][0]**2-det!=0:
                    case1b(i)
                else:
                    case1c(i)
            elif P[0][0]!=0:
                case2(i)
            else:
                print("This program is not capable of computing nilpotent or zero matrices")
                d=-1
            if d!=-1:
                print("+/-")
                print("Type 0 to exit;")
                print("Type 1 to find the sq root of the above matrix;")
                if c==True:
                    print("Type 2 to get the another pair of the sq root")
                d=int(input("Please type the number: "))        
            c=False
            if d==2 and c==True:
                print(P)
                c=False
            elif d!=1 and d!=0:
                print("error")
                c=False
            elif d==1:      #iteration is being used here, just if you want to find M^(1/4), M^(1/8)...etc
                c=True
