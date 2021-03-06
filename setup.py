import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="payrun", # Replace with your own username
    version="0.0.1",
    author="Andrii Pushkar",
    author_email="zingeon1@gmail.com",
    description="A Python SDK for PayRun API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zingeon/payrun-python",
    download_url = "https://codeload.github.com/Zingeon/payrun-python/tar.gz/0.0.2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)