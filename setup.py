from setuptools import find_packages
from setuptools import setup

setup(name='kimsufi-checker',
      version='0.1.0',
      description='Checks for kimsufi availability',
      author='Tom Creasey',
      author_email='NA',
      keywords='server',
      license='Apache 2.0',
      python_requires='~=3.6',
      package_dir={'': 'src'},
      packages=find_packages(where='src'),
      zip_safe=False,
      install_requires=['requests~=2.19.1'],
      entry_points={'console_scripts': ['kimsufi-checker = kimsufi_checker.kimi:main']},
      classifiers=[
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ]
      )
