# setup.py
from setuptools import setup, find_packages

setup(
    name="pyspark-hello-world",
    version="0.0.1",
    author="Subhankar Das",
    author_email="imsubha27@gmail.com",
    description="A simple Pyspark application",
    packages=find_packages(),   #Automatically detects the python packages under src/.
    package_dir={"": "src"},
    install_requires=[     #Lists dependencies for the package
        'pyspark==3.5.4',  # Specify the minimum version of PySpark
    ],
    entry_points={         #Create a CLI command for the app
        'console_scripts': [
            'hello-world = hello-world:main',
        ],
    },
    python_requires=">=3.6",
)
