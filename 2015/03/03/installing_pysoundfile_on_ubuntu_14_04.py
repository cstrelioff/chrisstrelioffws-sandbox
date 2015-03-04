
from __future__ import print_function
import pysoundfile as sf

print("PySoundFile version: {}".format(sf.__version__))

for key, val in sf.available_formats().items():
    print("{:5s} -- desc: {}".format(key, val))

# read an existing wav file
data, samplerate = sf.read('existing_file.wav')

# write the data to a new ogg file
sf.write(data, 'new_file.ogg', samplerate=samplerate)