from math import log10 as log
import numpy as np
import matplotlib.pyplot as plt

CBi, CA, V0, Ve = 0.1, 0.1, 10, 10
CB, CBH, CH, pH, V = [], [], [], [], []
for VA in np.arange(1, 26, 0.5):
    if VA < Ve:
        V.append(VA)
        CB.append((CBi*V0-CA*VA)/(V0+VA))
        CBH.append((CA*VA/(V0+VA)))
        CH.append(0)
        pH.append(4.2 + log((0.1*V0-CA*VA)/(CA*VA)))
    elif VA > Ve:
        V.append(VA)
        CB.append(0)
        CBH.append(CBi*V0/(V0+VA))
        CH.append((CA*VA-CBi*V0)/(V0+VA))
        pH.append(-log((CA*VA-CBi*V0)/(V0+VA)))

plt.subplot(121)
plt.plot(V, CB, 'bx-', label="CB")
plt.plot(V, CBH, 'rx-', label="CBH")
plt.legend()
plt.subplot(122)
plt.ylim(0, 14)
plt.plot(V, pH, 'rx-', label="pH")
plt.legend()
plt.show()
