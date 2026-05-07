# SigLoMa-Code

SigLoMa-Code is the public entry repository for the SigLoMa system: training code, deployment guidance, and the full repository map built on top of `ROS Base`.

> [!TIP]
> **Project Website / Framework Docs**
>
> If you want to understand the framework behind the full system, the `ROS Base` documentation website is the best place to start:
> - English: <https://11chens.github.io/ros_base_doc/en/>
> - Chinese: <https://11chens.github.io/ros_base_doc/>
>
> **Why ROS Base**
> - Plugin-style project structure for reusable multi-module deployment
> - Mixed-frequency coordination across perception, control, state machines, and bridge nodes
> - Stable performance with efficient shared context and multi-process isolation

SigLoMa builds on top of that foundation to connect training, high-level VLM orchestration, low-level locomotion, filtering, and real-robot deployment into one reproducible workflow.

## Repository Map

1. [`SigLoMa-Code`](https://github.com/11chens/SigLoMa-Code): public entry repository for training code, workflow documentation, and installation guides.
2. [`ros_base`](https://github.com/11chens/ros_base): the underlying ROS2 Python framework used across the SigLoMa system.
3. [`ROS Base Documentation`](https://11chens.github.io/ros_base_doc/en/): the project website that explains the framework design, core concepts, and real examples.
4. [`SigLoMa-VLM`](https://github.com/11chens/SigLoMa-VLM): high-level task orchestration, VLM integration, visual tracking, and bridge logic.
5. [`quad_deploy`](https://github.com/11chens/quad_deploy): low-level locomotion deployment and execution-side control.
6. [`KalmanFilter`](https://github.com/11chens/KalmanFilter): standalone Kalman-filter implementation repository used by the ROS-side sigma-points tracking node.

More details are collected in [docs/repositories.md](docs/repositories.md).

## Quick Start

### 1. Clone this repository

```bash
git clone https://github.com/11chens/SigLoMa-Code.git
cd SigLoMa-Code
```

### 2. Choose a workflow

- Training setup and commands: see [docs/training.md](docs/training.md)
- Real-robot deployment: see [docs/deployment.md](docs/deployment.md)
- Hardware list and notes: see [docs/hardware.md](docs/hardware.md)

## Training Overview

Training is documented around a dedicated environment named `sigloma`.

The current workflow is:

1. Create and activate the `sigloma` environment.
2. Install `Isaac Gym` and follow the setup in [docs/training.md](docs/training.md).
3. Run the public training commands:

```bash
python scripts/train.py --config configs/train.example.yaml
python scripts/play.py --config configs/play.example.yaml
```

## Deployment Overview

Real-robot deployment is documented around a dedicated environment named `sigloma_run`.

Current deployment flow:

1. Connect to the robot with `ssh -X`
2. Install `isaac_ros_visual_slam`
3. Install the required SigLoMa repositories
4. Launch the unified SigLoMa entry from `SigLoMa-VLM`

```bash
ssh -X user@robot_ip
conda activate sigloma_run
cd ~/Project/SigLoMa-VLM
python launch/sigloma_launch.py
```

Recommended workflow notes:

- prefer `ssh -X` so you can launch remotely and still access the first-person image stream
- avoid opening VS Code directly on the robot during deployment, because the VS Code server can occupy a large amount of memory and reduce deployment efficiency
- use a high-bandwidth network card to keep the forwarded image stream responsive and stable

The current launcher automatically wires together `quad_deploy`, `SigLoMa-VLM`, `ros_base`, and the `VSLAM_DOCKER` session through `launch/launch_cfg.yaml`. Full details live in [docs/deployment.md](docs/deployment.md).

The two main VLM scripts are:

- `SigLoMa-VLM/sigloma_vlm/scripts/pick_place_run.py`
- `SigLoMa-VLM/sigloma_vlm/scripts/test_modules.py`

They are switched through the launcher node selection:

```bash
# Full pick-and-place workflow
python launch/sigloma_launch.py

# Single-stage module testing
python launch/sigloma_launch.py --disable VLM_LOGIC --enable VLM_TEST
```

After launch, the operator uses the real controller and the SigLoMa UI together:

- `pick_place_run.py`: finish all pick-target annotations first, press `Space`, then annotate the place target and press `Space` again
- `test_modules.py`: single-module testing, so each run only needs one manual box selection

## Hardware Notes

This section focuses on the current hardware list and connection notes:

- use a high-bandwidth network card on the robot side
- keep the gripper, its controller board, and the mounting parts documented as one reference setup
- connection diagrams and hardware photos are still being prepared

See [docs/hardware.md](docs/hardware.md) for the current structure and placeholders.

## Current Status

- `SigLoMa-VLM` is the current real deployment entrypoint.
- `SigLoMa-Code` reserves the public training entrypoints and the top-level integration docs.
- `ros_base` provides the running ROS node wrappers, while the underlying Kalman implementation is installed from [`KalmanFilter`](https://github.com/11chens/KalmanFilter).
- Some hardware assets and `isaac_ros_visual_slam` local modifications are still marked as pending.
