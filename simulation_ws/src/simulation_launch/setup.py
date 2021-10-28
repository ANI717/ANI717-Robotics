from setuptools import setup, find_packages
from glob import glob

PACKAGE_NAME = 'simulation_launch'

setup(
    name=PACKAGE_NAME,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + PACKAGE_NAME]),
        ('share/' + PACKAGE_NAME, ['package.xml']),
        ('share/' + PACKAGE_NAME + '/launch', glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ANI717',
    maintainer_email='animesh.ani@live.com',
    description='ROS2 Package to run a Robot Car in Gazebo Simulation',
    license='MIT License',
    tests_require=['pytest'],
)
