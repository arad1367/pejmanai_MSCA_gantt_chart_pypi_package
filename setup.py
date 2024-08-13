from setuptools import setup, find_packages

setup(
    name='pejmanai_msca',
    version='0.0.3',
    description='A Python package that creates a high-quality Gantt chart to visualize project timelines, work packages, milestones, and deliverables',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Pejman',
    author_email='pejman.ebrahimi77@gmail.com',
    url='https://github.com/arad1367/pejmanai_MSCA_gantt_chart_pypi_package',
    packages=find_packages(),
    install_requires=[
        'plotly',
        'kaleido',
        'numpy'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.8',
    project_urls={
        'Source': 'https://github.com/arad1367/pejmanai_MSCA_gantt_chart_pypi_package',
        'Buy me a coffee': 'https://ko-fi.com/arad1367',
    },
)
