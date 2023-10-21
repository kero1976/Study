import sys
import pprint
import os
print(sys.version)
pprint.pprint(sys.path)

for key, val in os.environ.items():
    print(f"{key}: {val}")