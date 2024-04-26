#import numpy as np
# Importing PySwarms
import matplotlib.pyplot as plt
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_contour
from pyswarms.utils.plotters.formatters import Designer, Mesher

# Set-up all the hyperparameters
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
# Call an instance of PSO
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)
# Perform the optimization
cost, pos = optimizer.optimize(fx.sphere, iters=1000)

m = Mesher(func=fx.sphere)
anim = plot_contour(pos_history=optimizer.pos_history,mesher=m,mark=(0,0))
anim = plt.show()