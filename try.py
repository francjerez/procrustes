# Get direct script access (just for testing)
from procrustes import *

# Get unobtrusive plotting support
import matplotlib.pyplot as p; p.rcParams['toolbar'] = 'None';

# Preview n point clouds at once (first one to be marked as reference)
def show(o, e, b):

	# Format canvas
	p.figure(figsize=(10, 10), dpi=72, facecolor='w').add_axes([0.05, 0.05, 0.9, 0.9], aspect='equal')

	# Draw origin
	p.plot(0, 0, marker='x', mew=1, ms=10, c='g', zorder=2, clip_on=False)

	# Show RMSD (residuals sum)
	p.gcf().canvas.set_window_title('%f' % e)

	# Center shapes by fitting extremes to window bounds
	x = np.ravel(o[0].T[0])
	y = np.ravel(o[0].T[1])
	p.xlim(min(x), max(x)) 
	p.ylim(min(y), max(y))

	# Format data
	a = []
	for i, j in np.ndindex(len(o), 2):
		a.append(o[i].T[j])	

	# Draw data
	O = p.plot(*a, marker='x', mew=1, ms=10, lw=.25, c='b', zorder=0, clip_on=False)

	# Highlight references
	O[0].set(c='r', zorder=1)
	if not b:
		O[2].set_color('b')#r
		O[2].set_alpha(0.4)#r

	# Wait until pyplot window has been closed (we don't want a 'while True' interactive mode hack to unlock blocking)
	p.axis('off') 	
	p.show()

# Wikipedia 'fly wings' landmarks
arr1 = np.array([[588.0, 443.0], [178.0, 443.0], [56.0, 436.0], [50.0, 376.0], [129.0, 360.0], [15.0, 342.0], [92.0, 293.0], [79.0, 269.0], [276.0, 295.0], [281.0, 331.0], [785.0, 260.0], [754.0, 174.0], [405.0, 233.0], [386.0, 167.0], [466.0, 59.0]])
arr2 = np.array([[477.0, 557.0], [130.129, 374.307], [52.0, 334.0], [67.662, 306.953], [111.916, 323.0], [55.119, 275.854], [107.935, 277.723], [101.899, 259.73], [175.0, 329.0], [171.0, 345.0], [589.0, 527.0], [591.0, 468.0], [299.0, 363.0], [306.0, 317.0], [406.0, 288.0]])

# Ordinary Procrustes Analysis example
def demo_opa(a):
	r, s, t, d = opa(a[0], a[1])
	a[1] = a[1].dot(r) * s + t
	return a, d, False
show(*demo_opa([arr1, arr2, np.matrix.copy(arr2)]))

# Generalized Procrustes Analysis example
def demo_gpa(a):
	g = gpa(a, -1) 
	D = [avg(a)]
	for i in range(len(a)):
		D.append(a[i].dot(g[0][i]) * g[1][i] + g[2][i])
	return D, sum(g[3])/len(a), True 
show(*demo_gpa([arr1, arr2]))

