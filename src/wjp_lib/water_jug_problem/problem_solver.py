from typing import List, Optional
from water_jug_problem.math import gcd
from water_jug_problem.schemas import Step, ActionLabel, Action, State
from water_jug_problem.constants import (
    EMPTY_JUG_CANT,
    JUG1_POS,
    JUG2_POS,
    JUGS_NUM,
)


def _water_jug_problem_has_solution(
    jug_capacity_1: int, jug_capacity_2: int, target: int
) -> bool:
    """
    checks if water jug problem has solution for a defined input

    Parameters
    ----------
    jug_capacity_1 : int
        jug 1 capacity
    jug_capacity_2 : int
        jug 2 capacity
    target : int
        desidered target

    Returns
    -------
    bool
        True if problem has solution, False otherwise
    """
    assert jug_capacity_1 >= 0 and jug_capacity_2 >= 0 and target >= 0
    jugs_gcd = gcd(jug_capacity_1, jug_capacity_2)
    return (
        target <= max(jug_capacity_1, jug_capacity_2)
        and target % jugs_gcd == 0
    )


def water_jug_solver_from(
    jug_capacity_1: int, jug_capacity_2: int, target: int, start_jug: int
) -> List[Step]:
    """
    Solves water jug problem assuming to start filling jug 'start_jug'

    Parameters
    ----------
    jug_capacity_1 : int
        jug 1 capacity
    jug_capacity_2 : int
        jug 2 capacity
    target : int
        desidered target
    start_jug : int
        jug to start with

    Returns
    -------
    List[Step]
        List of required stepts to reach solution
    """
    steps = []
    jugs = [EMPTY_JUG_CANT, EMPTY_JUG_CANT]
    capacities = [jug_capacity_1, jug_capacity_2]
    steps = []
    other_jug = (start_jug + 1) % JUGS_NUM

    while jugs[JUG1_POS] != target and jugs[JUG2_POS] != target:
        if jugs[start_jug] == EMPTY_JUG_CANT:
            jugs[start_jug] = capacities[start_jug]
            steps.append(
                Step(
                    action=Action(
                        action_label=ActionLabel.FILL,
                        jug_from=(start_jug + 1),
                        moved_cant=capacities[start_jug],
                    ),
                    state=State(
                        jug1_amount=jugs[JUG1_POS], jug2_amount=jugs[JUG2_POS]
                    ),
                )
            )
        elif jugs[other_jug] == capacities[other_jug]:
            jugs[other_jug] = EMPTY_JUG_CANT
            steps.append(
                Step(
                    action=Action(
                        action_label=ActionLabel.EMPTY,
                        jug_from=(other_jug + 1),
                        moved_cant=capacities[other_jug],
                    ),
                    state=State(
                        jug1_amount=jugs[JUG1_POS], jug2_amount=jugs[JUG2_POS]
                    ),
                )
            )
        else:
            transfer = min(
                jugs[start_jug], capacities[other_jug] - jugs[other_jug]
            )
            jugs[start_jug] -= transfer
            jugs[other_jug] += transfer
            steps.append(
                Step(
                    action=Action(
                        action_label=ActionLabel.TRANSFER,
                        jug_from=(start_jug + 1),
                        moved_cant=transfer,
                    ),
                    state=State(
                        jug1_amount=jugs[JUG1_POS], jug2_amount=jugs[JUG2_POS]
                    ),
                )
            )
    return steps


def water_jug_solver(
    jug_capacity_1: int, jug_capacity_2: int, target: int
) -> Optional[List[Step]]:
    """
    Solves water jug problem for a jug 1 capacity, jug 2 capacity and desidered
    target 'target'. Returns None if problem hasn't solution

    Parameters
    ----------
    jug_capacity_1 : int
        jug 1 capacity
    jug_capacity_2 : int
        jug 2 capacity
    target : int
        desidered target

    Returns
    -------
    Optional[List[Step]]
        None if problem hasn't solution otherwise returns the list of steps
        to reach the solution

    Raises
    ------
    ValueError
        When input are lower than zero
    """
    steps = None
    if jug_capacity_1 < 0 or jug_capacity_2 < 0 or target < 0:
        raise ValueError("Jugs capacities and target must be positive values")

    if target == 0:
        steps = []
    elif _water_jug_problem_has_solution(
        jug_capacity_1=jug_capacity_1,
        jug_capacity_2=jug_capacity_2,
        target=target,
    ):
        steps_start_1 = water_jug_solver_from(
            jug_capacity_1=jug_capacity_1,
            jug_capacity_2=jug_capacity_2,
            target=target,
            start_jug=0,
        )
        steps_start_2 = water_jug_solver_from(
            jug_capacity_1=jug_capacity_1,
            jug_capacity_2=jug_capacity_2,
            target=target,
            start_jug=1,
        )
        steps = (
            steps_start_1
            if len(steps_start_1) < len(steps_start_2)
            else steps_start_2
        )
    return steps
