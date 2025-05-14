from setuptools import setup

if __name__ == "__main__":
    setup(
        name="dctorch",
        version="0.1.2",
        description="Fast discrete cosine transforms for PyTorch",
        url="https://github.com/GallagherCommaJack/dctorch",
        author="Jack Gallagher",
        author_email="jack@gallabytes.com",
        license="MIT",
        packages=["dctorch"],
        install_requires=[
            "numpy>=1.22.0",
            "scipy>=1.8.0",
            "torch>=1.11.0",
        ],
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
        ],
        python_requires=">=3.8",
    )
