from setuptools import setup, find_packages

version = '1.0a1'

setup(name='mr.steele',
      version=version,
      description="Plone Core-specific release management tools",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Eric Steele',
      author_email='esteele@plone.org',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['mr'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'argh'
      ],
      entry_points="""
      [console_scripts]
      manage = mr.steele:main
      """,
      )
