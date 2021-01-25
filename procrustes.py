"""
Procrustes analysis with Python
https://en.wikipedia.org/wiki/Procrustes_analysis
"""

# Get [proper] multi-dimensional array support
import numpy as np

# Ordinary Procrustes Analysis (alignment to reference)
def opa(a, b):

	# Compute centroid (ori_avg/ori_len) 
	aT = a.mean(0)	
	bT = b.mean(0)

	# Translate point cloud around own origin (0)
	A = a - aT 
	B = b - bT

	# Compute quadratic mean of point cloud
	aS = np.sum(A * A)**.5	
	bS = np.sum(B * B)**.5

	# Get scale invariant unit vector (ori/ori_rms=0_to_1_rmsd_norm_coords) 
	A /= aS	
	B /= bS

	# Compute the covariance matrix from escalar product of sets
	C = np.dot(B.T, A)

	# Decompose point cloud into orthonormal bases (U, V being U transposed as in 'np.fliplr(np.rot90(U))') and singular values (S/_)
	U, _, V = np.linalg.svd(C)

	# Compute optimal rotation matrix from unitary matrices (left U and transposed right V singular vectors)
	aR = np.dot(U, V)

	# Enforce clockwise rotation matrix by disabling svd 'best-fit' reflections (the UV matrix R determinant should always be +1)
	if np.linalg.det(aR) < 0:

		# Flip sign on second row
		V[1] *= -1

		# Rebuild rotation matrix (no need to rerun if condition skipped)
		aR = np.dot(U, V)

	# Get scale multiplier factor so we can zoom in mutable shape into reference (rotation is already computed so we can leave the norm space)
	aS = aS / bS

	# Compute translation distance from mutable shape to reference (aT - bT_fitted_to_a_space)
	aT = aT - (bT.dot(aR) * aS)

	# Rotate mutable B unto fixed A (svd helps but the method for optimal rotation matrix U is Kabsch's)  
	B_ = B.dot(aR)

	# Compute Procrustes distance from RMSD (as per Kabsch 'A-BR' instead of dummy 'A-B')
	aD = (np.sum((A - B_)**2) / len(a))**.5

	# Output full rst transformation tuple and Kabsch RMSD
	return aR, aS, aT, aD 

# Generalized Procrustes Analysis (mean shape)
def gpa(v, n=-1):

	# Compute unknown mean shape prototype or fit everything to nth shape
	p = avg(v) if n < 0 else v[n]

	# Get shape collection length
	l = len(v)

	# Initialize storage arrays (one per shape)
	r, s, t, d = np.ndarray((4, l), object)

	# Get procrustes components for every shape against the reference (first one)
	for i in range(l):
		r[i], s[i], t[i], d[i] = opa(p, v[i]) 

	# Return per-shape transforms collection (including average shape and disparity)
	return r, s, t, d

# Average shape from n point clouds
def avg(v):

	# Make a shape collection copy (we don't want to overwrite the original data) while making sure is a well-formatted one (numpy)
	v = np.copy(v)

	# Get shape collection length
	l = len(v) 

	# Initialize storage arrays (one per shape) with type-agnostic lists for flexible assignment
	R, S, T = [list(np.zeros(l)) for _ in range(3)]

	# Avg 1/2 (sum): Iterate every possible match between shapes
	for i, j in np.ndindex(l, l):

		# Compute transform components for every permutation
		r, s, t, _ = opa(v[i], v[j]) 

		# Add up [A]ngle (scalar) from all [R]otations (matrix) carried against every other shape 
		R[j] += np.arccos(min(1,max(-1, np.trace(r[:1])))) * np.sign(r[1][0]) 			

		# Get combined scale and translation values for every shape
		S[j] += s 
		T[j] += t 

	# Avg 2/2 (div): Apply average transformations to shapes
	for i in range(l):

		# Average rotation 'theta' angle for every shape and rebuild rotation matrix
		a = R[i] / l
		r = [np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]

		# Transform shape collection (so we can compute the prototype average from it)
		v[i] = v[i].dot(r) * (S[i] / l) + (T[i] / l) 

	# Return components and shape prototype (useful as virtual reference) from 'procrustes mean' (shapes are optimally fitted so this is a safe estimation)
	return v.mean(0)
