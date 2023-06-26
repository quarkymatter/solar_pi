from setuptools import setup, find_packages

setup(
    name='solar_pi',
    version='0.1.0',
    author='quarkymatter',
    author_email='w.osborn@utah.edu',
    description='Solar charge controller data via Raspberry Pi.',
    packages=find_packages(),
    install_requires=[
        'prometheus_client==0.1.0',
        'pyserial==3.4',
        'MinimalModbus==0.7',
    ],
)
