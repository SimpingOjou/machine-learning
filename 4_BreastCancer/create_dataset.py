import config
from imutils import paths
import random, shutil, os

def create_dataset():
        # Load the original dataset paths
        originalPaths = list(paths.list_images(config.DATASET_PATH))

        # Shuffle the files
        random.seed(7)
        random.shuffle(originalPaths)

        # Calculate the index for the training split
        index = int(len(originalPaths) * config.TRAIN_SPLIT)
        # Split the original paths into training and testing paths
        trainPaths = originalPaths[:index]
        testPaths = originalPaths[index:]

        # Calculate the index for the validation split within the training paths
        index = int(len(trainPaths) * config.VAL_SPLIT)
        # Split the training paths into validation and remaining training paths
        valPaths = trainPaths[:index]
        trainPaths = trainPaths[index:]

        datasets = [("training", trainPaths, config.TRAIN_PATH),
                ("validation", valPaths, config.VAL_PATH),
                ("testing", testPaths, config.TEST_PATH)
        ]

        for (setType, originalPaths, basePath) in datasets:
                # Print the type of dataset being built
                print(f'Building {setType} set')

                # Check if the base path exists, if not, create it
                if not os.path.exists(basePath):
                        print(f'Building directory {basePath}')
                        os.makedirs(basePath)

                # Loop over each path in the current set
                for path in originalPaths:
                        # Extract the file name and label from the path
                        file = path.split(os.path.sep)[-1]
                        label = file[-5:-4]

                        # Create the label directory if it does not exist
                        labelPath = os.path.sep.join([basePath, label])
                        if not os.path.exists(labelPath):
                                print(f'Building directory {labelPath}')
                                os.makedirs(labelPath)

                        # Construct the new path and copy the file
                        newPath = os.path.sep.join([labelPath, file])
                        shutil.copy2(path, newPath)