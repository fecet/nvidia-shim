import sys

try:
    import nvshmem

    sys.modules["nvidia.nvshmem"] = nvshmem
except ImportError:
    pass
