# Image Transformation Playground

A Python project for applying **linear transformations** to images using inverse mapping — built from scratch with NumPy and PIL, no OpenCV shortcuts.

---

## What It Does

Takes an image and applies a 2×2 transformation matrix to it using **inverse mapping** — for every pixel in the destination image, it traces back to where it came from in the source image.

Currently implemented: **2× scaling** (zoom out), but the matrix `A` is the real star here. Swap it out and you get rotation, shearing, reflection — whatever you want.

---

## How It Works

```
destination pixel → shift origin to center → apply A_inv → shift back → sample source pixel
```

The key idea: instead of pushing source pixels forward (which leaves holes), we pull destination pixels backward through the inverse transformation. Clean, no gaps.

```python
A = np.array([
    [2, 0],
    [0, 2]
])

A_inv = A.T  # inverse mapping
src_coord = A_inv @ coord_centered
```

---

## Setup

```bash
pip install numpy pillow matplotlib
```

Then drop your image in the same directory and update the filename in the script:

```python
image_path = os.path.join(dir, "your_image.jpeg")
```

Run it:

```bash
python transform.py
```

---

## Project Structure

```
.
├── transform.py       # main script
└── IMG_2031.jpeg      # sample image (swap with your own)
```

---

## Transformations You Can Try

Just change the `A` matrix:

```python
# Scale up 2x
A = np.array([[2, 0], [0, 2]])

# Rotate 45° (approx)
A = np.array([[0.707, -0.707], [0.707, 0.707]])

# Shear
A = np.array([[1, 0.5], [0, 1]])

# Reflect horizontally
A = np.array([[-1, 0], [0, 1]])
```

---

## Coming Soon

Got more ideas, just need time —

- [ ] Bilinear interpolation (smoother sampling, no pixelation)
- [ ] Interactive UI to tweak the matrix in real time
- [ ] Chaining multiple transformations
- [ ] Perspective / homography warps
- [ ] Animated transforms (watch the image morph)

---

## Requirements

- Python 3.x
- NumPy
- Pillow
- Matplotlib

---

## Why

Mostly to understand what's actually happening under the hood when libraries like OpenCV do `warpAffine`. Turns out it's just matrix math and careful indexing.
