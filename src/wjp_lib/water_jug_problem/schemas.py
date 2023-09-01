"""Defines schemas."""
from enum import Enum
from typing import Union

from pydantic import BaseModel


class ActionLabel(str, Enum):
    """represents an action label"""

    FILL = "Fill"
    EMPTY = "Empty"
    TRANSFER = "Transfer"


class State(BaseModel):
    """represents a possible state."""

    jug1_amount: int
    jug2_amount: int


class Action(BaseModel):
    """represents an executed action"""

    action_label: ActionLabel
    jug_from: int
    moved_cant: int


class Step(BaseModel):
    """
    represents a water jug problem step to reach solution
    """

    state: State
    action: Action
