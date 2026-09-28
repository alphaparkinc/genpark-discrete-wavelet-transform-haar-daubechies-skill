"""Example demonstrating Haar DWT."""
from client import WaveletTransform

def main():
    sig = [4.0, 6.0, 10.0, 12.0]
    c = WaveletTransform.haar_forward(sig)
    print("Haar Coefficients:", [round(x, 2) for x in c])
    recon = WaveletTransform.haar_inverse(c)
    print("Reconstructed Signal:", recon)

if __name__ == "__main__":
    main()
