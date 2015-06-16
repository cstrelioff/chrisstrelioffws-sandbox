
from __future__ import print_function
import soundfile as sf

print("PySoundFile version: {}".format(sf.__version__))

for key, val in sf.available_formats().items():
    print("{:5s} -- desc: {}".format(key, val))