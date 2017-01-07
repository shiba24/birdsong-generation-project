import os
import argparse
import glob
from tqdm import tqdm
import scipy
import scipy.signal
import wave
import struct
import numpy as np
import array


def readWave(wavefile):
    """
    Input: A file like object or file path
    Output: A numpy array of integers representing the PCM coded data, and
            the sample rate of the channels (mixed rate channels not supported)
    """
    stream = wave.open(wavefile, "r")
    num_channels = stream.getnchannels()
    sample_rate = stream.getframerate()
    sample_width = stream.getsampwidth()
    num_frames = stream.getnframes()

    raw_data = stream.readframes(num_frames)    # Returns byte data
    stream.close()
    total_samples = num_frames * num_channels
    if sample_width == 1:
        fmt = "%iB" % total_samples     # read unsigned chars
    elif sample_width == 2:
        fmt = "%ih" % total_samples     # read signed 2 byte shorts
    else:
        raise ValueError("Only supports 8 and 16 bit audio formats.")
    integer_data = struct.unpack(fmt, raw_data)
    del raw_data      # Keep memory tidy (who knows how big it might be)
    channels = [[] for time in range(num_channels)]
    for index, value in enumerate(integer_data):
        bucket = index % num_channels
        channels[bucket].append(value)
    return np.array(channels), sample_rate, sample_width
 

 def resample(in_wav, in_rate, sample_width, out_file, out_rate, out_channel=1):
    if len(in_wav.shape) > 1:
        in_sample = len(in_wav[0])
        in_wav = in_wav[0]
    else:
        in_sample = len(in_wav)
    out_sample = in_sample * out_rate / in_rate

    # FFT is fastest when len(signal) is power of 2
    y = np.floor(np.log2(in_sample))
    nextpow2 = np.int64(np.power(2, y + 1))
    pad_data = np.pad(in_wav, (0, nextpow2 - in_sample), mode='constant', constant_values=(0, 0))
    data = scipy.signal.resample(pad_data, nextpow2 * out_rate / in_rate).astype(np.int16)[:out_sample]

    w = wave.Wave_write(out_file)
    w.setparams((out_channel, sample_width, out_rate, out_sample, "NONE", "not compressed"))
    w.writeframes(array.array('h', data).tostring())
    w.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Resample .wav files from 44.1 kHz to 16 kHz.')
    parser.add_argument('--srcdir', '-s', default='', type=str,
                        help='Source data directory')
    parser.add_argument('--dstdir', '-d', default='./corpus', type=str,
                        help='Destination data directory')
    args = parser.parse_args()

    src_dir = args.srcdir
    dst_dir = args.dstdir

    src_list = glob.glob(os.path.join(src_dir, '*.wav'))
    src_list.sort()
    dst_list = [os.path.join(dst_dir, file[file.rfind(os.path.sep) + 1:]) for file in src_list]

    out_channel = 1
    out_rate = 16000
    for src_file, dst_file in tqdm(zip(src_list, dst_list)):
        in_wav, in_rate, sample_width = readWave(src_file)
        resample(in_wav, in_rate, sample_width, dst_file, out_rate, out_channel)
