
====================
Leonardo Blog Module
====================

FeinCMS ElephantBlog integration

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo_module_blog

or as leonardo bundle

.. code-block:: bash

    pip install django-leonardo["blog"]

Add ``leonardo_module_sentry`` to APPS list, in the ``local_settings.py``::

    APPS = [
    	...
        'blog'
        ...
    ]

    of 

    INSTALLED_APPS = ['leonardo_module_blog']
        

Load new template to db

.. code-block:: bash

	python manage.py sync_all
