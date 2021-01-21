from os.path import abspath, dirname, join, pardir

from loren_frank_data_processing import Animal

# LFP sampling frequency
SAMPLING_FREQUENCY = 1500

# Data directories and definitions
ROOT_DIR = join(abspath(dirname(__file__)), pardir)
RAW_DATA_DIR = join(ROOT_DIR, 'Raw-Data')
PROCESSED_DATA_DIR = join(ROOT_DIR, 'Processed-Data')


ANIMALS = {
    'HPa': Animal(directory=join(RAW_DATA_DIR, 'HPa_direct'),
                  short_name='HPa'),
}
