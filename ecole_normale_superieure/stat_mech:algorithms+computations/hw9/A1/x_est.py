import random, math, pylab

def prob(x):
    s1 = math.exp(-(x + 1.2) ** 2 / 0.72)
    s2 = math.exp(-(x - 1.5) ** 2 / 0.08)
    return (s1 + 2.0 * s2) / math.sqrt(2.0 * math.pi)

delta = 10.0
nsteps = 10000000
acc_tot = 0
acc_tmp = 0
data = []
xaxis = [a*0.01 for a in range(-400, 300)]
x = 0.0
x_av = 0.0
for step in xrange(nsteps):
    xnew = x + random.uniform(-delta, delta)
    if random.uniform(0.0, 1.0) < prob(xnew) / prob(x):
        x = xnew
        acc_tot += 1
	acc_tmp += 1
    x_av += x
    data.append(x)
    if step % 100 == 0:
	if acc_tmp > 60:
		delta = delta * 1.1
	if acc_tmp < 40:
		delta = delta / 1.1
	acc_tmp = 0	

print 'global acceptance ratio:', acc_tot / float(nsteps)
print '<x> =', x_av / float(nsteps)

pylab.hist(data, bins=1000, normed = True)
exact_data = []
for a in xaxis:
	exact_data.append(prob(a))
print len(xaxis), "and", len(exact_data)
pylab.plot(xaxis, exact_data)
pylab.show()
