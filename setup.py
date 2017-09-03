from distutils.core import setup

setup(
    name='next-episode',
    version='0.1.0',
    author='Egor Berdnikov',
    author_email='me@day-zero.org',
    packages=[],
    scripts=['bin/nextepisode'],
    url='http://day-zero.org',
    license='LICENSE',
    description='Start media player and enqueue a next unseen episode of a series',
    long_description=open('README.md').read(),
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Multimedia :: Video'
        ],
)
