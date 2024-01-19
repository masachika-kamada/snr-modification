# SNR Modification

This repository contains the code and resources for modifying the Signal-to-Noise Ratio (SNR) of audio signals. The primary script is a Jupyter Notebook (`ipynb` file) that demonstrates the process of adjusting SNR for given audio samples.

## Features

- **Signal Power Calculation**: Functions to calculate the power of audio signals.
- **SNR Calculation**: Functions to compute the SNR of audio signals.
- **SNR Adjustment**: Methods to adjust SNR to a target value.
- **Room Simulation**: Utilizing Pyroomacoustics to simulate audio in a room environment.
- **Audio Playback**: Integrated audio playback in Jupyter Notebook.

## Usage

1. **Load Audio Files**: Load your audio files using the provided `load_signal_from_wav` function.
2. **Calculate Signal Power**: Determine the power of your source and noise signals.
3. **Compute and Adjust SNR**: Calculate the current SNR and adjust it to your desired target SNR.
4. **Room Simulation**: Simulate the audio signals in a room environment using Pyroomacoustics.
5. **Playback**: Use the IPython display module to play back the audio.

## SNR Calculation Method

The SNR is defined as the ratio of the power of a signal to the power of noise. Here are the basic steps to calculate SNR:

1. **Calculate Signal Power**: Compute the average power of the signal. This is done by squaring the samples of the signal in the time domain and taking their average.
2. **Calculate Noise Power**: Similarly, compute the average power of the noise.
3. **Compute SNR**: Divide the signal power by the noise power to obtain the SNR. Typically, this ratio is expressed in decibels (dB).

$$SNR (dB) = 10 \cdot \log_{10} \left( \frac{\text{Signal Power}}{\text{Noise Power}} \right)$$

Using this method, you can assess the current SNR of your audio samples and adjust it to a target SNR.
