import os

# Define the path to the input dataset
DATASET_PATH = r'./Data/Input_dataset'

# Define the path to the output datasets
BASE_PATH = r'./Data'
TRAIN_PATH = os.path.sep.join([BASE_PATH, "training"])
VAL_PATH = os.path.sep.join([BASE_PATH, "validation"])
TEST_PATH = os.path.sep.join([BASE_PATH, "testing"])

# Define training, validation, and testing split
TRAIN_SPLIT = 0.8
VAL_SPLIT = 0.1