from setuptools import setup

VERSION = '1.0.0'
DESCRIPTION = 'Minientreprise csv - Image validation before uploading'
f = open('README.md')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name="plantDetectionIA",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="camarm",
    author_email="armand@camponovo.xyz",
    license='MIT',
    packages=['plantDetectionIA'],
    install_requires=['opencv-python', 'numpy', 'qrdet'],
    keywords='conversion',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ],
    long_description_content_type='text/markdown'
)
