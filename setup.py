from distutils.core import setup

setup(
    name='houdini',
    description="Houdini escaping library bindings for Python.",
    version='0.0.1',
    author='Zachary Voase',
    author_email='z@zacharyvoase.com',
    url='https://github.com/zacharyvoase/pyhoudini',
    py_modules=['houdini'],
    license='Public Domain',
    long_description=open('README.rst').read().decode('utf-8'),
)
