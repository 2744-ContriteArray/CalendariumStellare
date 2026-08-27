from setuptools import find_packages, setup

setup(
    name='stardate',
    packages=find_packages(include=['stardate']),
    version='0.0.1',
    description='A means for implementing a stardate calendar based on the pulsar J1850-0026.',
    author='2744-ContriteArray',
    install_requires=['datetime', 'math'],
)