import os
import sys
import argparse

def main(mode='rand_sound'):
    mode = mode.lower()

    from pycochleagram import cochleagram as cgram
    from pycochleagram import erbfilter as erb
    from pycochleagram import utils
    from random import choice
    from pycochleagram.demo import demo_human_cochleagram_helper

    from os.path import dirname, join, realpath
    from pydub import AudioSegment
    # from argparse import argumentparser
  #AUDIO PROCESSING SECTION: MANIPULATES MP3 FILES AND CONVERTS TO WAV, SLICES $
    DEMO_PATH = join(dirname(realpath(__file__)) #'/media/sf_acm_mirum_tempo' THE DATASET LINK MUST BE PUT HERE
    if mode == 'rand_sound':
        rfn=[]
        soundname=[]
        file_extension=[]
    #mpg123 -w train.append(f.wav) f 
        path, dirs, files = next(os.walk(DEMO_PATH))
        file_count = len(files)
        for i in range(0,file_count):
            rfn.append(choice([os.path.join(DEMO_PATH,f)for f in os.listdir(DEMO_PATH) if f.endswith('.mp3')]))
            soundname.append(AudioSegment.from_mp3(rfn[i]))
            clips = soundname[i][:10000]
    #sound.export("/output/path/file.wav", format="wav")
    #mpg123 -w foo.wav foo.mp3
    #print(os.listdir(DEMO_PATH))
    # rfn = [os.path.join(DEMO_PATH, f)for f in os.listdir(DEMO_PATH)][1]
        print('Running demo with sound file: %s ' % rfn)
        demo_stim = utils.wav_to_array(soundname[1])
        demo_sr=12000
        demo_n = 38  # default filter for low_lim=50 hi_lim=20000
    else:
        demo_stim, demo_sr, demo_n = None, None, None

    print('\n### DEMO: COCHLEAGRAM GENERATION ###')
    print('====================================')
    demo_human_cochleagram(demo_stim, demo_sr, demo_n)
    features= demo_human_cochleagram_helper(file, demo_sr, demo_n, sample_factor=2, downsample=None, nonlinearity=None)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-m', '--mode', default='rand_sound',
      help='Determines what type of signals to use for the demo.')
  args = parser.parse_args()

  main(mode=args.mode)

