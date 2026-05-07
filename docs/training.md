# Training

## Status

This repository already reserves the stable public training entrypoints:

```bash
python scripts/train.py --config configs/train.example.yaml
python scripts/play.py --config configs/play.example.yaml
```

The full training implementation has not been migrated into `SigLoMa-Code` yet. This document defines the intended environment and command layout so the public workflow is stable from the beginning.

## Recommended Environment

- Environment name: `sigloma`
- Python version: `3.10+`
- Simulator stack: `Isaac Gym`

## Setup Flow

### 1. Create and activate the training environment

```bash
conda create -n sigloma python=3.10
conda activate sigloma
```

### 2. Install Isaac Gym

Install `Isaac Gym` into the `sigloma` environment first. The exact package source and local verification steps should follow your internal GPU and driver setup.

> `Isaac Gym` installation notes will be refined here once the training code is fully migrated.

### 3. Clone and install `SigLoMa-Code`

```bash
git clone https://github.com/11chens/SigLoMa-Code.git
cd SigLoMa-Code
pip install -e .
```

### 4. Use the reserved public entrypoints

Train:

```bash
python scripts/train.py --config configs/train.example.yaml
```

Play:

```bash
python scripts/play.py --config configs/play.example.yaml
```

## What Will Live Here

The long-term goal is to keep the public training workflow inside this repository, including:

- environment setup for `Isaac Gym`
- task and experiment configuration
- training entrypoints
- evaluation or play entrypoints

## Pending Items

- migrate the real training implementation into this repository
- finalize package-level dependencies for the training stack
- replace example configs with the first public task configs
