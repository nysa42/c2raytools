import const
import numpy as np
import density_file as df
from helper_functions import print_msg 

class XfracFile:
	'''
	A C2Ray xfrac file.
	
	Use the read_from_file method to load an xfrac file, or 
	pass the filename to the constructor.
	
	Some useful attributes of this class are:
		* xi (numpy array): the ionized fraction
		* z (float): the redshift of the file (-1 if it couldn't be determined from the file name)
	
	'''
	def __init__(self, filename = None, old_format=False):
		'''
		Initialize the file. If filename is given, read data. Otherwise,
		do nothing.
		
		Parameters:
			* filename = None (string): the file to read from.
			* old_format = False (bool): whether to use the old-style 
				file format.
		Returns:
			Nothing
		'''
		if filename:
			self.read_from_file(filename, old_format)

	def read_from_file(self, filename, old_format=False):
		'''
		Read data from file.
		
		Parameters:
			* filename (string): the file to read from.
			* old_format = False (bool): whether to use the old-style (32 bits)
				file format.
		Returns:
			Nothing
		'''
		print_msg('Reading xfrac file:%s...' % filename)
		self.filename = filename

		f = open(filename, 'rb')
		temp_mesh = np.fromfile(f, count=6, dtype='int32')
		self.mesh_x, self.mesh_y, self.mesh_z = temp_mesh[1:4]

		if old_format:
			self.xi = np.fromfile(f, dtype='float32')
		else:
			self.xi = np.fromfile(f, dtype='float64')
		self.xi = self.xi.reshape((self.mesh_x, self.mesh_y, self.mesh_z), order='F')

		f.close()
		print_msg('...done')

		#Store the redshift from the filename
		import os.path
		try:
			name = os.path.split(filename)[1]
			self.z = float(name.split('_')[1][:-4])
		except:
			print_msg('Could not determine redshift from file name')
			self.z = -1


