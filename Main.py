import subprocess
from Models import Models

# ==== Configuration ====
MODEL_NAME = Models.QWEN25_72B.value
PORT = "8190"
GPUS = "6,7"
VRAM_LIMIT = "0.9"
BATCH_SIZE = "150"
MAX_TOKENS = "3000"

# Optional Settings
DTYPE = "float16"  # Default: float16
QUANTIZATION = ""  # fp8
   

# ==== Derived Values ====
NUM_GPUS = str(len(GPUS.split(",")))

# ==== Build Command ====
command = [
    "vllm", "serve", MODEL_NAME,
    "--port", PORT,
    "--gpu-memory-utilization", VRAM_LIMIT,
    "--tensor-parallel-size", NUM_GPUS,
    "--max_num_seqs", BATCH_SIZE,
    "--max-num-batched-tokens", MAX_TOKENS,
]

# ==== Logic: Quantization > Dtype > Default ====
if QUANTIZATION and DTYPE:
    print(f"Cant Set Both - Set On Default Mode: float16")
elif QUANTIZATION:
    command.extend(["--quantization", QUANTIZATION])
    print(f"Quantization Mode: {QUANTIZATION}")
elif DTYPE:
    command.extend(["--dtype", DTYPE])
    print(f"Dtype Mode: {DTYPE}")
else:
    command.extend(["--dtype", "float16"])
    print(f"Default Mode: float16")

# ==== Environment Variables ====
env = {
    "CUDA_VISIBLE_DEVICES": GPUS,
    **subprocess.os.environ
}

# ==== Run Command ====
try:
    print("Running Command:")
    print(" ".join(command))
    subprocess.run(command, check=True, env=env)
except subprocess.CalledProcessError as e:
    print(f"Error While Running The Command:\n{e}")
