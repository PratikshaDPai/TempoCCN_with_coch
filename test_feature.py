
import unittest
from numba.decorators import jit as optional_jit
import librosa

from tempocnn.feature import read_features
from tempocnn.tester import demo_human_cochleagram_helper  #(signal, sr, n, sample_factor=2, downsample=None, nonlinearity=None)

class TestTempoClassifier(unittest.TestCase):

    def test_init(self):
        print(":) in test_init")
        file = 'data/drumtrack.mp3'
        y, sr = librosa.load(file, sr=11025)
        # possible features frames
        num_feature_frames = y.shape[0] / 512
        # possible feature windows with half overlap
        num_feature_windows = (num_feature_frames // 128) // 2

        #features = read_features(file)


        demo_stim, demo_sr = utils.wav_to_array(file)
        demo_n = 38  # default filter for low_lim=50 hi_lim=20000, we use loww = 20, high = 5000
        #demo_human_cochleagram(demo_stim, demo_sr, demo_n)
        features= demo_human_cochleagram_helper(file, demo_sr, demo_n, sample_factor=2, downsample=None, nonlinearity=None)
        self.assertEqual(len(features.shape), 4)
        self.assertEqual(features.shape[0], num_feature_windows)
        self.assertEqual(features.shape[1], 40)
        self.assertEqual(features.shape[2], 256)
        self.assertEqual(features.shape[3], 1)
        print(features.shape)
