import setuptools

requirements = [
    "pandas",
    "requests",
]

setuptools.setup(
    name="Geocoding-utils",
    version="0.0.1",
    author="Charles Herriau",
    description="Python library utils for Geocoding library",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/chrlryo/Geocoding-utils",
    packages=setuptools.find_packages(include=['Geocoding_utils', 'Geocoding_utils.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    install_requires=requirements,
)
