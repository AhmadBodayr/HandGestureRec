import platform
from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()
    tfversion = ""
    if platform.system() == "Darwin":
        tfversion = "tensorflow-macos"
    else:
        tfversion = "tensorflow"
        
setup(
    long_description=long_description, 
    long_description_content_type="text/markdown",
    name='HandGestureRec',
    version='0.1.4',
    description='m1 macs version',
    packages=find_packages(),
    py_modules=[
        "main",
        "MLScript_2",
        "mainView",
        "modelTestingView",
        "myDataSetsView",
        "myGesturesView",
        "myModelsView",
    ],
    entry_points={
        'console_scripts': [
            'runHandGestureRec = main:run',
        ],
    },
    install_requires=[
        "scikit-learn",
        'mediapipe',
        'opencv-python',
        tfversion,
        'numpy',
        "pandas",
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    package_dir = {'': 'src'},
  
)  
