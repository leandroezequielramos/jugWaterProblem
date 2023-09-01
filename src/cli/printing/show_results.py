"""functions to show water jug problem results"""
from typing import List, Optional

from water_jug_problem.schemas import Action, ActionLabel, State, Step


def _step_to_str(step: Step) -> str:
    """
    converts a step in a str

    Parameters
    ----------
    step : Step
        step to convert

    Returns
    -------
    str
        step string representation
    """
    to_jug = 1 if step.action.jug_from == 2 else 2
    action_str = (
        f"{step.action.action_label} {step.action.moved_cant} "
        f"Gallons from Jug {step.action.jug_from} to Jug {to_jug}."
        if step.action.action_label == ActionLabel.TRANSFER
        else f"{step.action.action_label} Jug {step.action.jug_from}."
    )
    state_str = (
        f"State = (jug1 = {step.state.jug1_amount} "
        f"Gallons, jug2 = {step.state.jug2_amount} Gallons)"
    )
    return f"{action_str} {state_str}"


def print_results(
    jug1_capacity: int,
    jug2_capacity: int,
    target: int,
    steps: Optional[List[Step]],
):
    """
    prints solution in command line

    Parameters
    ----------
    jug1_capacity : int
        jug 1 capacity
    jug2_capacity : int
        jug2 capacity
    target : int
        target
    steps : Optional[List[Step]]
        steps to reach solution or None if hasn't solution
    """
    print(f"Jug 1 capacity: {jug1_capacity} Gallons")
    print(f"Jug 2 capacity: {jug2_capacity} Gallons")
    print(f"Desidered target: {target} Gallons")
    if steps:
        print(f"Best solution requires: {len(steps)} movements")
        for i, step in enumerate(steps):
            print(f"{i+1}) {_step_to_str(step=step)}")
    else:
        print("No Solution!")
