from setuptools import setup

setup(
    name='django2-goflow',
    version='1.0',
    description='Fork from Eric Simorre\'s django-goflow, and update it with python 3.6 and fit for django2.0',
    author='Mike Li',
    author_email='mikewolfli@163.com',
    url='***',
    packages=['goflow2', 'goflow2.apptools', 'goflow2.runtime', 'goflow2.graphics', 'goflow2.graphics2', 'goflow2.workflow', 'goflow2.apptools.templatetags', 'goflow2.runtime.templatetags', 'goflow.workflow.templatetags', 'goflow.graphics2.templatetags'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD Licence',
        'Operating System :: OS Independent',
        'Programming Language :: Python3',
        'Framework :: Django2.*',
    ],
    include_package_data=True,
    zip_safe=False,
)
