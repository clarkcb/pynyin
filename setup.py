from setuptools import setup
from pynyin import __version__

setup(name='pynyin',
      version=__version__,
      description='A basic pinyin parser',
      url='https://github.com/clarkcb/pynyin.git',
      author='Cary Clark',
      author_email='clarkcb@gmail.com',
      install_requires=[],
      license='MIT',
      packages=['pynyin'],
      python_requires='>=3',
      scripts=[
          'bin/pynyin'
      ],
      tests_require=[
          'nose',
      ])
