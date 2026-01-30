import torch

# Check for Apple Silicon GPU support
if torch.backends.mps.is_available():
    mps_device = torch.device("mps")
    print(f"Success: MPS device found. Using: {torch.device(mps_device)}")
else:
    print("MPS not available. Using CPU.")
    