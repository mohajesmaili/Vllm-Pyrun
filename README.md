# VLLM Runner

A lightweight Python script to easily launch VLLM models using subprocess.  
This script is designed for quick setup of large language models (LLMs) with customizable GPU, memory, and batching options.

---

## Features

- Easily configure **model name**, **GPU devices**, **VRAM limits**, and **batch sizes**.
- Supports **dtype selection** or **quantization modes**.
- Dynamically builds the `vllm serve` command.
- Uses `subprocess` to run the model in a separate system process.
- Automatically sets environment variables like `CUDA_VISIBLE_DEVICES`.

---

## Configuration

Inside the Python script, you can customize:

| Variable         | Purpose                                      | Example Value        |
|------------------|----------------------------------------------|----------------------|
| `MODEL_NAME`     | Name of the model to launch via VLLM         | `Model Name`         |  
| `PORT`           | Server port number                           | `9000`               |
| `GPUS`           | GPU IDs to use (comma-separated)             | `0,1,2,3,4`          |
| `VRAM_LIMIT`     | Maximum GPU memory utilization (0~1)         | `0.9`                |
| `BATCH_SIZE`     | Maximum number of concurrent sequences       | `100`                |
| `MAX_TOKENS`     | Maximum tokens per batch                     | `3000`               |
| `DTYPE`          | Floating point type (Default: `float16`)     | `float16`            |
| `QUANTIZATION`   | Quantization mode (Example: `fp8`)           | `"fp8"`              |

---

## Logic

- If both `QUANTIZATION` and `DTYPE` are set, the script forces `float16` mode and warns the user.
- If only `QUANTIZATION` is set, the model will run in quantized mode.
- If only `DTYPE` is set, the model will run with the specified data type.
- Otherwise, it defaults to `float16`.

---

## How To Run

1. Install `vllm` in your environment:
    ```bash
    pip install vllm
    ```

2. Adjust the configuration section in the script to match your system.

3. Run the script:
    ```bash
    python run_vllm.py
    ```

4. If successful, your model will be served on the defined port (`PORT`) and ready to accept inference requests.

---

## Error Handling

If the subprocess fails, the script will catch the error and print the error details in the terminal:

