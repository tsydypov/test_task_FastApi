import enum
from pydantic import BaseModel, Field


class Colours(str, enum.Enum):
    blue = 'blue'
    green = 'green'
    red = 'red'


class ColourPostSchema(BaseModel):
    guess: Colours
    num: int = Field(..., ge=0, le=99, description="select number [0,99]", example=2)


class ColourResponseSchema(BaseModel):
    system_colour: Colours
    your_colour: Colours
    guessed: bool

