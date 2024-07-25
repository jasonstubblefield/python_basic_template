### Basic Python Template

I created this as a better starting point for Python scripting. 

* testing
* readme
* gitignore
* license
* requirements

**Please modify or remove the license file if you don't intend to use this for open source code. This code is released under the MIT license.**

Create a virtual environment.

`python3 -m venv venv`

Initialize the virtual environment.

`source venv/bin/activate`

Install the requirements.

`python3 -m pip install -r requirements.txt`

Run the unit tests.

`pytest ./custom_math.py`

Run the feature tests.

`pytest ./main.py`