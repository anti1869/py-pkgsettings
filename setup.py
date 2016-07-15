
from setuptools import setup
setup(**{'author': 'Niels Lensink',
 'author_email': 'niels.lenssink@kpn.com',
 'classifiers': ['Development Status :: 5 - Production/Stable',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.5',
                 'Topic :: Internet :: WWW/HTTP'],
 'description': 'Python package to ease the configuration of packages',
 'include_package_data': True,
 'install_requires': ['pkgversion'],
 'long_description': "pkgsettings\n===========\n\n.. image:: https://secure.travis-ci.org/kpn-digital/py-pkgsettings.svg?branch=master\n    :target:  http://travis-ci.org/kpn-digital/py-pkgsettings?branch=master\n\n.. image:: https://img.shields.io/codecov/c/github/kpn-digital/py-pkgsettings/master.svg\n    :target: http://codecov.io/github/kpn-digital/py-pkgsettings?branch=master\n\n.. image:: https://img.shields.io/pypi/v/pkgsettings.svg\n    :target: https://pypi.python.org/pypi/pkgsettings\n\n.. image:: https://readthedocs.org/projects/py-pkgsettings/badge/?version=latest\n    :target: http://py-pkgsettings.readthedocs.org/en/latest/?badge=latest\n\n\nGoal\n----\n\nThe goal of this package is to offer an easy, generic and extendable way\nof configuring a package.\n\nInstallation\n------------\n.. start_installation\n\n.. code-block:: bash\n\n    $ pip install pkgsettings\n\n.. end_installation\n\nUsage\n-----\n.. start_usage\n.. code-block:: python\n\n    from pkgsettings import Settings\n\n    # Create the settings object for your package to use\n    settings = Settings()\n\n    # Now lets defined the default settings\n    settings.configure(hello='World', debug=False)\n\nBy calling the configure you actually inject a ``layer`` of settings.\nWhen requesting a setting it will go through all layers until it finds the\nrequested key.\n\nNow if someone starts using your package it can easily modify the active\nsettings of your package by calling the configure again.\n\n.. code-block:: python\n\n    from my_awesome_package.conf import settings\n\n    # Lets change the configuration here\n    settings.configure(debug=True)\n\n\nNow from within your package you can work with the settings like so:\n\n.. code-block:: python\n\n    from conf import settings\n\n    print(settings.debug) # This will print: True\n    print(settings.hello) # This will print: World\n\nIt is also possible to pass an object instead of kwargs.\nThe settings object will call ``getattr(ur_object, key)``\nAn example below:\n\n.. code-block:: python\n\n    class MySettings(object):\n        def __init__(self):\n            self.debug = True\n\n    settings = Settings()\n    settings.configure(MySettings())\n    print(settings.debug) # This will print: True\n\nMore advanced usage\n-------------------\n\nThe settings object can also be used as context manager:\n\n.. code-block:: python\n\n    with settings(debug=True):\n        print(settings.debug) # This will print: True\n\n    print(settings.debug) # This will print: False\n\nAdditionally you can also use this as a decorator:\n\n.. code-block:: python\n\n    @settings(debug=True)\n    def go()\n        print(settings.debug) # This will print: True\n\n    go()\n\n    print(settings.debug) # This will print: False\n\n\n.. end_usage\n",
 'name': 'pkgsettings',
 'packages': ['pkgsettings', 'tests'],
 'tests_require': ['tox'],
 'url': 'https://github.com/kpn-digital/py-pkgsettings.git',
 'version': '0.10.0',
 'zip_safe': False})
