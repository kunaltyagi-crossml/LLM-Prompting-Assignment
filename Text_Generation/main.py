import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load API Key


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")


# Initialize Gemini Client


client = genai.Client(api_key=api_key)


# Text Generation Function


def generate_text(prompt, temperature, top_p, max_tokens):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt],
        config=types.GenerateContentConfig(
            temperature=temperature,
            top_p=top_p,
            max_output_tokens=max_tokens
        )
    )
    return response.text


# Prompts

blog_prompt = (
    "Write an introduction for a blog explaining the basics "
    "of Git version control for beginners."
)

product_prompt = (
    "Create a compelling product description using the following points:\n"
    "- Wireless noise-cancelling headphones\n"
    "- 40-hour battery life\n"
    "- Bluetooth 5.3\n"
    "- Fast charging support"
)

story_prompt = (
    "Write a short science-fiction story starting with:\n"
    "'The robot paused before making its final decision.'"
)


# Generate Outputs

if __name__ == "__main__":

    print("\n=== BLOG INTRO (Low Temperature) ===")
    print(generate_text(
        blog_prompt,
        temperature=0.2,
        top_p=0.9,
        max_tokens=1000
    ))

    print("\n=== PRODUCT DESCRIPTION (Medium Temperature) ===")
    print(generate_text(
        product_prompt,
        temperature=0.6,
        top_p=0.9,
        max_tokens=1000
    ))

    print("\n=== SHORT STORY (High Temperature) ===")
    print(generate_text(
        story_prompt,
        temperature=0.9,
        top_p=1.0,
        max_tokens=1000
    ))

