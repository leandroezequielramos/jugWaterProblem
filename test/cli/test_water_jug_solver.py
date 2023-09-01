"""test for water jug solver."""
import pytest
from water_jug_problem import water_jug_solver

EXPECTED_4_3_2_SOLUTION = [
    '{"state":{"jug1_amount":0,"jug2_amount":3},"action":'
    '{"action_label":"Fill","jug_from":2,"moved_cant":3}}',
    '{"state":{"jug1_amount":3,"jug2_amount":0},"action":'
    '{"action_label":"Transfer","jug_from":2,"moved_cant":3}}',
    '{"state":{"jug1_amount":3,"jug2_amount":3},"action":'
    '{"action_label":"Fill","jug_from":2,"moved_cant":3}}',
    '{"state":{"jug1_amount":4,"jug2_amount":2},"action":'
    '{"action_label":"Transfer","jug_from":2,"moved_cant":1}}',
]


@pytest.mark.parametrize(
    "jug1_capacity,jug2_capacity,target", [(-1, 8, 2), (4, -7, 2), (4, 3, -2)]
)
def test_negative_values(jug1_capacity: int, jug2_capacity: int, target: int):
    """test raise an exception when values are negative"""
    with pytest.raises(ValueError):
        water_jug_solver(
            jug_capacity_1=jug1_capacity,
            jug_capacity_2=jug2_capacity,
            target=target,
        )


def test_zero_target():
    """
    checks case zero target value
    """
    solution = water_jug_solver(
        jug_capacity_1=4,
        jug_capacity_2=3,
        target=0,
    )
    assert solution is not None and len(solution) == 0


@pytest.mark.parametrize(
    "jug1_capacity,jug2_capacity,target", [(6, 8, 5), (1, 2, 3), (4, 8, 10)]
)
def test_check_no_solution(
    jug1_capacity: int, jug2_capacity: int, target: int
):
    """
    checks differents scenarios without solution
    """
    solution = water_jug_solver(
        jug_capacity_1=jug1_capacity,
        jug_capacity_2=jug2_capacity,
        target=target,
    )
    assert solution is None


def test_check_solution():
    """
    checks a case with solution
    """
    solution = water_jug_solver(
        jug_capacity_1=4,
        jug_capacity_2=3,
        target=2,
    )

    assert (
        solution is not None
        and len(solution) == 4
        and [s.model_dump_json() for s in solution] == EXPECTED_4_3_2_SOLUTION
    )


def test_same_result():
    """
    checks if you invert jug order number of steps must be the same
    """
    solution = water_jug_solver(
        jug_capacity_1=4,
        jug_capacity_2=3,
        target=2,
    )
    solution2 = water_jug_solver(
        jug_capacity_1=3,
        jug_capacity_2=4,
        target=2,
    )
    assert (
        solution is not None
        and solution2 is not None
        and len(solution) == len(solution2)
    )
