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


def water_jug_solver_from(jug_capacity_1, jug_capacity_2, target, start_jug):
    steps = []
    jugs = [0, 0]
    capacities = [jug_capacity_1, jug_capacity_2]
    steps = []
    other_jug = (start_jug + 1) % 2

    while jugs[0] != target and jugs[1] != target:
        if jugs[start_jug] == 0:
            jugs[start_jug] = capacities[start_jug]
            steps.append(
                f"Fill jug {start_jug+1} ({capacities[start_jug]} Gallons)"
            )
        elif jugs[other_jug] == capacities[other_jug]:
            jugs[other_jug] = 0
            steps.append(
                f"Empty jug {other_jug+1} ({capacities[other_jug]} "
                f"Gallons)"
            )
        else:
            transfer = min(
                jugs[start_jug], capacities[other_jug] - jugs[other_jug]
            )
            jugs[start_jug] -= transfer
            jugs[other_jug] += transfer
            steps.append(
                f"Pour {transfer} Gallons from jug {start_jug+1} to jug "
                f"{other_jug+1}"
            )
    return steps


def water_jug_solver(jug_capacity_1, jug_capacity_2, target):
    steps = None

    if _water_jug_problem_has_solution(
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
