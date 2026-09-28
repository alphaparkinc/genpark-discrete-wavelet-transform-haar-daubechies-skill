"""Discrete Wavelet Transform (Haar DWT).
100% Python Standard Library.
"""

import math

class WaveletTransform:
    @staticmethod
    def haar_forward(signal):
        n = len(signal)
        assert n % 2 == 0
        approx = []
        detail = []
        inv_sqrt2 = 1.0 / math.sqrt(2.0)
        for i in range(0, n, 2):
            approx.append((signal[i] + signal[i+1]) * inv_sqrt2)
            detail.append((signal[i] - signal[i+1]) * inv_sqrt2)
        return approx + detail

    @staticmethod
    def haar_inverse(coeffs):
        n = len(coeffs)
        half = n // 2
        approx = coeffs[:half]
        detail = coeffs[half:]
        inv_sqrt2 = 1.0 / math.sqrt(2.0)
        signal = [0.0] * n
        for i in range(half):
            signal[2*i] = round((approx[i] + detail[i]) * inv_sqrt2, 5)
            signal[2*i + 1] = round((approx[i] - detail[i]) * inv_sqrt2, 5)
        return signal
