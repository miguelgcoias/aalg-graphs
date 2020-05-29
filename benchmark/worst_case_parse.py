import sys
import matplotlib.pyplot as plt

m = [[] for i in range(7)]
t = [[] for i in range(7)]


log_path = sys.argv[1] # path to a file with the output of apl_worst_case

with open(log_path) as f:
    lines = f.readlines()
    for l in lines:
        l = l.strip('\n').split(' ')
        d = int(l[1])

        if(d > 6):
            d = 0

        m[d] += [int(l[0]) ** 2]
        t[d] += [float(l[2])]

plt.xlabel('$V^2$', useTex=True)
plt.ylabel('Time [s]')

plt.plot(m[3], t[3], 'ro', label='3')
plt.plot(m[4], t[4], 'bo', label='4')
plt.plot(m[5], t[5], 'go', label='5')
plt.plot(m[6], t[6], 'yo', label='6')
plt.plot(m[0], t[0], 'o',  label='6+')
plt.legend(title='Diameter', loc='upper left')

plt.show()
#plt.savefig('apl_worst_case.png')
