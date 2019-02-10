
import setuptools

version = '0.0.1'

setuptools.setup(
    name='mysql_tracer',
    version=version,
    author='Adrien Horgnies',
    author_email='adrien.pierre.horgnies@gmail.com',
    description='A MySQL client to run queries, write execution reports and export results',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AdrienHorgnies/py-mysql-tracer',
    download_url='https://github.com/AdrienHorgnies/py-mysql-tracer/archive/{version}.tar.gz'.format(version=version),
    packages=setuptools.find_packages(),
    install_requires=['mysql-connector-python', 'pyyaml', 'alone', 'keyring'],
    license='MIT License',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers'
    ],
    keywords=['mysql', 'client', 'report', 'export']
)