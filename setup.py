from setuptools import setup, find_packages
setup(
    name='HandGestureRecSiliconM1',
    version='0.1',
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
            'run = main:run',
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
        'Operating System :: OS Independent',
    ],
    package_dir = {'': 'src'},
)  
