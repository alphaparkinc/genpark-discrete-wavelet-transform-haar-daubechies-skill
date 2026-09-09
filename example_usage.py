"""Example usage for Discrete Wavelet Transform Skill."""
from client import HaarWaveletTransform

def main():
    print("Executing Haar Discrete Wavelet Transform...")
    data = [4.0, 6.0, 10.0, 12.0]
    approx, detail = HaarWaveletTransform.forward(data)
    print("Approximation (Low-pass):", approx)
    print("Detail (High-pass):", detail)

    rec = HaarWaveletTransform.inverse(approx, detail)
    print("Reconstructed:", rec)
    for v1, v2 in zip(data, rec):
        assert abs(v1 - v2) < 1e-3
    print("Haar Wavelet Transform verified successfully!")

if __name__ == "__main__":
    main()
