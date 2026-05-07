# Repository Map

This document explains how the public SigLoMa repositories relate to each other.

## Core Repositories

| Repository | Role | Used In | Notes |
| --- | --- | --- | --- |
| [`SigLoMa-Code`](https://github.com/11chens/SigLoMa-Code) | Top-level entry repository for training, docs, and workflow integration | Training, documentation | This repository keeps the public overview and the future training code entrypoints. |
| [`ros_base`](https://github.com/11chens/ros_base) | ROS2 Python framework for orchestration and modular project structure | Deployment foundation | Provides the manager-agent-handler-node architecture used by the system. |
| [`SigLoMa-VLM`](https://github.com/11chens/SigLoMa-VLM) | High-level task orchestration, VLM logic, tracking, and bridge nodes | Real deployment | This repository is the current unified launch entry for the full SigLoMa runtime. |
| [`quad_deploy`](https://github.com/11chens/quad_deploy) | Low-level locomotion deployment and execution-side control | Real deployment | Owns the lower-level deployment and control path. |
| [`KalmanFilter`](https://github.com/11chens/KalmanFilter) | Standalone filtering and state-estimation repository | Experiments, reference | Published independently from the current `sigloma_launch.py` runtime path. |

## Documentation Website

- [`ROS Base Documentation`](https://11chens.github.io/ros_base_doc/en/)

This is the project website for the framework itself. It explains:

- why `ROS Base` exists
- how the plugin-style structure works
- how `BaseManager`, `BaseNode`, `BaseAgent`, and `BaseHandler` interact
- how the same framework is used in `SigLoMa-VLM` and `quad_deploy`

## Boundary Summary

- `SigLoMa-Code` should not duplicate the full framework manual. It should point readers to the project website first.
- `SigLoMa-Code` should describe the end-to-end workflow across repositories.
- `SigLoMa-VLM` remains the practical deployment entrypoint until more code is migrated into this repository.
- `quad_deploy` and `ros_base` remain independently installable repositories.
- `KalmanFilter` remains a separate open repository rather than a hidden internal dependency.

## Historical Naming

`SigLoMa-VLM` was previously named `HomiQuad-VLM`. Public-facing documentation in this repository uses only the new `SigLoMa-VLM` name.
