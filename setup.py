import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-validators",
    version="1.0.1",
    author="Devang Padhiyar",
    author_email="devangpadhiyar700@gmail.com",
    description="Django validators used for commonly used validations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devangpadhiyar/django-validators",
    packages=setuptools.find_packages(),
    install_requires=[
        'Django>=1.8',
        'python-magic>=0.4.15'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)