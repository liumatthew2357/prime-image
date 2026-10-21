# ImagePrime

ImagePrime is a Python project that transforms an image into a numerical representation and searches for the next prime number greater than that representation.

The project combines image processing, arbitrary-precision arithmetic, and computational number theory to explore the relationship between visual data and prime numbers.

## Features

- **Image Processing:** Loads, resizes, and processes images using Pillow.
- **Colour Quantization:** Maps image pixels to a predefined colour palette.
- **Numerical Representation:** Converts processed image data into a large integer.
- **Prime Search:** Uses `gmpy2` to find the next prime number greater than the generated integer.
- **Performance Benchmarking:** Measures prime-search performance for integers containing thousands of digits.

## Technologies

- **Python** — Core implementation
- **Pillow** — Image processing
- **gmpy2** — Arbitrary-precision arithmetic and prime-number computation

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/prime-image.git
cd prime-image
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

The project currently uses a local Python implementation.

**To run:** Add the verified command for the program's main entry point here, along with a sample input and expected output.

## Project Status

The core image-processing and prime-search algorithms have been implemented. A user-facing web interface is planned for a future version.

## Future Improvements

- Build a local web interface for uploading images.
- Display the processed image and corresponding prime-number representation.
- Improve performance for larger numerical inputs.
- Deploy the application online.