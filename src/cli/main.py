import sys
from printing import print_results
from water_jug_problem import water_jug_solver


def main():
    """Main function."""
    if len(sys.argv) != 4:
        sys.stderr.write(
            "Wrong number of arguments. "
            "Expected: 'python main.py jug1_cap jug2_cap target'"
            "\n"
        )
        sys.exit(1)
    jug_capacity_1 = int(sys.argv[1])
    jug_capacity_2 = int(sys.argv[2])
    target = int(sys.argv[3])
    try:
        steps = water_jug_solver(
            jug_capacity_1=jug_capacity_1,
            jug_capacity_2=jug_capacity_2,
            target=target,
        )
        print_results(
            jug1_capacity=jug_capacity_1,
            jug2_capacity=jug_capacity_2,
            target=target,
            steps=steps,
        )
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
