from water_jug_problem.math import gcd


def _water_jug_problem_has_solution(
    jug_capacity_1, jug_capacity_2, target
) -> bool:
    """
    _water_jug_problem_has_solution _summary_

    Parameters
    ----------
    jug_capacity_1 : _type_
        _description_
    jug_capacity_2 : _type_
        _description_
    target : _type_
        _description_

    Returns
    -------
    bool
        _description_
    """
    jugs_gcd = gcd(jug_capacity_1, jug_capacity_2)
    # check negatives
    return (
        target <= max(jug_capacity_1, jug_capacity_2)
        and target % jugs_gcd == 0
    )


def water_jug_solver(jug_capacity_1, jug_capacity_2, target):
    steps = None

    if _water_jug_problem_has_solution(
        jug_capacity_1=jug_capacity_1,
        jug_capacity_2=jug_capacity_2,
        target=target,
    ):
        jug1 = 0
        jug2 = 0
        steps = []

        while jug1 != target and jug2 != target:
            if jug1 == 0:
                jug1 = jug_capacity_1
                steps.append(f"Fill jug 1 ({jug_capacity_1} Gallons)")
            elif jug2 == jug_capacity_2:
                jug2 = 0
                steps.append(f"Empty jug 2 ({jug_capacity_2} Gallons)")
            else:
                transfer = min(jug1, jug_capacity_2 - jug2)
                jug1 -= transfer
                jug2 += transfer
                steps.append(f"Pour {transfer} Gallons from jug 1 to jug 2")

    return steps
