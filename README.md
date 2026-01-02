# LLM-Prompting-Assignment

A hands-on assignment focused on integrating Google Gemini AI. Includes API implementation, response handling, and multimodal data processing.
## Project Overview
The project consists of **two main experiments**:
1. **Text Generation Experiments**
   - Blog introduction generation
   - Product description generation
   - Short story generation
   - Parameter tuning for creativity vs determinism
2. **Multimodal Generation Experiments**
   - Image + text prompts
   - Interior design suggestions
   - Diagram explanation
   - Food recipe generation from images
---
##  Tech Stack
- **Language:** Python 3.10+
- **LLM:** Google Gemini
- **SDK:** `google-genai`
- **Image Processing:** Pillow (PIL)
- **Environment Management:** `python-dotenv`
---
##  Installation
1. Clone the repository
    ```bash
        git clone https://github.com/kunaltyagi-crossml/LLM-Prompting-Assignment.git
        cd gemini-generation-experiments
2. Create and activate a virtual environment (recommended)
    ```bash
        python -m venv venv
        source venv/bin/activate
3. Install dependencies
    ```bash
        pip install google-genai pillow python-dotenv
4.  Set up your GEMINI_API_KEY:
    
    Create a file named .env in the root directory of this project. Add the following line to the .env file, replacing YOUR_API_KEY with your actual Gemini API key:
      
        api_key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)
5. Usage
    1. Text Generation Experiment
      This script explores how different prompts and parameters affect generated text.
          python Assignment1.py
      Prompts Used:
        -  Technical blog introduction
        -  Product description from bullet points
        -  Short story generation
      Parameters Tuned:
        -  temperature
        -  top_p
        -  max_output_tokens
     2. Multimodal (Image + Text) Generation
        This script uses images + prompts to generate contextual responses.
            python Assignment2.py
     Examples:
        -  Interior design suggestions from a room image
        -  Explaining a flowchart step
        -  Creating a vegan fusion recipe from food images
     Parameters Tuned:
        -  temperature
        -  top_p
        -  top_k
## Learning Outcomes
  -  Understand the impact of temperature on creativity
  -  Compare top_p vs top_k sampling
  -  Learn how Gemini handles multimodal inputs
  -  Build intuition for prompt engineering