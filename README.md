# DCTorch

Fast discrete cosine transforms for PyTorch.

## Installation

```bash
pip install dctorch
```

## Usage

```python
import torch
from dctorch import dct, idct, dct2, idct2, dct3, idct3

# 1D DCT
x = torch.randn(10, 16)  # batch_size x length
y = dct(x)
x_reconstructed = idct(y)

# 2D DCT
x = torch.randn(10, 32, 32)  # batch_size x height x width
y = dct2(x)
x_reconstructed = idct2(y)

# 3D DCT
x = torch.randn(10, 8, 32, 32)  # batch_size x depth x height x width
y = dct3(x)
x_reconstructed = idct3(y)
```

## Functions

- `dct(t)` - 1D Discrete Cosine Transform
- `idct(t)` - 1D Inverse Discrete Cosine Transform
- `dct2(t)` - 2D Discrete Cosine Transform
- `idct2(t)` - 2D Inverse Discrete Cosine Transform
- `dct3(t)` - 3D Discrete Cosine Transform
- `idct3(t)` - 3D Inverse Discrete Cosine Transform

## License

MIT 