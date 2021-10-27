from setuptools import setup, find_packages
from glob import glob

PACKAGE_NAME = 'ros2_pytorch_model_to_twist_message'

setup(
    name=PACKAGE_NAME,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + PACKAGE_NAME]),
        ('share/' + PACKAGE_NAME, ['package.xml']),
        ('share/' + PACKAGE_NAME + '/launch', ['launch/launch.py']),
        ('share/' + PACKAGE_NAME + '/torch_model', glob('torch_model/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ANI717',
    maintainer_email='animesh.ani@live.com',
    description='Deep Learning Package to Publish Twist Message for Robot Running',
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'execute = ros2_pytorch_model_to_twist_message.torch_to_twist_function:main',
        ],
    },
)