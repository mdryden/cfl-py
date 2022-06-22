from setuptools import find_namespace_packages, setup

setup(
    name="CFLPy",
    version="0.0.2+cfl1.38",
    author="Michael Dryden",
    author_email="mjdryden@gmail.com",
    description=("An implementation of the CFL's public API (api.cfl.ca) in Python."),
    license="MIT",
    keywords="CFL API",
    url="https://github.com/mdryden/cfl-py",
    packages=find_namespace_packages(include=["cflpy.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Other/Nonlisted Topic",
        "License :: OSI Approved :: MIT License",
    ],
)
