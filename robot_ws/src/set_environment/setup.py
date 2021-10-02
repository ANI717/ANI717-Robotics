from setuptools import setup, find_packages

PACKAGE_NAME = 'set_environment'
REQUIRES_PYTHON = '>=3.6.0'

setup(
    name=PACKAGE_NAME,
    version='1.0.0',
    zip_safe=True,
    packages=find_packages(),
    python_requires=REQUIRES_PYTHON,
    install_requires=[
        'setuptools',
        'opencv-python',
        'torch',
        'torchvision',
        'inputs'
    ]
)