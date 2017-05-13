from setuptools import setup, find_packages


setup(
    name='flask-pluggy-guest',
    packages=find_packages('.'),
    entry_points={
        'flaskplug': [
            'flask_pluggy_guest = guest.plugin'
        ]
    }
)
