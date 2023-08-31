import sys
from water_jug_problem import water_jug_solver


def print_results(steps, target):
    if steps:
        print(f"Steps to measure {target} gallons:")
        print(f"Solution in {len(steps)} steps")
        for i, step in enumerate(steps):
            print(f"{i+1}){step}")
    else:
        print("No Solution")


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
    print_results(
        steps=water_jug_solver(
            jug_capacity_1=jug_capacity_1,
            jug_capacity_2=jug_capacity_2,
            target=target,
        ),
        target=target,
    )


if __name__ == "__main__":
    main()
