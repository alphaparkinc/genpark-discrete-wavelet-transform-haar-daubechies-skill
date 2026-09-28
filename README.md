# Discrete Wavelet Transform (Haar DWT) Skill

Orthogonal multi-resolution spatial-frequency decomposition using Haar scaling and wavelet filter banks.

```mermaid
flowchart LR
    Signal["Signal Vector x[n]"] --> LowPass["Scaling Filter (Approximation A)"]
    Signal --> HighPass["Wavelet Filter (Detail D)"]
    LowPass --> Coeffs["Combined Wavelet Coefficients [A | D]"]
    HighPass --> Coeffs
    Coeffs --> Synthesis["Orthonormal Synthesis Filter Bank"]
    Synthesis --> Reconstructed["Exact Reconstructed Signal"]
```

## Features
- **100% Python Standard Library**: Orthonormal basis decomposition.
- **Simultaneous Time-Frequency Localization**: Captures transient edges and steps.
