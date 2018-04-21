from setuptools import setup, find_packages
import morseplay

with open("README.md", "r") as f:
    long_description = f.read()

setup(name='morseplay',
      version=morseplay.__version__,
      description='Python library to send and receive morse codes on Raspberry Pi',
      long_description=long_description,
      author='Ritiek Malhotra',
      author_email='ritiekmalhotra123@gmail.com',
      packages = find_packages(),
      url='https://www.github.com/ritiek/morseplay',
      keywords=['morse', 'raspberry-pi', 'python', 'LED'],
      license='MIT',
      download_url='https://github.com/ritiek/morseplay/archive/v' + morseplay.__version__ + '.tar.gz',
      classifiers=[],
      install_requires=[
            'morse-talk',
      ]
     )
