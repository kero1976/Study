import sys
import pprint
import os
print(sys.version)
pprint.pprint(sys.path)
pprint.pprint({key: val for key, val in os.environ.items()})
