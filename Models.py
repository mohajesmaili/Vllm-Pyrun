from enum import Enum

class Models(Enum):
    GEMMA3 = "google/gemma-3-27b-it"
    DEEPSEEK_R1 = "deepseek-ai/DeepSeek-R1"
    DEEPSEEK_V3 = "deepseek-ai/DeepSeek-V3"
    OLM_OCR = "allenai/olmOCR-7B-0225-preview"
    QWEN25_3B = "Qwen/Qwen2.5-VL-3B-Instruct"
    QWEN25_7B = "Qwen/Qwen2.5-VL-7B-Instruct"
    QWEN25_32B = "Qwen/Qwen2.5-VL-32B-Instruct"
    QWEN25_72B = "Qwen/Qwen2.5-VL-72B-Instruct"
