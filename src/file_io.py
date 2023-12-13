import numpy as np
from scipy.io import wavfile
from scipy.signal import resample_poly

def load_signal_from_wav(wav_file_path: str, expected_fs: int) -> np.ndarray:
    fs, signal = wavfile.read(wav_file_path)
    if fs != expected_fs:
        signal = signal.astype(float)
        signal = resample_poly(signal, expected_fs, fs)

    if len(signal.shape) >= 2:
        signal = signal.T
    return signal