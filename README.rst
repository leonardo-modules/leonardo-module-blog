
======================
Leonardo Sentry Module
======================

Provide end-user friendly 500 Error handler for Leonardo Sites

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo_module_sentry

or as leonardo bundle

.. code-block:: bash

    pip install django-leonardo["sentry"]

Add ``leonardo_module_sentry`` to APPS list, in the ``local_settings.py``::

    APPS = [
    	...
        'leonardo_module_sentry'
    	...
    ]

Load new template to db

.. code-block:: bash

	python manage.py sync_common

Add ``RAVEN_CONFIG`` into your ``settings.py``::

    RAVEN_CONFIG = {
        'dsn': 'http://public:secret@example.com/1',
    }
