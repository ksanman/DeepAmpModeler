import numpy as np
from wav_loader import wav_to_np
import matplotlib.pyplot as plt

def draw_file(data: np.array):
    plt.plot(data)
    plt.show()

if __name__ == '__main__':
    filepath = 'C:/GIT/DeepRig/data/essex30_source/30_sec/split_30_essex30_source.wav'
    data = wav_to_np(filepath=filepath)
     
    # Test first 1000 data points
    #data = data[:1000]
    draw_file(data)