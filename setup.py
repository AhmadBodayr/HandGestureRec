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
    version='0.1.6',
    description='Dynamic hand gesture detection library using ML.',
    packages=find_packages(),
    py_modules=[
        "main",
        "MLScript",
        "mainView",
        "modelTestingView",
        "myDataSetsView",
        "myGesturesView",
        "myModelsView",
    ],
    entry_points={
        'console_scripts': [
            'execHandGestureRec = main:run',
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
