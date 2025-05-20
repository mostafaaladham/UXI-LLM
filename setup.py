from setuptools import setup, find_packages

setup(
    name="uxi-llm",
    version="0.1.0",
    description="A modular, symbolic-ready LLM framework addressing developer pain points",
    author="BryceWDesign",
    author_email="contact@example.com",
    url="https://github.com/BryceWDesign/UXI-LLM",
    packages=find_packages(),
    install_requires=[
        "torch>=1.12.0",
        "transformers>=4.20.0",
        "numpy",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "uxi-train=scripts.train:main",
            "uxi-eval=scripts.evaluate:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
