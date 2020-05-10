import setuptools

with open("README.md", mode="r") as fd:
    long_description = fd.read()

setuptools.setup(
    name="discord-logger",
    version="1.0.4",
    author="Chaitanya Chinni",
    description="Disccord Logger is a custom message logger to Discord for Python 3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chinnichaitanya/python-discord-logger",
    packages=setuptools.find_packages(),
    install_requires=["discord-webhook"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
)
