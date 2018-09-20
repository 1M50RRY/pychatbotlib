import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pychatbotlib",
    version="1.0.1",
    author="ims0rry",
    author_email="dmr0@protonmail.com",
    description="Library for creating chatbots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/1M50RRY/pychatbotlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
