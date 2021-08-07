import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NT.py",
    version="4.1.1",
    author="adl212",
    author_email="emailforpythoncoding@gmail.com",
    description="A package to use the nitrotype api and get player or team stats",
    long_description=long_description, # don't touch this, this is your README.md
    long_description_content_type="text/markdown",
    url="https://github.com/adl212/NT.py",
    packages=['nitrotype'],
    data_files=['nitrotype/scrapers.json'],
    include_package_data = True,
    install_requires=['cloudscraper', 'jsonpickle'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)