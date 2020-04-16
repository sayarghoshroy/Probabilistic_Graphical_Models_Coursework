P_eh = {'l': 0.2, 'h': 0.8}

P_oil_eh = {'ll':0.9, 'hl':0.1, 'lh':0.05, 'hh':0.95}

P_bp_oil = {'lh': 0.1, 'nh': 0.4, 'hh': 0.5, 'll': 0.9, 'nl':0.1, 'hl': 0}

P_rt_infeh = {'lll':0.9, 'hll':0.1, 'llh':0.1, 'hlh':0.9, 'lhl':0.1, 'hhl':0.9, 'lhh':0.01, 'hhh':0.99}

P_inf_oileh = {'lll':0.9, 'hll':0.1, 'llh':0.1, 'hlh':0.9, 'lhl':0.1, 'hhl':0.9, 'lhh':0.01, 'hhh':0.99}

summer = ['l', 'h']

numer = denom = 0

for oil in summer:
	for eh in summer:
		prod = P_rt_infeh['hh'+eh]*P_inf_oileh['h'+oil+eh]*P_bp_oil['n'+oil]*P_oil_eh[oil+eh]*P_eh[eh]
		numer += prod

print("Numerator: " + str(numer))

for oil in summer:
	for eh in summer:
		for inf in summer:
			prod = P_rt_infeh['h'+inf+eh]*P_inf_oileh[inf+oil+eh]*P_bp_oil['n'+oil]*P_oil_eh[oil+eh]*P_eh[eh]
			print("term: " + str(prod) + "   " + inf + oil + eh)
			denom += prod

print("Denominator: " + str(denom))

print("Result: " + str(numer / denom))