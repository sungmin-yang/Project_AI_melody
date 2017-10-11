

## Librosa : neat. clean, simple
 > https://librosa.github.io <br/>
 


## Aubio
> https://github.com/aubio/aubio <br/>

For monophonic signals go with YIN (or pYIN https://github.com/ronggong/pypYIN),  <br/>
for more complex mixtures with a predominant melody you can try out MELODIA (Salamon et al.), <br/>
available in essentia or as a VAMP plugin. <br/>

Stefan <br/>
https://github.com/librosa/librosa/issues/527 <br/>

## PyAudioAnalysis

> def stHarmonic(frame, fs):<br/>
     """<br/>
     Computes harmonic ratio and pitch<br/>
> def phormants(x, Fs)

> https://github.com/tyiannak/pyAudioAnalysis <br/>


### feature extraction
https://github.com/tyiannak/pyAudioAnalysis/wiki/3.-Feature-Extraction
Feature ID	Feature Name	Description
1	Zero Crossing Rate	The rate of sign-changes of the signal during the duration of a particular frame.
2	Energy	The sum of squares of the signal values, normalized by the respective frame length.
3	Entropy of Energy	The entropy of sub-frames' normalized energies. It can be interpreted as a measure of abrupt changes.
4	Spectral Centroid	The center of gravity of the spectrum.
5	Spectral Spread	The second central moment of the spectrum.
6	Spectral Entropy	Entropy of the normalized spectral energies for a set of sub-frames.
7	Spectral Flux	The squared difference between the normalized magnitudes of the spectra of the two successive frames.
8	Spectral Rolloff	The frequency below which 90% of the magnitude distribution of the spectrum is concentrated.
9-21	MFCCs	Mel Frequency Cepstral Coefficients form a cepstral representation where the frequency bands are not linear but distributed according to the mel-scale.
22-33	Chroma Vector	A 12-element representation of the spectral energy where the bins represent the 12 equal-tempered pitch classes of western-type music (semitone spacing).
34	Chroma Deviation	The standard deviation of the 12 chroma coefficients.


### just for reading, formant, harmonics, ...
> http://www.voicescienceworks.org/harmonics-vs-formants.html
