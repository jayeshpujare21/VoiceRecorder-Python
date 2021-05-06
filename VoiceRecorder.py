import sounddevice as sd
from scipy.io.wavfile import write
  
Frequency = 44100

FileName = input('Enter Duration in File Name :')
Duration = int(input('Enter Duration in Seconds :'))

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(Duration * Frequency), samplerate=Frequency, channels=2)

sd.wait()

write(FileName+'.wav', Frequency, myrecording)