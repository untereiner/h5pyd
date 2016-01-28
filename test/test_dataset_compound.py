##############################################################################
# Copyright by The HDF Group.                                                #
# All rights reserved.                                                       #
#                                                                            #
# This file is part of H5Serv (HDF5 REST Server) Service, Libraries and      #
# Utilities.  The full HDF5 REST Server copyright notice, including          #
# terms governing use, modification, and redistribution, is contained in     #
# the file COPYING, which can be found at the root of the source code        #
# distribution tree.  If you do not have access to this file, you may        #
# request a copy from help@hdfgroup.org.                                     #
##############################################################################

import numpy as np
import math

import config

if config.get("use_h5py"):
    import h5py
else:
    import h5pyd as h5py
    
from common import ut, TestCase

        
class TestDatasetCompound(TestCase):
    def test_create_compound_dset(self):
        filename = self.getFileName("create_compoound_dset")
        print("filename:", filename)
        f = h5py.File(filename, "w")

        count = 10
  
        dt = np.dtype([('real', np.float), ('img', np.float)])
        dset = f.create_dataset('complex', (count,), dtype=dt)
   
        elem = dset[0]
        for i in range(count):
            theta = (4.0 * math.pi)*(float(i)/float(count))
            elem['real'] = math.cos(theta)
            elem['img'] = math.sin(theta)
            dset[i] = elem
       
        f.close()
        val = dset[0]
        self.assertEqual(val['real'], 1.0)
        f.close()
        
    
    
if __name__ == '__main__':
    ut.main()