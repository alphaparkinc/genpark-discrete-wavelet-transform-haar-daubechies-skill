"""
Autonomous Agent Discrete Wavelet Transform (DWT) Skill
Pure Python Standard Library implementation using Haar wavelets.
"""
import math
from typing import List, Tuple, Dict, Any

class HaarWaveletTransform:
    """
    Discrete Wavelet Transform with multi-level Haar subband filtering.
    """
    @staticmethod
    def forward(signal: List[float]) -> Tuple[List[float], List[float]]:
        n = len(signal)
        if n % 2 != 0:
            signal = list(signal) + [signal[-1]]
            n += 1
        approx = []
        detail = []
        inv_sqrt2 = 1.0 / math.sqrt(2.0)
        for i in range(0, n, 2):
            approx.append(round((signal[i] + signal[i + 1]) * inv_sqrt2, 4))
            detail.append(round((signal[i] - signal[i + 1]) * inv_sqrt2, 4))
        return approx, detail

    @staticmethod
    def inverse(approx: List[float], detail: List[float]) -> List[float]:
        signal = []
        inv_sqrt2 = 1.0 / math.sqrt(2.0)
        for a, d in zip(approx, detail):
            signal.append(round((a + d) * inv_sqrt2, 4))
            signal.append(round((a - d) * inv_sqrt2, 4))
        return signal
