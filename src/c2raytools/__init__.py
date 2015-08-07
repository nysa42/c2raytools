'''
c2raytools is a Python package for reading and 
analyzing data files produced with C2Ray and CubeP3M.
For documentation, see: http://ttt.astro.su.se/~hjens/c2raytools/
You can also get documentation for all routines directory from
the interpreter using Python's built-in help() function.
For example:
>>> import c2raytools as c2t
>>> help(c2t.calc_dt)
'''


#Import sub-modules 
import conv
from conv import set_sim_constants
from const import *
from beam_convolve import *
from density_file import *
from xfrac_file import *
from vel_file import *
from irate_file import *
from temper_file import *
from halo_list import *
from statistics import *
from power_spectrum import *
from tau import *
from lightcone import *
from pv_mpm import *
from temperature import *
from helper_functions import *
from cosmology import *
from plotting import *
from power_legendre import *
from deprecated import *
from angular_coordinates import *
from smoothing import *
from power_spectrum_noise import *
from gaussian_random_field import *

#Suppress warnings from zero-divisions and nans
import numpy
numpy.seterr(all='ignore')
