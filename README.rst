========
DataFake
========


.. image:: https://img.shields.io/pypi/v/datafake.svg
        :target: https://pypi.python.org/pypi/datafake

.. image:: https://img.shields.io/travis/davin2014/datafake.svg
        :target: https://travis-ci.com/davin2014/datafake

.. image:: https://readthedocs.org/projects/datafake/badge/?version=latest
        :target: https://datafake.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Python Boilerplate contains all the boilerplate you need to create a Python package.


* Free software: MIT license
* Documentation: https://datafake.readthedocs.io.


Features
--------

datafake
========

This is a script to generate fake user data and send it to a signup API.

Here is the Python code:

.. code-block:: python

    import requests
    import json
    from faker import Faker

    fake = Faker()

    def generate_fake_user():
        return {
            "email": fake.email(),
            "fullname": fake.name(),
            "password": fake.password()
        }

    def send_user_to_api(user):
        response = requests.post("http://localhost:5050/signup", data=json.dumps(user), headers={'Content-Type': 'application/json'})
        return response.status_code

    if __name__ == "__main__":
        print("Done")
        for _ in range(50):
            user = generate_fake_user()
            status_code = send_user_to_api(user)
            print(f"User {user['email']} registered with status code {status_code}")

To run the script, simply execute the Python file in your terminal.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
