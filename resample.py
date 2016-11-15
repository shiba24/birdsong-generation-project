import os
import wave
import audioop
import argparse



def downsampleWav(src, dst, inrate=44100, outrate=16000, inchannels=2, outchannels=1):
    if not os.path.exists(src):
        print 'Source not found!'
        return False

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    try:
        s_read = wave.open(src, 'r')
        s_write = wave.open(dst, 'w')
    except:
        print 'Failed to open files!'
        return False

    n_frames = s_read.getnframes()
    data = s_read.readframes(n_frames)

    try:
        converted = audioop.ratecv(data, 2, inchannels, inrate, outrate, None)
        if outchannels == 1:
            converted = audioop.tomono(converted[0], 2, 1, 0)
    except:
        print 'Failed to downsample wav'
        return False

    try:
        s_write.setparams((outchannels, 2, outrate, 0, 'NONE', 'Uncompressed'))
        s_write.writeframes(converted)
    except:
        print 'Failed to write wav'
        return False

    try:
        s_read.close()
        s_write.close()
    except:
        print 'Failed to close wav files'
        return False

    return True


parser = argparse.ArgumentParser(description='Resample .wav files from 44.1 kHz to 16 kHz.')
parser.add_argument('--srcdir', '-s', default='', type=str,
                    help='Source data directory')
parser.add_argument('--dstdir', '-d', default='./corpus', type=str,
                    help='Destination data directory')
args = parser.parse_args()

src_dir = args.srcdir
dst_dir = args.dstdir

src_list = glog.glob(os.pat.join(src_dir, '.wav'))
src_list.sort()

dst_list = [os.path.join(dst_dir, file[file.rfind(os.path.sep) + 1:]) for file in src_list]


for src_file, dst_file in zip(src_list, dst_list):
    downsampleWav(src_file, dst_file, inrate=44100, outrate=16000, inchannels=2, outchannels=1)

