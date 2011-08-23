from setuptools import setup, find_packages

version = '1.0a1'

setup(name='mr.steele',
      version=version,
      description=""
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zest.releaser',
      ],
      entry_points={
          'zest.releaser.releaser.after': [
              'dosomething = mr.steele:release.releaseTasks',
              ]},
      )
