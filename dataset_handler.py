from torch.utils.data import Dataset
import pandas as pd
from skimage import io

class CharacterDataset(Dataset):
    
    def __init__(self, descFile):
        """
        Args:
            descFile(string): path to the csv file that describes the dataset
        """
        self.files = pd.read_csv(descFile, usecols=range(1))
        self.labels = pd.read_csv(descFile, usecols=range(1,2))
        print(self.labels)

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        imgPath = self.files.iloc[idx,0]

        img = io.imread(imgPath)
        label = self.labels.iloc[idx, 0]
        sample = {'image': img, 'label': label}
        return sample
