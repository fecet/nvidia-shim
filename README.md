# NVIDIA Shim

A compatibility layer for handling NVIDIA package differences between PyPI and Conda distributions.

## Overview

This package provides import compatibility shims for NVIDIA-related Python packages that have different namespace structures between PyPI and Conda package managers.

## Features

- **NVIDIA NVSHMEM**: Maps `nvshmem` package to `nvidia.nvshmem` namespace
- **Flash Attention**: Maps `flash_attn_interface` to `flash_attn_3.flash_attn_interface` namespace

## How it works

The shim modifies `sys.modules` to redirect imports:
1. Attempts to import the actual underlying packages
2. Maps them to expected namespaces if successful
3. Gracefully handles missing packages
