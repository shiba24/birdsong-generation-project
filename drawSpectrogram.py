# -*- coding: utf-8 -*-
import numpy as np
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(context="poster", style='white', font_scale=1.5) #, rc={'grid.linestyle': '--'})

from resample import readWave


def main(wavefile, NFFT=255):
    print wavefile
    channels, sample_rate, _ = readWave(wavefile)
    plt.figure(figsize=(24, 10), dpi=120)
    plt.subplot(2, 1, 1)
    plt.plot(channels[0])
    plt.yticks([])
    plt.ylabel("waveform")
    plt.xlim([0., len(channels[0])])

    plt.subplot(2, 1, 2)
    plt.specgram(channels[0], Fs=sample_rate, NFFT=NFFT) #, scaling='spectrum')
    plt.ylim([0, sample_rate / 2])
    plt.ylabel("frequency [Hz]")
    plt.xlim([0., len(channels[0]) / float(sample_rate)])
    plt.xlabel("time [s]")

    plt.subplots_adjust(hspace=0)
    plt.savefig(wavefile[:-4] + "_spectrogram.png")
    plt.close() 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--wavefile', '-w', type=str, help='')
    parser.add_argument('--nfft', '-n', default=255, type=int, help='')
    args = parser.parse_args()

    main(args.wavefile, args.nfft)


