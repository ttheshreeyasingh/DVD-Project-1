import pandas as pd

def round_nearest_05(x):
	return round(x * 20) / 20

def single_nmos(vdd, A):
    Isub = 0 
    Ib = 0
    Ig = 0 
    LeakagePower = 0
    
    if A == 0:
        nmos_off = pd.read_csv('./NMOS_Single/nmos_off.csv')
        row = nmos_off.loc[(nmos_off['Vdd'] == vdd)]
        Igate = abs(row.iloc[0]['Igate'])
        Isub = abs(row.iloc[0]['Isource'])
        Ib = abs(row.iloc[0]['Ibody'])
    elif A == 1:
        nmos_on = pd.read_csv('./NMOS_Single/nmos_on.csv')
        row = nmos_on.loc[(nmos_on['Vdd'] == vdd)]
        Igate = abs(row.iloc[0]['Igate'])
        Ib = abs(row.iloc[0]['Ibody'])
        Isub = 0
    else:
        print("Incorrect Input Level")
        
    LeakagePower = vdd * (Isub + Igate + Ib)    
    return LeakagePower, Isub, Ib, Igate

def single_pmos(vdd, A):
    Isub = 0 
    Ib = 0
    Ig = 0 
    LeakagePower = 0
    
    if A == 1:
        nmos_off = pd.read_csv('./NMOS_Single/nmos_off.csv')
        row = nmos_off.loc[(nmos_off['Vdd'] == vdd)]
        Igate = abs(row.iloc[0]['Igate'])
        Isub = abs(row.iloc[0]['Isource'])
        Ib = abs(row.iloc[0]['Ibody'])
    elif A == 0:
        nmos_on = pd.read_csv('./NMOS_Single/nmos_on.csv')
        row = nmos_on.loc[(nmos_on['Vdd'] == vdd)]
        Igate = abs(row.iloc[0]['Igate'])
        Ib = abs(row.iloc[0]['Ibody'])
        Isub = 0
    else:
        print("Incorrect Input Level")
        
    LeakagePower = vdd * (Isub + Igate + Ib)    
    return LeakagePower, Isub, Ib, Igate

def stack_nmos(B, A):
	Isub=0 
	Ib=0
	Ig=0 
	LeakagePower=0
	nmos_stack=pd.read_csv('./NMOS_Stack/nmos_stack.csv')
	if (A == 0 & B == 0) or (A == 0 & B == 1):
		row = nmos_stack.loc[(nmos_stack['Va'] == A*1.1) & (nmos_stack['Vb'] == B*1.1)]
		Vx = round_nearest_05(abs(row.iloc[0]['Vx']))
		LeakagePowera, Isuba, Iba, Iga = single_nmos(Vx, A)
		LeakagePowerb, Isubb, Ibb, Igb = single_nmos(round_nearest_05((1.1-Vx)), B)
	else:
		LeakagePowera, Isuba, Iba, Iga = single_nmos(1.1, A)
		LeakagePowerb, Isubb, Ibb, Igb = single_nmos(1.1, B)
	
	LeakagePower = LeakagePowera + LeakagePowerb
	Isub = Isuba + Isubb
	Ib = Iba + Ibb
	Ig = Iga + Igb	
	
	return LeakagePower, Isub, Ib, Ig

def stack_pmos(B, A):
	Isub=0 
	Ib=0
	Ig=0 
	LeakagePower=0
	pmos_stack=pd.read_csv('./PMOS_Stack/pmos_stack.csv')
	if (A == 0 & B == 0) or (A == 0 & B == 1):
		LeakagePowera, Isuba, Iba, Iga = single_pmos(1.1, A)
		LeakagePowerb, Isubb, Ibb, Igb = single_pmos(1.1, B)
	else:
		row = pmos_stack.loc[(pmos_stack['Va'] == A*1.1) & (pmos_stack['Vb'] == B*1.1)]
		Vx = round_nearest_05(abs(row.iloc[0]['Vx']))
		LeakagePowera, Isuba, Iba, Iga = single_pmos(round_nearest_05((1.1-Vx)), A)
		LeakagePowerb, Isubb, Ibb, Igb = single_pmos(Vx , B)
	
	LeakagePower = LeakagePowera + LeakagePowerb
	Isub = Isuba + Isubb
	Ib = Iba + Ibb
	Ig = Iga + Igb	
	
	return LeakagePower, Isub, Ib, Ig
	
def inv(A):
	Isub=0 
	Ib=0
	Ig=0 
	LeakagePower=0
	
	LeakagePowerp, Isubp, Ibp, Igp = single_pmos(1.1, A)
	LeakagePowern, Isubn, Ibn, Ign = single_nmos(1.1, A)
	
	LeakagePower = LeakagePowerp + LeakagePowern
	Isub = Isubp + Isubn
	Ib = Ibp + Ibn
	Ig = Igp + Ign
	
	return LeakagePower, Isub, Ib, Ig
	
def nand2(A, B):
	Isub=0 
	Ib=0
	Ig=0 
	LeakagePower=0
	
	LeakagePowerp1, Isubp1, Ibp1, Igp1 = single_pmos(1.1, A)
	LeakagePowerp2, Isubp2, Ibp2, Igp2 = single_pmos(1.1, B)
	LeakagePowern, Isubn, Ibn, Ign = stack_nmos(A, B)
	
	LeakagePower = LeakagePowerp1 + LeakagePowerp2 + LeakagePowern
	Isub = Isubp1 + Isubp2 + Isubn
	Ib = Ibp1 + Ibp2 + Ibn
	Ig = Igp1 + Igp2 + Ign
	
	return LeakagePower, Isub, Ib, Ig

def nor2(A, B):
	Isub = 0
	Ib = 0
	Ig = 0
	LeakagePower = 0
	
	LeakagePowern1, Isubn1, Ibn1, Ign1 = single_nmos(1.1, A)
	LeakagePowern2, Isubn2, Ibn2, Ign2 = single_nmos(1.1, B)
	LeakagePowerp, Isubp, Ibp, Igp = stack_pmos(A, B)
    
	LeakagePower = LeakagePowern1 + LeakagePowern2 + LeakagePowerp
	Isub = Isubn1 + Isubn2 + Isubp
	Ib = Ibn1 + Ibn2 + Ibp
	Ig = Ign1 + Ign2 + Igp
	
	return LeakagePower, Isub, Ib, Ig
	
def and2(A, B):
	Isub=0 
	Ib=0
	Ig=0 
	LeakagePower=0
	
	LeakagePower_nand, Isub_nand, Ib_nand, Ig_nand = nand2(A, B)
	if A == 1 & B == 1:
		LeakagePower_inv, Isub_inv, Ib_inv, Ig_inv = inv(0)
	else:
		LeakagePower_inv, Isub_inv, Ib_inv, Ig_inv = inv(1)
	
	LeakagePower = LeakagePower_nand + LeakagePower_inv
	Isub = Isub_nand + Isub_inv
	Ib = Ib_nand + Ib_inv
	Ig = Ig_nand + Ig_inv
	
	return LeakagePower, Isub, Ib, Ig

def or2(A, B):
	Isub=0 
	Ib=0
	Ig=0 
	LeakagePower=0
	
	LeakagePower_nor, Isub_nor, Ib_nor, Ig_nor = nor2(A, B)
	if (A == 1 | B == 1):
		LeakagePower_inv, Isub_inv, Ib_inv, Ig_inv = inv(0)
	else:
		LeakagePower_inv, Isub_inv, Ib_inv, Ig_inv = inv(1)
	
	LeakagePower = LeakagePower_nor + LeakagePower_inv
	Isub = Isub_nor + Isub_inv
	Ib = Ib_nor + Ib_inv
	Ig = Ig_nor + Ig_inv
	
	return LeakagePower, Isub, Ib, Ig

def and3(A, B, C):
	Isub=0 
	Ib=0
	Ig=0 
	LeakagePower=0
	
	LeakagePower_and1, Isub_and1, Ib_and1, Ig_and1 = and2(A, B)
	LeakagePower_and2, Isub_and2, Ib_and2, Ig_and2 = and2(C, A*B)
	
	LeakagePower = LeakagePower_and1 + LeakagePower_and2
	Isub = Isub_and1 + Isub_and2
	Ib = Ib_and1 + Ib_and2
	Ig = Ig_and1 + Ig_and2
	
	return LeakagePower, Isub, Ib, Ig

def or3(A, B, C):
	Isub=0 
	Ib=0
	Ig=0 
	LeakagePower=0
	
	LeakagePower_or1, Isub_or1, Ib_or1, Ig_or1 = or2(A, B)
	LeakagePower_or2, Isub_or2, Ib_or2, Ig_or2 = or2(C, max(A,B))
	
	LeakagePower = LeakagePower_or1 + LeakagePower_or2
	Isub = Isub_or1 + Isub_or2
	Ib = Ib_or1 + Ib_or2
	Ig = Ig_or1 + Ig_or2
	
	return LeakagePower, Isub, Ib, Ig
	
def and4(A, B, C, D):
	Isub=0 
	Ib=0
	Ig=0 
	LeakagePower=0
	
	LeakagePower_and1, Isub_and1, Ib_and1, Ig_and1 = and2(A, B)
	LeakagePower_and2, Isub_and2, Ib_and2, Ig_and2 = and2(C, D)
	LeakagePower_and3, Isub_and3, Ib_and3, Ig_and3 = and2(A*B, C*D)
	
	LeakagePower = LeakagePower_and1 + LeakagePower_and2 + LeakagePower_and3
	Isub = Isub_and1 + Isub_and2 + Isub_and3
	Ib = Ib_and1 + Ib_and2 + Ib_and3
	Ig = Ig_and1 + Ig_and2 + Ig_and3
	
	return LeakagePower, Isub, Ib, Ig

def or4(A, B, C, D):
	Isub=0 
	Ib=0
	Ig=0 
	LeakagePower=0
	
	LeakagePower_or1, Isub_or1, Ib_or1, Ig_or1 = or2(A, B)
	LeakagePower_or2, Isub_or2, Ib_or2, Ig_or2 = or2(C, D)
	LeakagePower_or3, Isub_or3, Ib_or3, Ig_or3 = or2(max(A,B), max(C,D))
	
	LeakagePower = LeakagePower_or1 + LeakagePower_or2 + LeakagePower_or3
	Isub = Isub_or1 + Isub_or2 + Isub_or3
	Ib = Ib_or1 + Ib_or2 + Ib_or3
	Ig = Ig_or1 + Ig_or2 + Ig_or3
	
	return LeakagePower, Isub, Ib, Ig

def nor3(A, B, C):
	Isub=0 
	Ib=0
	Ig=0 
	LeakagePower=0
	
	LeakagePower_or, Isub_or, Ib_or, Ig_or = or3(A, B, C)
	if (A == 1 | B == 1 | C == 1):
		LeakagePower_inv, Isub_inv, Ib_inv, Ig_inv = inv(1)
	else:
		LeakagePower_inv, Isub_inv, Ib_inv, Ig_inv = inv(0)

	LeakagePower = LeakagePower_or + LeakagePower_inv
	Isub = Isub_or + Isub_inv
	Ib = Ib_or + Ib_inv
	Ig = Ig_or + Ig_inv

	return LeakagePower, Isub, Ib, Ig

def nor4(A, B, C, D):
	Isub=0 
	Ib=0
	Ig=0 
	LeakagePower=0
	
	LeakagePower_or, Isub_or, Ib_or, Ig_or = or4(A, B, C, D)
	if (A == 1 | B == 1 | C == 1 | D == 1):
		LeakagePower_inv, Isub_inv, Ib_inv, Ig_inv = inv(1)
	else:
		LeakagePower_inv, Isub_inv, Ib_inv, Ig_inv = inv(0)

	LeakagePower = LeakagePower_or + LeakagePower_inv
	Isub = Isub_or + Isub_inv
	Ib = Ib_or + Ib_inv
	Ig = Ig_or + Ig_inv

	return LeakagePower, Isub, Ib, Ig

def ISCAS_74182(P3,P2,P1,P0,G3,G2,G1,G0,Cn):

	LeakagePower0,Isub0,Ib0,Ig0 = inv(Cn)
	Cn_inv = 1-Cn

	LeakagePower1,Isub1,Ib1,Ig1 = or4(P3,P2,P1,P0)

	LeakagePower2,Isub2,Ib2,Ig2 = and4(G0,G1,G2,G3)
	LeakagePower3,Isub3,Ib3,Ig3 = and4(P1,G3,G2,G1)
	LeakagePower4,Isub4,Ib4,Ig4 = and4(G2,G1,G0,Cn_inv)
	LeakagePower5,Isub5,Ib5,Ig5 = and4(P0,G2,G1,G0)

	LeakagePower6,Isub6,Ib6,Ig6 = and3(P2,G3,G2)
	LeakagePower7,Isub7,Ib7,Ig7 = and3(P1,G2,G1)
	LeakagePower8,Isub8,Ib8,Ig8 = and3(G1,G0,Cn_inv)
	LeakagePower9,Isub9,Ib9,Ig9 = and3(P0,G1,G0)

	LeakagePower10,Isub10,Ib10,Ig10 = and2(P3,G3)
	LeakagePower11,Isub11,Ib11,Ig11 = and2(P2,G2)
	LeakagePower12,Isub12,Ib12,Ig12 = and2(P1,G1)
	LeakagePower13,Isub13,Ib13,Ig13 = and2(G0,Cn_inv)
	LeakagePower14,Isub14,Ib14,Ig14 = and2(P0,G0)

	LeakagePower15,Isub15,Ib15,Ig15 = or4(G0&G1&G2&G3,P1&G3&G2&G1,P2&G3&G2,P3&G3)
	LeakagePower16,Isub16,Ib16,Ig16 = nor4(G2&G1&G0&(Cn_inv),P0&G2&G1&G0,P1&G2&G1,P2&G2)
	LeakagePower17,Isub17,Ib17,Ig17 = nor3(G1&G0&(Cn_inv),P0&G1&G0,P1&G1)
	LeakagePower18,Isub18,Ib18,Ig18 = nor2(G0&(Cn_inv),P0&G0)

	LeakagePower = LeakagePower0 + LeakagePower1 + LeakagePower2 + LeakagePower3 + LeakagePower4 + LeakagePower5 + LeakagePower6 + LeakagePower7 + LeakagePower8 + LeakagePower9 + LeakagePower10 + LeakagePower11 + LeakagePower12 + LeakagePower13 + LeakagePower14 + LeakagePower15 + LeakagePower16 + LeakagePower17 + LeakagePower18
	Isub = Isub0 + Isub1 + Isub2 + Isub3 + Isub4 + Isub5 + Isub6 + Isub7 + Isub8 + Isub9 + Isub10 + Isub11 + Isub12 + Isub13 + Isub14 + Isub15 + Isub16 + Isub17 + Isub18
	Ib = Ib0 + Ib1 + Ib2 + Ib3 + Ib4 + Ib5 + Ib6 + Ib7 + Ib8 + Ib9 + Ib10 + Ib11 + Ib12 + Ib13 + Ib14 + Ib15 + Ib16 + Ib17 + Ib18
	Ig = Ig0 + Ig1 + Ig2 + Ig3 + Ig4 + Ig5 + Ig6 + Ig7 + Ig8 + Ig9 + Ig10 + Ig11 + Ig12 + Ig13 + Ig14 + Ig15 + Ig16 + Ig17 + Ig18

	return LeakagePower, Isub, Ib, Ig

P3 = int(input("Enter the value of P3: "))
P2 = int(input("Enter the value of P2: "))
P1 = int(input("Enter the value of P1: "))
P0 = int(input("Enter the value of P0: "))
G3 = int(input("Enter the value of G3: "))
G2 = int(input("Enter the value of G2: "))
G1 = int(input("Enter the value of G1: "))
G0 = int(input("Enter the value of G0: "))
Cn = int(input("Enter the value of Cn: "))

LeakagePower, Isub, Ib, Ig = ISCAS_74182(P3,P2,P1,P0,G3,G2,G1,G0,Cn)

print("Leakage Power: ", LeakagePower, "W.")
print("Subthreshold Current: ", Isub, "A.")
print("Ib: ", Ib)
print("Ig: ", Ig)