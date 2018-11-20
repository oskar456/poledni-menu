Polední menu
============

This utility will scrap daily menues from nearby restaurants and
send them via e-mail. It is based on very simple modular architecture where
each extractor presents similar API.

Instalation
-----------

Use Python 3.6 virtual environment to install all necessary dependencies:

.. code-block:: shell

    $ python3 -m venv venv
    $ source venv/bin/activate
    (venv) $ pip install -U pip
    (venv) $ pip install git+https://github.com/oskar456/poledni-menu

After installation, you'll get three new runables:

`poledni-menu-print <extractor>`
  Call given extractor and print its output to the standard output.

`poledni-menu-digest <config file>`
  Read a list of extractors and their parameters from a YAML config file.
  Print daily menu digest to the standard output.

`poledni-menu-email <config file>`
  Read a list of extractors and their parameters from a YAML config file.
  Send an e-mail with the digest to e-mail addresses configured in the
  config file.

Configuration file example
--------------------------

.. code-block:: yaml

    ---
    menu:
     - potrefena_husa
     - kulatak
     - budvarka
     - blox
     - extractor: agata
       place_id: 3
     - extractor: agata
       place_id: 5
     - bernard_pub

    email:
      server: localhost
      sender: Foodmaster <foodmaster@example.com>
      recipients:
              - Root <root@localhost>
              - postmaster@example.com
    ...
