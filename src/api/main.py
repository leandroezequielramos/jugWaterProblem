"""Application main module."""
from typing import List
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import conint
from water_jug_problem.schemas import Step
from water_jug_problem import water_jug_solver

VERSION = "0.1.0"

app = FastAPI(
    title="Water Jug Riddle API",
    description="Water Jug problem solver API",
    version=VERSION,
    root_path="/",
    debug=False,
)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(path="/version")
async def version() -> str:
    return VERSION


@app.get(path="/water_jug_solver")
async def water_jug_riddle(
    jug1_capacity: int = Query(ge=1),
    jug2_capacity: int = Query(ge=1),
    target: int = Query(ge=0),
) -> List[Step]:
    return water_jug_solver(
        jug_capacity_1=jug1_capacity,
        jug_capacity_2=jug2_capacity,
        target=target,
    )
