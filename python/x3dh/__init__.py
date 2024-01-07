from .x3dh import *

class _X3DHSer:
    def __init__(self): pass

    def gen_3xdh_secrets_key_pairs(self): 
        u1_ints, u2_ints = generate_3xdh_secrets_key_pairs()
        return (bytes(u1_ints), bytes(u2_ints))
    
x3dh_ser = _X3DHSer()
