# Deployment

## Framework Overview

If you want the architecture behind the deployment stack, the framework docs are a helpful reference:

- English: <https://11chens.github.io/ros_base_doc/en/>
- Chinese: <https://11chens.github.io/ros_base_doc/>

That documentation explains the manager-agent-handler-node structure used by the SigLoMa deployment stack.

## Recommended Environment

- Environment name: `sigloma_run`
- Workspace root in the current launcher config: `~/Project`
- ROS setup in the current launcher config: `~/unitree_ros2/setup_id1.sh`

## Environment Setup

### Recommended Connection Method

For real deployment, it is recommended to connect to the robot with `ssh -X` and launch the system remotely:

```bash
ssh -X user@robot_ip
```

This workflow is recommended because:

- `ssh -X` keeps the deployment workflow lightweight on the robot
- X11 forwarding provides the first-person image stream needed by the SigLoMa UI
- a high-bandwidth network card helps keep the image transmission responsive and stable

It is not recommended to open VS Code directly on the robot during deployment, because the VS Code server can consume a large amount of memory and reduce deployment efficiency.

### 1. Install ROS2 in the deployment environment

The current SigLoMa repositories assume a ROS2-capable Python environment. `RoboStack` is a practical option when you want ROS2 inside a virtual environment instead of the system Python.

### 2. Install `isaac_ros_visual_slam`

Official repository:

- <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam>

This repository provides the real-time camera pose used by the Kalman pipeline and by the world-coordinate computation for target objects.

> Local configuration changes and helper scripts for `isaac_ros_visual_slam` are still pending and will be added here later.

### 3. Install the required SigLoMa repositories

```bash
cd ~/Project
git clone https://github.com/11chens/KalmanFilter.git
git clone https://github.com/11chens/ros_base.git
git clone https://github.com/11chens/quad_deploy.git
git clone https://github.com/11chens/SigLoMa-VLM.git
```

Install the Python packages:

```bash
cd ~/Project/KalmanFilter
pip install -e .

cd ~/Project/ros_base
pip install -e .

cd ~/Project/quad_deploy
pip install -e .

cd ~/Project/SigLoMa-VLM
pip install -e .
```

## Unified Launch Entry

The current real deployment entrypoint lives in `SigLoMa-VLM`:

```bash
conda activate sigloma_run
cd ~/Project/SigLoMa-VLM
python launch/sigloma_launch.py
```

The VLM runtime scripts are located in:

- `SigLoMa-VLM/sigloma_vlm/scripts/pick_place_run.py`
- `SigLoMa-VLM/sigloma_vlm/scripts/single_module_run.py`

The launcher switches between these modes through node selection in `launch/launch_cfg.yaml`:

- `VLM_PICK_PLACE` runs `sigloma_vlm/scripts/pick_place_run.py`
- `VLM_SINGLE` runs `sigloma_vlm/scripts/single_module_run.py`

Example commands:

```bash
# Full pick-and-place workflow
python launch/sigloma_launch.py

# Standalone single-module run
python launch/sigloma_launch.py --disable VLM_PICK_PLACE --enable VLM_SINGLE
```

## What the Current Launcher Starts

The current `SigLoMa-VLM/launch/launch_cfg.yaml` is designed to orchestrate:

- `RL_CONTROL` from `quad_deploy`
- `VLM_PICK_PLACE` from `SigLoMa-VLM`
- `VLM_SINGLE` from `SigLoMa-VLM` as an optional standalone target
- `KALMAN_NODE` from `ros_base`
- `VIS_NODE` from `SigLoMa-VLM`
- `VSLAM_DOCKER` as a separate VSLAM session

The launcher configuration already contains a dedicated `conda_env` and `ros_setup`, so the runtime flow is designed to source the ROS2 environment automatically as part of the orchestration process.

`KALMAN_NODE` is the ROS-side node wrapper from `ros_base`, while its underlying Kalman tracking implementation comes from the separately installed [`KalmanFilter`](https://github.com/11chens/KalmanFilter) repository.

## After Launch

After the launcher starts, the current interactive flow includes both robot control and target selection.

### UI Selection Workflows

`single_module_run.py` is intended for standalone pick or place runs:

1. Drag the mouse once to select the current target.
2. Press `Enter` to confirm the selection.
3. The script then runs the single selected pick or place module.

`pick_place_run.py` is the full pick-and-place workflow:

1. Use the UI to drag and confirm all pick targets one by one.
2. Press `Space` after all pick targets have been collected.
3. Then drag and confirm the place target.
4. Press `Space` again to finish the annotation stage.

### Real-Robot Controller Flow

For the real robot, locomotion and safety switching are handled with the wireless controller:

1. Press `L1` to recover and stand up if the robot is in shutdown mode.
2. After the robot becomes stable, press `X` to switch from cold start or recovery into RL teleoperation.
3. Use `R2` to enter remote-control mode and turn autonomous control off.
4. Use `R1` to enter automatic control mode. This publishes `rl_ready` and allows the full SigLoMa execution flow to start.
5. Use `L2` to shut down the motors and make the robot lie down immediately if needed.

During the VLM workflow, the VLM side can finish target anchoring first and then wait for `rl_ready`. The robot only enters the actual automatic run after the `R1` action has enabled autonomous control.

The VLM rotation stages in `pick_place_run.py` explicitly wait for `rl_ready`, so annotation and autonomous execution are separated by design.

## Notes on `KalmanFilter`

`KalmanFilter` is published as an independent repository that provides the underlying Kalman filter implementation. The current `sigloma_launch.py` deployment path launches `kf_sigma_node.py` from `ros_base`, and that ROS node calls into the `KalmanFilter` package for the actual tracking algorithm.

## Pending Items

- document the recommended `isaac_ros_visual_slam` local patches and helper scripts
- add troubleshooting notes for the deployment environment
- document the full operator workflow in more detail for later public release
