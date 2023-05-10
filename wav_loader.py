import numpy as np
import wavio
import struct

def wav_to_np(filepath: str) -> np.ndarray:
    with open(filepath, 'rb') as wave_file:
        w = wavio.read(wave_file)
        channels = w.data.shape[1]
        assert channels == 1
        samplewidth = w.sampwidth
        assert samplewidth == 3
        framerate = w.rate
        assert framerate == 48000

        frame_length = w.data.shape[0]

        print(f'Channels: {channels}')
        print(f'Frame Length: {frame_length}')
        print(f'Sample Width: {samplewidth}')
        print(f'Frame Rate {framerate}')

    return w.data

if __name__ == '__main__':
    file_path = 'C:/GIT/DeepRig/data/essex30_source/30_sec/split_30_essex30_source.wav'
    data = wav_to_np(file_path)
    print(f'Data Length {data.shape}')