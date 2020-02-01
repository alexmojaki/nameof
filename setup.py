from setuptools import setup

package = 'nameof'


setup(name=package,
      version='0.0.1',
      description='Get the name of a variable or attribute, as in C#',
      url='https://github.com/alexmojaki/' + package,
      author='Alex Hall',
      author_email='alex.mojaki@gmail.com',
      license='MIT',
      include_package_data=True,
      py_modules=[package],
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      zip_safe=False)
