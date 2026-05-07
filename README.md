# SigLoMa-Code

SigLoMa-Code is the public entry repository for the SigLoMa system: training code, deployment guidance, and the full repository map built on top of `ROS Base`.

> [!IMPORTANT]
> **Project Website / Framework Docs**
>
> Before deployment, start from the framework docs:
> - English: <https://11chens.github.io/ros_base_doc/en/>
> - Chinese: <https://11chens.github.io/ros_base_doc/>
>
> `ROS Base` is not just a dependency. It is the framework that explains how SigLoMa organizes VLM, locomotion, filtering, bridge nodes, and VSLAM into one mixed-frequency robotic system.

## Why ROS Base, Why SigLoMa

`ROS Base` is an open-source ROS2 Python framework designed for complex robotic systems. It gives SigLoMa a clean way to organize:

- plugin-style project structure
- mixed-frequency modules for perception, control, state machines, and hardware bridges
- efficient shared context inside one main process
- multi-process expansion when a module should be isolated for performance

SigLoMa builds on top of that foundation to connect training, high-level VLM orchestration, low-level locomotion, filtering, and real-robot deployment into one reproducible workflow.

## Repository Map

1. [`SigLoMa-Code`](https://github.com/11chens/SigLoMa-Code): public entry repository for training code, workflow documentation, and installation guides.
2. [`ros_base`](https://github.com/11chens/ros_base): the underlying ROS2 Python framework used across the SigLoMa system.
3. [`ROS Base Documentation`](https://11chens.github.io/ros_base_doc/en/): the project website that explains the framework design, core concepts, and real examples.
4. [`SigLoMa-VLM`](https://github.com/11chens/SigLoMa-VLM): high-level task orchestration, VLM integration, visual tracking, and bridge logic.
5. [`quad_deploy`](https://github.com/11chens/quad_deploy): low-level locomotion deployment and execution-side control.
6. [`KalmanFilter`](https://github.com/11chens/KalmanFilter): standalone state-estimation module and filtering experiments.

More details are collected in [docs/repositories.md](docs/repositories.md).

## Quick Start

### 1. Read the framework docs first

If you want to understand why the system is organized this way, start with the project website:

- <https://11chens.github.io/ros_base_doc/en/>

That documentation explains the `BaseManager`, `BaseNode`, `BaseAgent`, and `BaseHandler` model that SigLoMa uses for deployment orchestration.

### 2. Clone this repository

```bash
git clone https://github.com/11chens/SigLoMa-Code.git
cd SigLoMa-Code
```

### 3. Install the local Python package

```bash
pip install -e .
```

### 4. Choose a workflow

- Training path: see [docs/training.md](docs/training.md)
- Real-robot deployment path: see [docs/deployment.md](docs/deployment.md)
- Hardware notes and pending assets: see [docs/hardware.md](docs/hardware.md)

## Training Overview

Training is documented around a dedicated environment named `sigloma`.

The current public entrypoints are reserved as:

```bash
python scripts/train.py --config configs/train.example.yaml
python scripts/play.py --config configs/play.example.yaml
```

The command shape is already fixed, but the full training stack is still being migrated into this repository. See [docs/training.md](docs/training.md) for the planned setup and current placeholder status.

## Deployment Overview

Real-robot deployment is documented around a dedicated environment named `sigloma_run`.

Current deployment flow:

1. Install `isaac_ros_visual_slam`
2. Install the required SigLoMa repositories
3. Activate the deployment environment
4. Launch the unified SigLoMa entry from `SigLoMa-VLM`

```bash
conda activate sigloma_run
cd ~/Project/SigLoMa-VLM
python launch/sigloma_launch.py
```

The current launcher automatically wires together `quad_deploy`, `SigLoMa-VLM`, `ros_base`, and the `VSLAM_DOCKER` session through `launch/launch_cfg.yaml`. Full details live in [docs/deployment.md](docs/deployment.md).

## Hardware Notes

The current documentation assumes the existing real-robot setup. Highlights:

- use a high-bandwidth network card on the robot side
- keep the gripper and STM32 controller documented as a concrete reference setup
- connection diagrams and hardware photos are still being prepared

See [docs/hardware.md](docs/hardware.md) for the current structure and placeholders.

## Current Status

- `SigLoMa-VLM` is the current real deployment entrypoint.
- `SigLoMa-Code` reserves the public training entrypoints and the top-level integration docs.
- Some hardware assets and `isaac_ros_visual_slam` local modifications are still marked as pending.
