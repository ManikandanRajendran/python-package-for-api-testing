from setuptools import setup, find_packages

classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 3',
    'Licence :: OSI Approved :: MIT Licence',
    'Intended Audience :: Education'
]

setup(
    name="api-testing-commons",
    version="0.0.1",
    description="",
    long_description=open("README.md").read() + '\n\n' + open('CHANGELOG.txt').read(),
    url="",
    author="Manikandan Rajendran",
    author_email="r.manikandan.king@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords=["api automation", "api testing", "api commons", "python api"],
    packages=find_packages(),
    install_requires=[
        "jsonschema==4.4.0",
        "requests==2.27.1"
        ]
)