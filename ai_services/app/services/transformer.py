from app.core.openai_client import call_openai
from app.enums.transform_type import TransformType


def transform_text(input_text: str, transform_type: TransformType) -> list[str]:
    """
    Transforms input text using OpenAI based on the given transform_type.
    
    Args:
        input_text (str): The text to transform.
        transform_type (str): The type of transformation to apply.

    Returns:
        list[str]: Transformed text results.
    """
    n = 3 if transform_type == "alternatives" else 1
    return call_openai(input_text, transform_type, n=n)