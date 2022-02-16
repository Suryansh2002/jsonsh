import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	# Here is the module name.
	name="jsonsh",

	version="0.0.3",

	author="Suryansh Sharma",

	author_email="suryanshforfree@gmail.com",

	long_description=long_description,
	long_description_content_type="text/markdown",

	url="https://github.com/Suryansh2002/jsonsh",
	packages=setuptools.find_packages(),


	install_requires=[
        "orjson",
        "ujson",
        "pydantic"
    ],


	license="MIT",

	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
