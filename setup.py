import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nitrotype.py",
    version="0.0.1",
    author="adl212",
    author_email="emailforpythoncoding@gmail.com",
    description="a short description.",
    long_description=long_description, # don't touch this, this is your README.md
    long_description_content_type="text/markdown",
    url="The link to the github/repl/repository",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)