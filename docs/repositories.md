# Repository Map

This document explains how the public SigLoMa repositories relate to each other.

The key point is that `ros_base`, `quad_deploy`, and `KalmanFilter` are not internal-only modules for SigLoMa. They are designed to run independently, be developed independently, and support other robotics projects through a decoupled architecture.

## Standalone Foundation Repositories

| Repository | Role | Used In | Notes |
| --- | --- | --- | --- |
| [`ros_base`](https://github.com/11chens/ros_base) | ROS2 Python framework for orchestration and modular project structure | General robotics foundation | Provides the manager-agent-handler-node architecture and the running ROS node wrappers used by the system. |
| [`quad_deploy`](https://github.com/11chens/quad_deploy) | Plugin-style quadruped reinforcement-learning deployment framework | Reusable deployment | Built on `ros_base`, supports both low-level joint control and high-level command control, and is designed to be reusable across quadruped projects. |
| [`KalmanFilter`](https://github.com/11chens/KalmanFilter) | Standalone Kalman-filter development repository | Reusable state-estimation development | Supports solution testing, simulation, visualization, frequency amplification, and delay compensation. In the current runtime, `kf_sigma_node.py` from `ros_base` calls into this repository for the underlying tracking algorithm. |

## Project Documentation Website

| Resource | Role | Notes |
| --- | --- | --- |
| [`ROS Base Documentation`](https://11chens.github.io/ros_base_doc/en/) | Framework documentation website | Explains the framework design, core concepts, and real application examples. |

## SigLoMa Application Repositories

| Repository | Role | Used In | Notes |
| --- | --- | --- | --- |
| [`SigLoMa-VLM`](https://github.com/11chens/SigLoMa-VLM) | High-level task orchestration, VLM logic, tracking, and bridge nodes | Real deployment | This repository is the current unified launch entry for the full SigLoMa runtime. |
| [`SigLoMa-Code`](https://github.com/11chens/SigLoMa-Code) | Top-level entry repository for training, docs, and workflow integration | Training, documentation | This repository keeps the public overview and the future training code entrypoints. |
