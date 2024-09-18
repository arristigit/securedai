from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name="securedai",
    version="0.1.1",
    description="Secure your ML models using securedai",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/arristigit/securedai",
    author="Varinder Kumar",
    packages=find_packages(),
    install_requires=["python-decouple==3.8"]
)