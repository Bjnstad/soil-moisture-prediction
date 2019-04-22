#!/usr/local/bin/python3.6
import matplotlib.pyplot as plt
import load

_days = load.new()

plt.plot(_days._moist_2)
plt.plot(_days._precip)
plt.show()
