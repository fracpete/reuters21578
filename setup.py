from setuptools import setup


setup(
    name="reuters21578",
    description="Little Python 3 library to generate a MEKA ARFF file from the Reuters 21578 SGML sources.",
    url="https://github.com/fracpete/reuters21578",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Programming Language :: Python :: 3',
    ],
    license='MIT License',
    package_dir={
        '': 'src'
    },
    packages=[
        "reuters",
    ],
    version="0.0.1",
    author='Peter "fracpete" Reutemann',
    author_email='fracpete@gmail.com',
    install_requires=[
        "beautifulsoup4",
        "liac-arff",
    ],
    entry_points={
        "console_scripts": [
            "reuters-generate=reuters.generate:sys_main",
        ]
    }
)
