from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    long_description=long_description, 
    long_description_content_type="text/markdown",
    name='HandGestureRecSiliconM1',
    version='0.1.3',
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
        'tensorflow-macos',
        'numpy',
        "pandas",
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS :: MacOS X',
    ],
    package_dir = {'': 'src'},
)  
