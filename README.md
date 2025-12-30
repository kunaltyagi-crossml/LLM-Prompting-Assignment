# LLM-Prompting-Assignment
LLM Integration Assignment focused on text generation, prompt engineering, and parameter tuning using a generative AI API such as Gemini.



📘 Part 1 — Text Generation
What happens in this part?

In this section, the AI model generates text-only responses based on different prompts.
The goal is to understand how changing generation parameters affects the AI’s output.

📝 Prompts Used

The following three types of prompts are used:

Blog Introduction
→ Introduction explaining Git version control for beginners

Product Description
→ Description of wireless noise-cancelling headphones using bullet points

Short Science-Fiction Story
→ Story generated from a single starting sentence

⚙️ Parameters Explained
Parameter	Meaning
temperature	Controls creativity and randomness
top_p	Controls diversity of word selection
max_tokens	Maximum length of the generated text
🔍 Example Behavior

Low temperature → More factual, safe, and consistent output

High temperature → More creative, imaginative, and varied output

🎯 Learning Outcome

By comparing outputs with different parameter values, we clearly understand how AI behavior changes in terms of creativity, repetition, and consistency.

📙 Part 2 — Multimodal Prompting (Image + Text)
What is Multimodal AI?

Multimodal AI can understand both images and text together, allowing richer and more contextual responses.

🧪 Tasks Performed
🏠 Interior Design

Input: Room image + design preferences

Output: Modern, budget-friendly interior design suggestions

🧠 Diagram Explanation

Input: Neural network diagram image

Output: Beginner-friendly explanation of how the network works

🍲 Food Recipe Generation

Input: Food image + dietary constraints

Output: Healthy vegetarian recipe suitable for an Indian diet

⚙️ Parameters Tuned

temperature

top_p

top_k

Each parameter is adjusted to observe changes in creativity, accuracy, and consistency.

🎯 Learning Outcome

This section demonstrates how image context, text prompts, and parameter tuning together influence the quality and relevance of AI responses.

📊 Overall Learnings

Low creativity → More accurate and consistent responses

High creativity → More diverse and imaginative responses

Well-written prompts → Better AI outputs

Multimodal AI → Better understanding compared to text-only AI