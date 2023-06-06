import setuptools
with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pycr",#python code return
    version="0.0.1",
    author="Kuan-Lin Chen",
    author_email="ken54787845@gmail.com",
    description="A small test project through which program messages can be sent back and forth to the line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tzamou/pycr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
