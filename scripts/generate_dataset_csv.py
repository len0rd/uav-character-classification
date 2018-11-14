import csv
from os import listdir
from os.path import isfile, join, dirname, realpath

# directory relative to the  repository root where the image files are located
rootFolder = 'dataset'

# get full path of where to find files for the dataset
datasetPath = join(dirname(realpath(__file__)), '../', rootFolder)
print("Dataset Path {}".format(datasetPath))

# get all the file names
datasetFiles = [f for f in listdir(datasetPath) if isfile(join(datasetPath, f))]

# write to csv
with open('character_description.csv', mode='w') as descFile:
    descriptionWriter = csv.writer(descFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for fileName in datasetFiles:
        rootRelativePath = join(rootFolder, fileName) # ie: dataset/A-123-2.jpeg
        classification = fileName[0] # first character in image name == classification

        # column 0 = filepath relative to repo root. column 1 = classification for that file
        descriptionWriter.writerow([rootRelativePath, classification])
