from setuptools import setup

setup(name='lamp',
      version='0.0.1',
      description='LAMP API and development tools',
      url='https://github.com/BIDMCDigitalPsychiatry/LAMP-python',
      author='BIDMC Digital Psychiatry',
      author_email='ryan@digitalpsych.org',
      license='MIT',
      packages=['lamp'],
      install_requires=[
          'numpy','pandas','datetime','matplotlib', 'lifelines', 'urllib3', 'seaborn', 'six'
      ],
      zip_safe=False)