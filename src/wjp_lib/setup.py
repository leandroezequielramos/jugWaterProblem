from setuptools import find_packages, setup
from water_jug_problem.version import __VERSION__

setup(
    name="water_jug_problem",
    packages=find_packages(include=["water_jug_problem"]),
    version=__VERSION__,
    description="Library to solve water two water jugs problem",
    author="Leandro ramos",
    license="MIT",
    install_requires=[],
    setup_requires=["pydantic==2.3.0"],
    tests_require=["pytest==7.4.0"],
    test_suite="tests",
)
