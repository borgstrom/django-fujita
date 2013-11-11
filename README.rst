Django-Fujita
=============

This is a Tornado server built to run the Django_ builtin 'runserver' command.

This uses WebSockets, so modern browsers only.

Why on earth would one want to do such a crazy thing?
-----------------------------------------------------
The main reason this was built was for the use case of a team environment where
the developers are using Vagrant_ for local development and want to give the
less terminal savvy users an easy way to run and control the Django_ development
server.

How do I use this?
------------------
For testing purposes:

#. Clone this repository.
#. Create a new virtualenv
#. Install ``Django`` & ``tornado`` via pip
#. Run the fujita.py script with the command to run the testproject (see below)
#. Visit the Fujita Console in your browser

To distribute a Fujita Console in your project simply list ``django-fujita`` in
your requirements and then add a ``fujita.py`` script to the root.

Running the fujita.py script
----------------------------
You need to tell the script how to run your development server through the
``--command`` option.

If you're following the steps above then you'll want to use something similar
to the following command::

  ./scripts/fujita.py --command "/home/user/.virtualenvs/fujita/bin/python /home/user/projects/django-fujita/testproject/manage.py runserver 0:8000"

The above command assumes you have a virtualenv named ``fujita`` in the
``.virtualenvs`` directory in your home. It also assumes that you have a
projects directory in your home and the ``django-fujita`` repository has been
checked out there. Adjust for your setup.

The ``command`` is run under ``/bin/sh`` so you can set environment variables
by prefixing them in front of the command::

  ./scripts/fujita.py --command "DJANGO_SETTINGS_MODULE=project.settings.dev django-admin.py runserver 0:8000"


.. _Django: http://djangoproject.com/
.. _Vagrant: http://vagrantup.com/
