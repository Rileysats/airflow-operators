from setuptools import setup, find_packages

setup(
    name='my-airflow-operators',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Custom Airflow operators and hooks',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'apache-airflow>=2.0.0',
        # Add other dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Apache Airflow',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)