import base64
import requests
import json
import sys

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b"  # Change if you're using a different name

def encode_image_to_base64(image_path):
    """Encodes an image file to base64 string."""
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded

def query_gemma3_vision(image_path, prompt=\
    # "Programming Question: Write a C program that defines a function to compute the sum of elements in a fixed-size array of integers. The array contains exactly 5 integers.\
    "Task: Evaluate the attached C program code based on the following Evaluation Criteria for the Visual Input. \
    The program is to write a C program that defines a function to compute the sum of elements in a fixed-size array of integers. The array contains exactly 5 integers. \
    Don't forget to print the total points gained base on the scoring guidelines\
    Evaluation Criteria for the Visual Input\
        Program Correctness: Your program should work correctly on all inputs. Also, if there are any specifications about how the program should be written or how the output should appear, those specifications should be followed. \
        Readability: Variables and functions should have meaningful names. Code should be organized into functions/methods where appropriate. There should be an appropriate amount of white space so that the code is readable, and indentation should be consistent. \
        Code Elegance: There are many ways to write the same functionality into your code, some of which are needlessly slow or complicated. For example, if you are repeating the same code, it should be inside a new method/function or a for loop. \
        Assignment Specifications: The assignment will likely ask you to include certain information as comments or save your program with a certain file name, or other such specifications. These tasks fall under “assignment specifications.\
    Scoring Method and Rubrics\
        Scoring Guidelines:\
            Program Correctness (10 points):\
                10 points: Program works flawlessly on all test cases and meets all specifications.\
                7 points: Minor issues present, but the program generally works as intended.\
                4 points: Major issues that affect functionality, but some parts work correctly.\
                1 point: The program does not work or fails to meet basic requirements.\
            Readability (5 points):\
                5 points: Code is very readable with clear naming conventions and proper organization.\
                3 points: Code is mostly readable but may have some minor issues with naming or organization.\
                1 point: Code is difficult to read due to poor naming, organization, or inconsistent formatting.\
                0 points: Code is unreadable.\
            Code Elegance (3 points):\
                3 points: Code is efficient, well-structured, and avoids redundancy.\
                2 points: Some redundancy or inefficiency present, but overall structure is acceptable.\
                1 point: Significant redundancy or inefficiency; code is overly complicated.\
                0 points: Code lacks elegance and is poorly structured.\
            Assignment Specifications (2 points):\
                2 points: All specifications are followed precisely.\
                1 point: Most specifications are followed, but some minor details are missed.\
                0 points: Major specifications are not followed\
    "):
    
    image_base64 = encode_image_to_base64(image_path)

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "images": [image_base64],
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "No response text returned.")

    except requests.RequestException as e:
        return f"Request failed: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gemma3_vision_insight.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    insights = query_gemma3_vision(image_path)
    print("=== Insights Extracted ===")
    print(insights)


 