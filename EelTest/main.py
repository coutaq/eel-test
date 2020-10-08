import eel
import ml_boilerplate as ml

MODE = 'folder' # or 'file', if you choose a plain text file (see above).
DATASET_PATH = '/data/uppercase' # the dataset file or root folder path.
N_CLASSES = 2 # CHANGE HERE, total number of classes
IMG_HEIGHT = 50 # CHANGE HERE, the image height to be resized to
IMG_WIDTH = 33 # CHANGE HERE, the image width to be resized to
CHANNELS = 1 # The 3 color channels, change to 1 if grayscale

X, Y = ml.read_images(DATASET_PATH, MODE, 19)

# eel.init("web")
# eel.start("main.html")