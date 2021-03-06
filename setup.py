import setuptools
from pkg_resources import get_distribution, DistributionNotFound

with open('README.md') as f:
    long_description = f.read()


def get_dist(pkgname):
    try:
        return get_distribution(pkgname)
    except DistributionNotFound:
        return None


requirements = [
    'pyxdg',
    'i3ipc',
    'pygame'
]
pillow_req = 'pillow-simd' if get_dist('pillow-simd') else 'pillow'
requirements.append(pillow_req)

setuptools.setup(name='i3expo',
                 version='1.1.2',
                 description='Provide a workspace overview for i3wm',
                 long_description=long_description,
                 url='https://github.com/mihalea/i3expo',
                 author='Mircea Mihalea',
                 author_email='mircea@mihalea.ro',
                 license='MIT',
                 zip_safe=False,
                 install_requires=requirements,
                 include_package_data=True,
                 packages=setuptools.find_packages(),
                 entry_points={
                     'console_scripts': [
                         'i3expo-daemon=i3expo.daemon:main',
                         'i3expo=i3expo.client:main'
                     ]
                 })
