# Repository Map

This document explains how the public SigLoMa repositories relate to each other.

## Core Repositories

| Repository | Role | Used In | Notes |
| --- | --- | --- | --- |
| [`SigLoMa-Code`](https://github.com/11chens/SigLoMa-Code) | Top-level entry repository for training, docs, and workflow integration | Training, documentation | This repository keeps the public overview and the future training code entrypoints. |
| [`ros_base`](https://github.com/11chens/ros_base) | ROS2 Python framework for orchestration and modular project structure | Deployment foundation | Provides the manager-agent-handler-node architecture and the running ROS node wrappers used by the system. |
| [`SigLoMa-VLM`](https://github.com/11chens/SigLoMa-VLM) | High-level task orchestration, VLM logic, tracking, and bridge nodes | Real deployment | This repository is the current unified launch entry for the full SigLoMa runtime. |
| [`quad_deploy`](https://github.com/11chens/quad_deploy) | Low-level locomotion deployment and execution-side control | Real deployment | Owns the lower-level deployment and control path. |
| [`KalmanFilter`](https://github.com/11chens/KalmanFilter) | Standalone Kalman-filter implementation repository for sigma-points tracking | Deployment support | Installed separately. The current runtime launches `kf_sigma_node.py` from `ros_base`, and that ROS node calls into this repository for the underlying tracking algorithm. |

## Documentation Website

- [`ROS Base Documentation`](https://11chens.github.io/ros_base_doc/en/)

This is the project website for the framework itself. It explains:

- why `ROS Base` exists
- how the plugin-style structure works
- how `BaseManager`, `BaseNode`, `BaseAgent`, and `BaseHandler` interact
- how the same framework is used in `SigLoMa-VLM` and `quad_deploy`
