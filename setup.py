from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.readlines()

setup(
    name="realtime_kmeans",
    version="0.1",
    description="Real-time KMeans clustering and streaming histogram",
    author="Fedor Shabashev",
    author_email="",
    packages=find_packages(exclude=("tests", "examples")),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="realtime, kmeans, clustering, histogram, streaming",
    python_requires=">=3.6",
)

