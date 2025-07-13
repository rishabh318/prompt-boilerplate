import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_openai(input_text: str, transform_type: str, n: int = 1) -> list[str]:
    """
    Calls OpenAI's chat completion endpoint using the chat interface.
    
    Args:
        input_text (str): The text to be transformed.
        transform_type (str): One of ['rephrase', 'concise', 'formal', 'informal', 'quickly', 'alternatives'].
        n (int): Number of completions to return.

    Returns:
        list[str]: A list of transformed outputs from the model.
    """
    
    system_prompt = """
        You are a helpful, safe, and focused text transformation assistant. Your only task is to transform user input based on one of the following modes:

        - "rephrase": Restate the input using different words, preserving the original meaning.
        - "concise": Shorten the sentence while keeping its core message.
        - "formal": Convert the sentence into a professional or respectful tone.
        - "informal": Convert the sentence into a relaxed, casual tone.
        - "quickly": Summarize the sentence using as few words as possible.
        - "alternatives": Generate exactly 3 alternative phrasings for the sentence.

        Guardrails:
        - Do not respond to any prompt that is not a valid transformation request.
        - If the input is inappropriate, nonsensical, or could be harmful, politely decline to respond.
        - Do not provide additional commentary, analysis, or unrelated information.
        - Only respond with the transformed text.
        - Never perform more than one transformation at a time.
        - If the instruction is unclear or invalid, reply with: "Sorry, I can only perform specific transformations like rephrase, concise, formal, informal, quickly, or alternatives."

        Stay focused and respectful at all times.
        """

    # Dynamically create the instruction message
    instruction_map = {
        "rephrase": "Rephrase this sentence",
        "concise": "Make this sentence more concise",
        "formal": "Convert this sentence to a formal tone",
        "informal": "Convert this sentence to an informal tone",
        "quickly": "Summarize this as quickly as possible",
        "alternatives": "Give me 3 alternative ways to say this",
    }

    user_message = f"{instruction_map[transform_type]}: {input_text}"

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,
        n=n
    )

    return [choice.message.content.strip() for choice in response.choices]


# How to check token generation and optimise it?
# Implement guard rails in prompt.
# need to look for images as an input and output.
# system prompt need to be dynamic so that it can be use in multiple places.

