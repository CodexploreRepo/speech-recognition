"""The setup file for the project
"""
from os import path

from setuptools import find_packages, setup

from src.__version__ import __DESCRIPTION__, __PACKAGE_NAME__, __VERSION__


def get_long_desc():
    README = ""
    try:
        with open("README.md", encoding="utf-8") as readme_file:
            README = readme_file.read()
    except:
        README = "N/A"
    return README


def open_file(filepath, mode="r"):
    here = path.abspath(path.dirname(__file__))
    full_path = path.join(here, filepath)
    return open(full_path, mode)


def find_requires():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        install_requires = []
        for line in f:
            req = line.split("#", 1)[0].strip()
            if req and not req.startswith("--"):
                install_requires.append(req)
    return install_requires


setup_args = dict(
    name=__PACKAGE_NAME__,
    version=__VERSION__,
    description=__DESCRIPTION__,
    long_description_content_type="text/markdown",
    author="Nguyen Ha Quan",
    author_email="quan.ngha95@gmail.com",
    long_description=get_long_desc(),
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 1 - RC",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Linux :: Redhat",
        "Programming Language :: Python",
        "Topic :: Analytics",
        "Topic :: Office/Business",
        "Topic :: Software Development :: Data Science",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)

if __name__ == "__main__":
    setup(**setup_args, install_requires=find_requires())
