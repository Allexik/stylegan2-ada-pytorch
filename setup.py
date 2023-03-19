from setuptools import setup, find_packages

setup(
    name="stylegan2-ada-pytorch",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
        "numpy",
        "pillow",
        "click",
        "tqdm",
        "opensimplex",
        "torch-utils",
        "tensorboard",
    ],
)
