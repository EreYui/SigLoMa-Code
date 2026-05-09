# Training

## Installation

### 1. Create and activate the training environment

Create a new Python virtual environment with Python 3.8:

```bash
conda create -n sigloma python=3.8
conda activate sigloma
```

### 2. Install Isaac Gym

- Download and install `Isaac Gym Preview 4` from [NVIDIA Developer](https://developer.nvidia.com/isaac-gym).
- Install the Python package:

```bash
cd isaacgym/python
pip install -e .
```

### 3. Install rsl_rl
- Clone this repository
- Install the package:
```bash
cd SigLoMaGym/rsl_rl && pip install -e .
```

### 4. Install legged_gym
```bash
cd ../ && pip install -e .
```

## Usage

### Training

```bash
python legged_gym/scripts/train.py --headless
```

### Testing

```bash
python legged_gym/scripts/play.py
```
