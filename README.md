# Sentence Laundry (문장세탁기) 🧺

[![Korean README](https://img.shields.io/badge/README-Korean-green.svg)](README_KR.md)

Sentence Laundry is a playful translation tool that "washes" your sentences through a cycle of multiple languages. By exploiting differences in word order, grammar, and nuance between languages, it returns your sentence with a completely new (and often hilarious) meaning.

## Key Features

- **Standard Wash**: Translates through a fixed chain of languages (e.g., English -> Korean -> Japanese -> English).
- **Random Spin**: Injects random languages (German, Arabic, Vietnamese, etc.) into the cycle for unpredictable chaos.
- **Laundry Score**: A metric showing how "cleanly" your sentence was washed (how much it differs from the original).
- **Virtual Environment Support**: Isolated execution using `venv`.

## 🚀 How to Run

### Installation
```bash
# Create virtual environment
python3 -m venv venv

# Activate environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

**Run CLI translator:**
```bash
# Directly test the core logic
python3 translator.py
```

**Run API server:**
```bash
# Start FastAPI server
python3 main.py
```
The server runs on `http://0.0.0.0:8001`.

## API Endpoints

### 1. `POST /wash` : Standard Wash
Translates through a defined or custom chain.
*   **Request Body**:
    ```json
    {
      "text": "Text to wash (required)",
      "chain": ["en", "ja"] (optional, default: en->ja->ko)
    }
    ```

### 2. `POST /random-spin` : Random Spin
Randomizes intermediate languages for maximum distortion.
*   **Request Body**:
    ```json
    {
      "text": "Text to wash (required)",
      "random_count": 3 (optional, default: 2)
    }
    ```

### Response Structure (Common)
Returns a detailed "Laundry Report":
```json
{
  "original": "Original text",
  "laundered_result": "Final washed text",
  "chain": ["ko", "en", "ja", "ko"],
  "steps": [
    { "src": "ko", "dest": "en", "text": "..." },
    ...
  ],
  "metrics": {
    "length_diff": 4,
    "similarity": 0.71,
    "laundry_score": 28.57
  }
}
```

---
"Why laundry? Because we wash the stains (original meaning) right out of your sentences!"
