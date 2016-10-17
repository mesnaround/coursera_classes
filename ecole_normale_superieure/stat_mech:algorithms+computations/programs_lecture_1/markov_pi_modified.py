import random

n_trials = 2 ** 12
acceptance_ratios = []

for delta in [0.062, 0.125, 0.25, 0.5, 1.0, 1.25, 1.5, 1.75, 2.0, 4.0, 8.0, 16.0]:
    n_accepted = 0
    n_rejected = 0
    n_hits = 0
    x, y =1.0, 1.0
    for i in range(n_trials):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            n_accepted += 1
            x, y = x + del_x, y + del_y
        else:
            n_rejected += 1
        if x**2 + y**2 < 1.0: n_hits += 1            
    print "delta = ",delta," and pi_est = ",4.0 * n_hits / float(n_trials)
    print "acceptance ratio = ",n_accepted/float(n_rejected)
    print '\n'
