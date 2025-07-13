from enum import Enum

class TransformType(str, Enum):
    rephrase = "rephrase"
    concise = "concise"
    formal = "formal"
    informal = "informal"
    quickly = "quickly"
    alternatives = "alternatives"
