import pytest
from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from main import app, VERSION

client = TestClient(app)

NO_SOLUTION_RESPONSE = {"detail": "Problem hasn't solution for X=4, Y=3, Z=5"}
ZERO_SOLUTION_RESPONSE = "[]"
SOLUTION_RESPONSE_4_3_2 = [
    {
        "state": {"jug1_amount": 0, "jug2_amount": 3},
        "action": {"action_label": "Fill", "jug_from": 2, "moved_cant": 3},
    },
    {
        "state": {"jug1_amount": 3, "jug2_amount": 0},
        "action": {"action_label": "Transfer", "jug_from": 2, "moved_cant": 3},
    },
    {
        "state": {"jug1_amount": 3, "jug2_amount": 3},
        "action": {"action_label": "Fill", "jug_from": 2, "moved_cant": 3},
    },
    {
        "state": {"jug1_amount": 4, "jug2_amount": 2},
        "action": {"action_label": "Transfer", "jug_from": 2, "moved_cant": 1},
    },
]


def test_version():
    """checks api version."""
    response = client.get("/version")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == VERSION


def test_check_no_solution():
    """checks solver with no solution possible"""
    response = client.get(
        "/water_jug_solver",
        params={"jug1_capacity": 4, "jug2_capacity": 3, "target": 5},
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == NO_SOLUTION_RESPONSE


@pytest.mark.parametrize(
    "jug1_capacity,jug2_capacity,target", [(-1, 8, 2), (4, -7, 2), (4, 3, -2)]
)
def test_check_negative_values(
    jug1_capacity: int, jug2_capacity: int, target: int
):
    """checks solver with negative values."""
    response = client.get(
        "/water_jug_solver",
        params={
            "jug1_capacity": jug1_capacity,
            "jug2_capacity": jug2_capacity,
            "target": target,
        },
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_check_zero_target():
    """checks solver requesting 0 Gallons to target."""
    response = client.get(
        "/water_jug_solver",
        params={
            "jug1_capacity": 8,
            "jug2_capacity": 9,
            "target": 0,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


def test_check_solution():
    """checks solver with a complex case."""
    response = client.get(
        "/water_jug_solver",
        params={
            "jug1_capacity": 4,
            "jug2_capacity": 3,
            "target": 2,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 4
    assert response.json() == SOLUTION_RESPONSE_4_3_2
