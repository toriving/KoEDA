from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="koeda",
    version="0.0.4",
    description="Korean Easy Data Augmentation Package",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Dongju.Park",
    author_email="toriving@gmail.com",
    url="https://github.com/toriving/KoEDA",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=requirements,
    keywords=["NLP deep learning koeda korean easy data augmentation"],
    license="MIT",
    python_requires=">=3.7.0",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
