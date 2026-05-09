# SigLoMa-Code

SigLoMa-Code is the public entry repository for the SigLoMa system: training code, deployment guidance, and the full repository map built on top of a reusable robotics ecosystem centered on `ros_base`, `quad_deploy`, and `KalmanFilter`.

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

SigLoMa builds on top of that foundation to connect training, high-level VLM orchestration, reusable locomotion deployment, Kalman-filter integration, and real-robot deployment into one reproducible workflow.

## Core Reusable Repositories

These repositories are not only for SigLoMa. They are intentionally decoupled, can run independently, and are designed to be reused and extended in other robotics projects.

1. [`ros_base`](https://github.com/11chens/ros_base): a ROS2 Python framework for plugin-style robot-system management, built for multi-module integration across different frequencies such as perception, control, and state-machine logic.
2. [`quad_deploy`](https://github.com/11chens/quad_deploy): a `ros_base`-based quadruped reinforcement-learning deployment framework with a plugin-style architecture, designed to be reusable and extensible for both low-level joint control and high-level command control.
3. [`KalmanFilter`](https://github.com/11chens/KalmanFilter): a standalone Kalman-filter development repository for robot-system integration, simulation, visualization, and solution testing, with built-in support for frequency amplification and delay compensation.

## Repository Map

1. [`SigLoMa-Code`](https://github.com/11chens/SigLoMa-Code): public entry repository for training code, workflow documentation, and installation guides.
2. [`ros_base`](https://github.com/11chens/ros_base): the reusable ROS2 Python framework that provides the system architecture used by SigLoMa and other robotics projects.
3. [`quad_deploy`](https://github.com/11chens/quad_deploy): the reusable quadruped RL deployment framework for low-level and high-level locomotion control.
4. [`KalmanFilter`](https://github.com/11chens/KalmanFilter): the reusable Kalman-filter development repository for simulation, visualization, and robot-side integration.
5. [`ROS Base Documentation`](https://11chens.github.io/ros_base_doc/en/): the project website that explains the framework design, core concepts, and real examples.
6. [`SigLoMa-VLM`](https://github.com/11chens/SigLoMa-VLM): high-level task orchestration, VLM integration, visual tracking, and bridge logic for the SigLoMa application layer.

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
python legged_gym/scripts/train.py --headless
python legged_gym/scripts/play.py
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
- `SigLoMa-VLM/sigloma_vlm/scripts/single_module_run.py`

They are switched through the launcher node selection:

```bash
# Full pick-and-place workflow
python launch/sigloma_launch.py

# Standalone single-module run
python launch/sigloma_launch.py --disable VLM_PICK_PLACE --enable VLM_SINGLE
```

After launch, the operator uses the real controller and the SigLoMa UI together:

- `pick_place_run.py`: finish all pick-target annotations first, press `Space`, then annotate the place target and press `Space` again
- `single_module_run.py`: standalone pick or place execution, so each run only needs one manual box selection

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