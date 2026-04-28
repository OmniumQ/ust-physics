#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UST-Physics Library Setup"""

from setuptools import setup, find_packages

setup(
    name="ust-physics",
    version="5.0.0",
    author="Niyazi ÖCAL",
    author_email="niyazi.ocal@gmail.com",
    description="Professional physics library: GR, QFT, UST, Quantum Gravity",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/OmniumQ/ust-physics",
    packages=find_packages(exclude=["tests", "examples"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "matplotlib>=3.5.0",
        "pandas>=1.3.0",
        "sympy>=1.9",
    ],
)
