from setuptools import setup

setup(
    name="fabric3-stubs",
    version="0.0.2",
    packages=["fabric-stubs"],
    package_data={
        "fabric-stubs": ["*.pyi"],
    },
    install_requires=[
        "fabric3==1.14.post1",
    ],
)

