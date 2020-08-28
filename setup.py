# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eggbot']

package_data = \
{'': ['*']}

install_requires = \
['discord>=1.0.1,<2.0.0', 'owotext>=1.0.3,<2.0.0']

setup_kwargs = {
    'name': 'eggbot',
    'version': '2.3.1',
    'description': '',
    'long_description': None,
    'author': 'repl.it user',
    'author_email': 'replituser@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
