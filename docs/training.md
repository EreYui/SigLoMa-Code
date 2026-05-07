# Training

The current public training commands are:

```bash
python scripts/train.py --config configs/train.example.yaml
python scripts/play.py --config configs/play.example.yaml
```

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

### 3. Clone `SigLoMa-Code`

```bash
git clone https://github.com/11chens/SigLoMa-Code.git
cd SigLoMa-Code
```

## Usage

### Training

```bash
python scripts/train.py --config configs/train.example.yaml
```

### Testing

```bash
python scripts/play.py --config configs/play.example.yaml
```
