from fastapi import FastAPI

from models.colour import ColourPostSchema, ColourResponseSchema
from solution import equation_solution, mr_randomizer

app = FastAPI()


@app.get("/quad_equation/")
def read_item(a: float, b: float, c: float):
    roots = equation_solution(a=a, b=b, c=c)
    return {f"roots for {a} x^2 + {b}x + {c} = 0 ": roots}


@app.post("/guess/colour", response_model=ColourResponseSchema)
def read_item(colour: ColourPostSchema):
    system_colours = mr_randomizer()
    selected = system_colours[colour.num]
    guessed = selected == colour.guess
    resp = ColourResponseSchema(system_colour=selected, your_colour=colour.guess, guessed=guessed)
    return resp
