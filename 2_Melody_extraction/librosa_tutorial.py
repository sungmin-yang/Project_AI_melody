import librosa
#https://librosa.github.io/librosa/tutorial.

# Load sound files
filenames           = ["1.wav", "2.wav"]
file_with_features  = dict()

for f in filenames:
  y, sr = librosa.load(f)
  file_with_features[f] = extract_features(y)
  

def extract_features(librosa_y):
  """
  https://librosa.github.io/librosa/feature.html
  """
  
  #features
  mfcc           = librosa.feature.mfcc(y=y, sr=sr)
  melspectrogram = librosa.feature.melspectrogram(y, n_mels = 2, n_fft=1024)
  
  
  #Core IO and DSP
  #https://librosa.github.io/librosa/core.html
  
  db = librosa.power_to_db(mel, ref = np.max)
  #pow = db = librosa.db_to_power(mel, ref = np.max)
  
  
