import sys

try:
    import flash_attn_interface

    sys.modules["flash_attn_3.flash_attn_interface"] = flash_attn_interface
except ImportError:
    pass
