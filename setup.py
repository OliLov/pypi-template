"""Setup for your_project_name."""
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

DESC = "Brief description of your project in one or two sentences."

setup(
    name="project-name",
    version="0.0.1",
    description=DESC,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/your-project-name",
    author="your-name",
    author_email="your-email@example.com",
    classifiers=[  # Add classifiers. See https://pypi.org/classifiers/.
        "Development Status :: 1 - Planning",
        "Intended Audience :: Other Audience",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)
