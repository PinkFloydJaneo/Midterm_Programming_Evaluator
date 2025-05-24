# Gemma3 Vision Insight Script

This Python script, `program_eval.py`, analyzes an image containing C program code and evaluates it based on specified criteria. It is designed to provide insights into the correctness, readability, elegance, and adherence to assignment specifications of the code.

## Description

`program_eval.py` takes an image file as input, which should contain a C program. The script encodes the image to a base64 string and sends it to a local API endpoint for analysis. The API evaluates the code based on the following criteria:

* **Program Correctness:** Determines if the program works correctly on all inputs and adheres to specifications.
* **Readability:** Assesses the clarity of variable and function names, organization of code, and formatting.
* **Code Elegance:** Evaluates the efficiency and structure of the code, avoiding redundancy.
* **Assignment Specifications:** Checks if the program follows the required specifications.

**Note:** The accuracy of the evaluation depends on the quality of the input image and the clarity of the text within it. Clear, well-formatted images will yield the best results.

## Usage

To run the script, use the following command in your terminal:

```bash
python program_eval.py <image_file.jpg>
```
## Note!

This script utilizes the Ollama API for code evaluation. Ensure that the API is running locally at http://localhost:11434/api/generate before executing the script.
