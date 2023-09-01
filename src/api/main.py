"""Application main module."""
from typing import List

from fastapi import FastAPI, Query, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import conint
from water_jug_problem import water_jug_solver
from water_jug_problem.schemas import Step

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
    """
    retrieves API verson

    Returns
    -------
    str
        API version as string
    """
    return VERSION


@app.get(path="/water_jug_solver")
async def water_jug_riddle(
    jug1_capacity: int = Query(ge=1),
    jug2_capacity: int = Query(ge=1),
    target: int = Query(ge=0),
) -> List[Step]:
    """
    solves water jug  problem for jug1_capacity, jug2_capacity and target

    Parameters
    ----------
    jug1_capacity : int, optional
        jug 1 capacity must be greater than 0, by default Query(ge=1)
    jug2_capacity : int, optional
        jug 2 capacity must be greater than 0, by default Query(ge=1)
    target : int, optional
        desidered target must be greater or equal than 0, by default Query(ge=0)

    Returns
    -------
    List[Step]
        List of steps to reach solution
    Raises
    ------
    HTTPException
        404 ->  When problem hasn't solution for desidered inputs

    """
    steps = water_jug_solver(
        jug_capacity_1=jug1_capacity,
        jug_capacity_2=jug2_capacity,
        target=target,
    )
    if steps is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Problem hasn't solution for "
            f"X={jug1_capacity}, Y={jug2_capacity}, Z={target}",
        )
    return steps
