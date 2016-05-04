import sys
import os
import subprocess
import csv
import numpy as np
import re
import time
from time import mktime
from datetime import datetime
sys.path.append("../../common/")
from common import *
from create_csv_common import *




fieldnames = glob +  [(h+"-"+s) for h in hosts for s in loca]

print ",".join(map(lambda x: "'"+x+"'", fieldnames))

