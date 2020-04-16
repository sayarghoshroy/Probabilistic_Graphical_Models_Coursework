P_a = {'1': 0.01, '0': 0.99}
P_s = {'1': 0.5, '0': 0.5}

P_t_a = {'11': 0.05, '01': 0.95, '10': 0.01, '00': 0.99}

P_l_s = {'11': 0.1, '01': 0.9, '10': 0.01, '00': 0.99}

P_b_s = {'11': 0.6, '01': 0.4, '10': 0.3, '00': 0.7}

P_x_e = {'11': 0.98, '01': 0.02, '10': 0.05, '00': 0.95}

P_e_tl = {'100': 0, '000': 1, '110': 1, '010': 0, '101': 1, '001': 0, '111':1, '011': 0}

P_d_eb = {'100': 0.1, '000': 0.9, '110': 0.7, '010': 0.3, '101': 0.8, '001': 0.2, '111':0.9, '011': 0.1}

binary = ['0', '1']

sum = 0
for e in binary:
	for b in binary:
		for l in binary:
			for t in binary:
				for s in binary:
					for a in binary:
						prod = P_d_eb['1'+e+b] * P_e_tl[e+t+l] * P_b_s[b+s] * P_l_s[l+s] * P_t_a[t+a] * P_a[a] * P_s[s]
						sum += prod

print("P(d = true) = " + str(sum))

sum = 0
for e in binary:
	for b in binary:
		for l in binary:
			for t in binary:
				for s in ['1']:
					for a in binary:
						prod = P_d_eb['1'+e+b] * P_e_tl[e+t+l] * P_b_s[b+s] * P_l_s[l+s] * P_t_a[t+a] * P_a[a]
						sum += prod

print("P(d = true | s = true) = " + str(sum))


sum = 0
for e in binary:
	for b in binary:
		for l in binary:
			for t in binary:
				for s in ['0']:
					for a in binary:
						prod = P_d_eb['1'+e+b] * P_e_tl[e+t+l] * P_b_s[b+s] * P_l_s[l+s] * P_t_a[t+a] * P_a[a]
						sum += prod

print("P(d = true | s = false) = " + str(sum))