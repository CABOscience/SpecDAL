# readers.py provides functions to read .sig spectrum files for data and
# metadata.

import pandas as pd
import numpy as np
from os.path import abspath, expanduser, splitext, basename, join, split
import glob
from collections import OrderedDict
import re
import json

def read_calibration(filepath, read_data=True, read_metadata=True, verbose=False):
    """
    Read txt file calibration for data and metadata
    
    Return
    ------
    2-tuple of (pd.DataFrame, OrderedDict) for data, metadata
    """
    data = None
    metadata = None
    raw_metadata = {}
    # first, get raw metadata and line number of data
    r = re.compile(r"^\d+(?=\d|$)")
    with open(abspath(expanduser(filepath)), 'r') as f:
        if verbose:
            print('reading {}'.format(filepath))
        for i, line in enumerate(f):
            if r.match(line):
                break
            field = line.strip().split('= ')
            if len(field) > 1:
                raw_metadata[field[0]] = field[1].strip()
    if read_data:
        # read data
        colnames = ["wavelength", "reflectance"]
        data = pd.read_table(filepath, skiprows=i,
                             sep="\s+",
                             header=None, names=colnames
        ).astype(str)
        for d in list(data.keys()):
            data[d] = data[d].str.replace(',', '.').astype(float)
        data = data.set_index('wavelength')

    if read_metadata:
        metadata = OrderedDict()
        metadata['file'] = f.name
        metadata['instrument_type'] = 'CALIBRATION'
        metadata['measurement_type'] = 'reflectance'
        metadata['wavelength_range'] = None
        if read_data:
            metadata['wavelength_range'] = (data.index.min(), data.index.max())
    return data, metadata
