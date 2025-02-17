import setuptools

with open("README.md", mode="r") as fd:
    long_description = fd.read()

setuptools.setup(
    name="discord-logger",
    version="1.2.4",
    author="Chaitanya Chinni",
    description="Discord Logger is a custom message logger to Discord for Python 3",
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chinnichaitanya/python-discord-logger",
    packages=setuptools.find_packages(),
    install_requires=["discord-webhook == 0.13.0", "pyyaml >= 6.0.1"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.5",
    keywords=[
        "monitoring",
        "discord",
        "messaging",
        "logging",
        "health-check",
        "notification-service",
        "notification",
        "discord-webhook",
    ],
)
