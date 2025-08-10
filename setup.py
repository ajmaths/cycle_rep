from setuptools import setup, find_packages

setup(
    name="cycle_reps_package",
    version="0.1.0",
    author="Wenwen Li",
    description="Weighted bipartite graph package with spanning tree and cycle analysis",
    packages=find_packages(),
    install_requires=[
        "networkx",
        "matplotlib",
    ],
    python_requires='>=3.7',
)
