# Obligatory Library

import os, sys, shutil, glob, numpy, csv, cPickle
import random, subprocess

from keras.models import load_model
from keras.metrics import top_k_categorical_accuracy
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.sequence import pad_sequence
from keras.models import Sequential
from keras.layers import Dense, Bidirectional, LSTM, BatchNormalization, Dropout



import tensorflow as tf

import numpy as np
from numpy import NaN, Inf, arange, isscalar, array

import scipy
import scipy.signal
import scipy.io.wavfile as wavfile
import scipy.fftpack as fft
from scipy.fftpack.realtransforms import dct
from scipy.signal import fftconvolve
from scipy.signal import lfilter, hamming
from scipy import linalg as la
from scipy.io import wavfile

from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split


import audioread

import librosa

##Useful Library : 
import six
# Six is a Python 2 and 3 compatibility library.
#  It provides utility functions for smoothing over the differences between the Python versions.

