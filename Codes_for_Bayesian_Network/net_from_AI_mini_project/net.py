def D(str):
	# CPT Table for Variable D
	if(str == '0'):
		return 0.1
	elif(str == '1 or 2'):
		return 0.7
	return 0.2

def Ex(str):
	# CPT Table for Variable Ex
	if(str == 'True'):
		return 0.3
	return 0.7

def Q(str):
	# CPT Table for Variable Q
	if(str == '0'):
		return 0.6
	elif(str == '1'):
		return 0.3
	return 0.1

def Ev(str):
	# CPT Table for Variable Ev
	if(str == 'True'):
		return 0.7
	return 0.3

def Te(str):
	# CPT Table for Variable Te
	if(str == 'True'):
		return 0.75
	return 0.25

def H(str):
	# CPT Table for Variable H
	if(str == '0'):
		return 0.7
	elif(str == '1'):
		return 0.28
	return 0.02

def F(tup, str):
	# CPT Table for Variable F
	if(str == 'Negligible'):
		if(tup == ('True')):
			return 0.95
		return 0.25

	if(tup == ('True')):
		return 0.05
	return 0.75

def T(tup, str):
	# CPT Table for Variable T
	if(str == '< 6 hrs'):
		if(tup ==('Low', '0')):
			return 0.6
		if(tup ==('Low', '1')):
			return 0.55
		if(tup ==('Low', '2')):
			return 0.5
		if(tup ==('Average', '0')):
			return 0.85
		if(tup ==('Average', '1')):
			return 0.8
		if(tup ==('Average', '2')):
			return 0.75
		if(tup ==('High', '0')):
			return 0.99
		if(tup ==('High', '1')):
			return 0.95
		if(tup ==('High', '2')):
			return 0.9

	elif(str == '6 to 12 hrs'):
		if(tup ==('Low', '0')):
			return 0.3
		if(tup ==('Low', '1')):
			return 0.33
		if(tup ==('Low', '2')):
			return 0.35
		if(tup ==('Average', '0')):
			return 0.1
		if(tup ==('Average', '1')):
			return 0.12
		if(tup ==('Average', '2')):
			return 0.15
		if(tup ==('High', '0')):
			return 0.009
		if(tup ==('High', '1')):
			return 0.04
		if(tup ==('High', '2')):
			return 0.08

	if(tup ==('Low', '0')):
		return 0.1
	if(tup ==('Low', '1')):
		return 0.12
	if(tup ==('Low', '2')):
		return 0.15
	if(tup ==('Average', '0')):
		return 0.05
	if(tup ==('Average', '1')):
		return 0.08
	if(tup ==('Average', '2')):
		return 0.1
	if(tup ==('High', '0')):
		return 0.001
	if(tup ==('High', '1')):
		return 0.01
	if(tup ==('High', '2')):
		return 0.02

def B(tup, str):
	# CPT Table for Variable B

	if(str == '1'):
		if (tup == ('Negligible', '< 6 hrs') ):
			return 0.1
		if (tup == ('Negligible', '6 to 12 hrs') ):
			return 0.3
		if (tup == ('Negligible', '> 12 hrs') ):
			return 0.7
		if (tup == ('Substantial', '< 6 hrs') ):
			return 0.01
		if (tup == ('Substantial', '6 to 12 hrs') ):
			return 0.05
		if (tup == ('Substantial', '> 12 hrs') ):
			return 0.1

	if(str == '2'):
		if (tup == ('Negligible', '< 6 hrs') ):
			return 0.2
		if (tup == ('Negligible', '6 to 12 hrs') ):
			return 0.3
		if (tup == ('Negligible', '> 12 hrs') ):
			return 0.2
		if (tup == ('Substantial', '< 6 hrs') ):
			return 0.04
		if (tup == ('Substantial', '6 to 12 hrs') ):
			return 0.15
		if (tup == ('Substantial', '> 12 hrs') ):
			return 0.3

	if (tup == ('Negligible', '< 6 hrs') ):
		return 0.7
	if (tup == ('Negligible', '6 to 12 hrs') ):
		return 0.4
	if (tup == ('Negligible', '> 12 hrs') ):
		return 0.1
	if (tup == ('Substantial', '< 6 hrs') ):
		return 0.95
	if (tup == ('Substantial', '6 to 12 hrs') ):
		return 0.8
	else:
		return 0.6

def W(tup, str):
	# CPT Table for Variable W
	if(str == 'Low'):
		if ( tup == ( '0', 'True', '0', 'True' ) ):
			return 0.166
		if ( tup == ( '0', 'True', '0', 'False' ) ):
			return 0.227
		if ( tup == ( '0', 'True', '1', 'True' ) ):
			return 0.141
		if ( tup == ( '0', 'True', '1', 'False' ) ):
			return 0.203
		if ( tup == ( '0', 'True', '> 2', 'True' ) ):
			return 0.110
		if ( tup == ( '0', 'True', '> 2', 'False' ) ):
			return 0.178
		if ( tup == ( '0', 'False', '0', 'True' ) ):
			return 0.289
		if ( tup == ( '0', 'False', '0', 'False' ) ):
			return 0.35
		if ( tup == ( '0', 'False', '1', 'True' ) ):
			return 0.264
		if ( tup == ( '0', 'False', '1', 'False' ) ):
			return 0.325
		if ( tup == ( '0', 'False', '> 2', 'True' ) ):
			return 0.239
		if ( tup == ( '0', 'False', '> 2', 'False' ) ):
			return 0.301
		if ( tup == ( '1 or 2', 'True', '0', 'True' ) ):
			return 0.129
		if ( tup == ( '1 or 2', 'True', '0', 'False' ) ):
			return 0.19
		if ( tup == ( '1 or 2', 'True', '1', 'True' ) ):
			return 0.104
		if ( tup == ( '1 or 2', 'True', '1', 'False' ) ):
			return 0.166
		if ( tup == ( '1 or 2', 'True', '> 2', 'True' ) ):
			return 0.08
		if ( tup == ( '1 or 2', 'True', '> 2', 'False' ) ):
			return 0.141
		if ( tup == ( '1 or 2', 'False', '0', 'True' ) ):
			return 0.250
		if ( tup == ( '1 or 2', 'False', '0', 'False' ) ):
			return 0.313
		if ( tup == ( '1 or 2', 'False', '1', 'True' ) ):
			return 0.227
		if ( tup == ( '1 or 2', 'False', '1', 'False' ) ):
			return 0.289
		if ( tup == ( '1 or 2', 'False', '> 2', 'True' ) ):
			return 0.203
		if ( tup == ( '1 or 2', 'False', '> 2', 'False' ) ):
			return 0.264
		if ( tup == ( '> 3', 'True', '0', 'True' ) ):
			return 0.055
		if ( tup == ( '> 3', 'True', '0', 'False' ) ):
			return 0.113
		if ( tup == ( '> 3', 'True', '1', 'True' ) ):
			return 0.031
		if ( tup == ( '> 3', 'True', '1', 'False' ) ):
			return 0.092
		if ( tup == ( '> 3', 'True', '> 2', 'True' ) ):
			return 0.006
		if ( tup == ( '> 3', 'True', '> 2', 'False' ) ):
			return 0.068
		if ( tup == ( '> 3', 'False', '0', 'True' ) ):
			return 0.178
		if ( tup == ( '> 3', 'False', '0', 'False' ) ):
			return 0.239
		if ( tup == ( '> 3', 'False', '1', 'True' ) ):
			return 0.154
		if ( tup == ( '> 3', 'False', '1', 'False' ) ):
			return 0.215
		if ( tup == ( '> 3', 'False', '> 2', 'True' ) ):
			return 0.129
		if ( tup == ( '> 3', 'False', '> 2', 'False' ) ):
			return 0.19

	if(str == 'Average'):
		if ( tup == ( '0', 'True', '0', 'True' ) ):
			return 0.308
		if ( tup == ( '0', 'True', '0', 'False' ) ):
			return 0.422
		if ( tup == ( '0', 'True', '1', 'True' ) ):
			return 0.262
		if ( tup == ( '0', 'True', '1', 'False' ) ):
			return 0.376
		if ( tup == ( '0', 'True', '> 2', 'True' ) ):
			return 0.217
		if ( tup == ( '0', 'True', '> 2', 'False' ) ):
			return 0.331
		if ( tup == ( '0', 'False', '0', 'True' ) ):
			return 0.536
		if ( tup == ( '0', 'False', '0', 'False' ) ):
			return 0.65
		if ( tup == ( '0', 'False', '1', 'True' ) ):
			return 0.49
		if ( tup == ( '0', 'False', '1', 'False' ) ):
			return 0.604
		if ( tup == ( '0', 'False', '> 2', 'True' ) ):
			return 0.445
		if ( tup == ( '0', 'False', '> 2', 'False' ) ):
			return 0.559
		if ( tup == ( '1 or 2', 'True', '0', 'True' ) ):
			return 0.239
		if ( tup == ( '1 or 2', 'True', '0', 'False' ) ):
			return 0.354
		if ( tup == ( '1 or 2', 'True', '1', 'True' ) ):
			return 0.194
		if ( tup == ( '1 or 2', 'True', '1', 'False' ) ):
			return 0.308
		if ( tup == ( '1 or 2', 'True', '> 2', 'True' ) ):
			return 0.148
		if ( tup == ( '1 or 2', 'True', '> 2', 'False' ) ):
			return 0.262
		if ( tup == ( '1 or 2', 'False', '0', 'True' ) ):
			return 0.468
		if ( tup == ( '1 or 2', 'False', '0', 'False' ) ):
			return 0.582
		if ( tup == ( '1 or 2', 'False', '1', 'True' ) ):
			return 0.422
		if ( tup == ( '1 or 2', 'False', '1', 'False' ) ):
			return 0.536
		if ( tup == ( '1 or 2', 'False', '> 2', 'True' ) ):
			return 0.376
		if ( tup == ( '1 or 2', 'False', '> 2', 'False' ) ):
			return 0.49
		if ( tup == ( '> 3', 'True', '0', 'True' ) ):
			return 0.103
		if ( tup == ( '> 3', 'True', '0', 'False' ) ):
			return 0.217
		if ( tup == ( '> 3', 'True', '1', 'True' ) ):
			return 0.057
		if ( tup == ( '> 3', 'True', '1', 'False' ) ):
			return 0.171
		if ( tup == ( '> 3', 'True', '> 2', 'True' ) ):
			return 0.011
		if ( tup == ( '> 3', 'True', '> 2', 'False' ) ):
			return 0.125
		if ( tup == ( '> 3', 'False', '0', 'True' ) ):
			return 0.331
		if ( tup == ( '> 3', 'False', '0', 'False' ) ):
			return 0.445
		if ( tup == ( '> 3', 'False', '1', 'True' ) ):
			return 0.285
		if ( tup == ( '> 3', 'False', '1', 'False' ) ):
			return 0.399
		if ( tup == ( '> 3', 'False', '> 2', 'True' ) ):
			return 0.239
		if ( tup == ( '> 3', 'False', '> 2', 'False' ) ):
			return 0.354

	else:
		if ( tup == ( '0', 'True', '0', 'True' ) ):
			return 0.526
		if ( tup == ( '0', 'True', '0', 'False' ) ):
			return 0.351
		if ( tup == ( '0', 'True', '1', 'True' ) ):
			return 0.596
		if ( tup == ( '0', 'True', '1', 'False' ) ):
			return 0.421
		if ( tup == ( '0', 'True', '> 2', 'True' ) ):
			return 0.667
		if ( tup == ( '0', 'True', '> 2', 'False' ) ):
			return 0.491
		if ( tup == ( '0', 'False', '0', 'True' ) ):
			return 0.175
		if ( tup == ( '0', 'False', '0', 'False' ) ):
			return 0
		if ( tup == ( '0', 'False', '1', 'True' ) ):
			return 0.246
		if ( tup == ( '0', 'False', '1', 'False' ) ):
			return 0.07
		if ( tup == ( '0', 'False', '> 2', 'True' ) ):
			return 0.316
		if ( tup == ( '0', 'False', '> 2', 'False' ) ):
			return 0.14
		if ( tup == ( '1 or 2', 'True', '0', 'True' ) ):
			return 0.632
		if ( tup == ( '1 or 2', 'True', '0', 'False' ) ):
			return 0.456
		if ( tup == ( '1 or 2', 'True', '1', 'True' ) ):
			return 0.702
		if ( tup == ( '1 or 2', 'True', '1', 'False' ) ):
			return 0.526
		if ( tup == ( '1 or 2', 'True', '> 2', 'True' ) ):
			return 0.772
		if ( tup == ( '1 or 2', 'True', '> 2', 'False' ) ):
			return 0.596
		if ( tup == ( '1 or 2', 'False', '0', 'True' ) ):
			return 0.281
		if ( tup == ( '1 or 2', 'False', '0', 'False' ) ):
			return 0.105
		if ( tup == ( '1 or 2', 'False', '1', 'True' ) ):
			return 0.351
		if ( tup == ( '1 or 2', 'False', '1', 'False' ) ):
			return 0.175
		if ( tup == ( '1 or 2', 'False', '> 2', 'True' ) ):
			return 0.421
		if ( tup == ( '1 or 2', 'False', '> 2', 'False' ) ):
			return 0.246
		if ( tup == ( '> 3', 'True', '0', 'True' ) ):
			return 0.842
		if ( tup == ( '> 3', 'True', '0', 'False' ) ):
			return 0.667
		if ( tup == ( '> 3', 'True', '1', 'True' ) ):
			return 0.912
		if ( tup == ( '> 3', 'True', '1', 'False' ) ):
			return 0.737
		if ( tup == ( '> 3', 'True', '> 2', 'True' ) ):
			return 0.982
		if ( tup == ( '> 3', 'True', '> 2', 'False' ) ):
			return 0.807
		if ( tup == ( '> 3', 'False', '0', 'True' ) ):
			return 0.491
		if ( tup == ( '> 3', 'False', '0', 'False' ) ):
			return 0.316
		if ( tup == ( '> 3', 'False', '1', 'True' ) ):
			return 0.561
		if ( tup == ( '> 3', 'False', '1', 'False' ) ):
			return 0.386
		if ( tup == ( '> 3', 'False', '> 2', 'True' ) ):
			return 0.632
		else:
			return 0.456

def domain(str):
	if(str == 'D'):
		return ['0', '1 or 2', '> 3']
	if(str == 'Ex'):
		return ['True', 'False']
	if(str == 'Q'):
		return ['0', '1', '> 2']
	if(str == 'Ev'):
		return ['True', 'False']
	if(str == 'Te'):
		return ['True', 'False']
	if(str == 'W'):
		return ['Low', 'Average', 'High']
	if(str == 'H'):
		return ['0', '1', '2']
	if(str == 'F'):
		return ['Negligible', 'Substantial']
	if(str == 'T'):
		return ['< 6 hrs', '6 to 12 hrs', '> 12 hrs']
	if(str == 'B'):
		return ['1', '2', '3' ]

summing = 0
for b in domain('B'):
	for d in domain('D'):
		for ex in domain('Ex'):
			for q in domain('Q'):
				for ev in domain('Ev'):
					for w in domain('W'):
						for h in domain('H'):
							for t in domain('T'):
								summing = summing + (float)(F(('True'), 'Negligible') * Te('True') * D(d) * Ex(ex) * Q(q) * Ev(ev) * B(('Negligible', t), b) * W( (d, ex, q, ev), w) * H(h) * T((w, h), t))

sum_num = 0
b = '1'

for d in domain('D'):
	for ex in domain('Ex'):
		for q in domain('Q'):
			for ev in domain('Ev'):
				for w in domain('W'):
					for h in domain('H'):
						for t in domain('T'):
							sum_num = sum_num + (float)(F(('True'), 'Negligible') * Te('True') * D(d) * Ex(ex) * Q(q) * Ev(ev) * B(('Negligible', t), b) * W( (d, ex, q, ev), w) * H(h) * T((w, h), t))

print("Required Probability = ", (sum_num / summing))