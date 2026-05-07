# Deployment

## Start With the Framework Docs

Before following the deployment commands, read the framework overview:

- English: <https://11chens.github.io/ros_base_doc/en/>
- Chinese: <https://11chens.github.io/ros_base_doc/>

That documentation explains the manager-agent-handler-node structure used by the SigLoMa deployment stack.

## Recommended Environment

- Environment name: `sigloma_run`
- Workspace root in the current launcher config: `~/Project`
- ROS setup in the current launcher config: `~/unitree_ros2/setup_id1.sh`

## Environment Setup

### 1. Install ROS2 in the deployment environment

The current SigLoMa repositories assume a ROS2-capable Python environment. `RoboStack` is a practical option when you want ROS2 inside a virtual environment instead of the system Python.

### 2. Install `isaac_ros_visual_slam`

Official repository:

- <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam>

This module should be installed before the rest of the real-robot pipeline.

> Local configuration changes and helper scripts for `isaac_ros_visual_slam` are still pending and will be added here later.

### 3. Install the required SigLoMa repositories

```bash
cd ~/Project
git clone https://github.com/11chens/ros_base.git
git clone https://github.com/11chens/quad_deploy.git
git clone https://github.com/11chens/SigLoMa-VLM.git
```

Install the Python packages:

```bash
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

## What the Current Launcher Starts

The current `SigLoMa-VLM/launch/launch_cfg.yaml` is designed to orchestrate:

- `RL_CONTROL` from `quad_deploy`
- `VLM_LOGIC` from `SigLoMa-VLM`
- `VLM_TEST` from `SigLoMa-VLM` as an optional test target
- `KALMAN_NODE` from `ros_base`
- `VIS_NODE` from `SigLoMa-VLM`
- `VSLAM_DOCKER` as a separate VSLAM session

The launcher configuration already contains a dedicated `conda_env` and `ros_setup`, so the runtime flow is designed to source the ROS2 environment automatically as part of the orchestration process.

## Notes on `KalmanFilter`

`KalmanFilter` is published as an independent repository for state-estimation work and experiments. The current `sigloma_launch.py` deployment path launches the Kalman node from `ros_base`, not from the standalone `KalmanFilter` repository.

## Pending Items

- document the recommended `isaac_ros_visual_slam` local patches and helper scripts
- add troubleshooting notes for the deployment environment
- document optional visualization and logging workflows in more detail
