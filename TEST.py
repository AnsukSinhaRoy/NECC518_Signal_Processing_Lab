import numpy as np

data_freq = {1: 200, 2: 300, 3: 400, 4: 500, 5: 600, 6: 700, 7: 800, 8: 900, 9: 1000, '*': 1100, 0: 1200, '#': 1300}
carrier_freq = 10000  
sample_rate = 44100  
duration = 0.1  

def generate_signal(digit, carrier_freq):
    freq = data_freq[digit]
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    signal = np.sin(2 * np.pi * freq * t) * np.sin(2 * np.pi * carrier_freq * t)
    return signal

def demodulate_signal(signal, carrier_freq):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    demod_signal = signal * np.sin(2 * np.pi * carrier_freq * t)
    fft_result = np.fft.fft(demod_signal)
    freqs = np.fft.fftfreq(len(demod_signal), d=1/sample_rate)
    magnitudes = np.abs(fft_result)
    peak_index = np.argmax(magnitudes)
    detected_freq = abs(freqs[peak_index])
    return detected_freq

def sender():
    data = [9, 8, 2, 0, 2]
    for i in data:
        signal = generate_signal(i, carrier_freq)
        receiver(signal, carrier_freq)

def receiver(signal, carrier_freq):
    detected_freq = demodulate_signal(signal, carrier_freq)
    for digit, freq in data_freq.items():
        if abs(freq - detected_freq) < 50:  
            print(f"Received: {digit}")
            break

sender()