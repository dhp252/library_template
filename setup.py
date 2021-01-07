# also available through the world wide web at this URL:
# http://opensource.org/licenses/OSL-3.0
# If you did not receive a copy of the license and are unable to obtain it
# Copyright (c) 2008 - 2013, EllisLab, Inc. (http://ellislab.com/)
# http://opensource.org/licenses/OSL-3.0 Open Software License (OSL 3.0)

if __name__=='__main__':
    from setuptools import find_namespace_packages, find_packages, setup
    from setuptools import Command

    from dhp import (__author__, __author_email__, __description__,
                     __keywords__, __license__, __license_files__,
                     __packagename__, __platforms__, __url__, __version__)

    from dhp.lib_utils import ensure_license, parse_requirements

    with open("README.md",'r') as f:
        LONG_DESCRIPTION = f.read()
        LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'

    PKG_DIR = 'dhp'
    PYTHON_REQUIRES = '>=3.7'
    REQUIREMENTS_PATH = 'requirements.txt'

    # from https://pypi.org/classifiers/
    CLASSIFIER = [
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Open Software License 3.0 (OSL-3.0)',
        'Natural Language :: English',
        'Natural Language :: Vietnamese',
        'Operating System :: OS Independent',
        # 'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Image Processing',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Debuggers',
        'Topic :: System :: Logging',
        'Topic :: Utilities',
    ]

    class UploadCommand(Command):
        """Support setup.py upload."""

        description = 'Build and publish the package.'
        user_options = []

        @staticmethod
        def status(s):
            """Prints things in bold."""
            print('\033[1m{0}\033[0m'.format(s))

        def initialize_options(self):
            pass

        def finalize_options(self):
            pass

        def run(self):
            import os, sys
            from shutil import rmtree
            here = os.path.abspath(os.path.dirname(__file__))
            try:
                self.status('Removing previous builds…')
                rmtree(os.path.join(here, 'dist'))
            except OSError:
                pass

            self.status('Building Source and Wheel (universal) distribution…')
            os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

            self.status('Uploading the package to PyPI via Twine…')
            os.system('twine upload dist/*')

            self.status('Pushing git tags…')
            os.system('git tag v{0}'.format(__version__))
            os.system('git push --tags')

            sys.exit()

    ensure_license(path=PKG_DIR)
    # import pdb; pdb.set_trace()
    setup(
        name                          = __packagename__,
        version                       = __version__,
        description                   = __description__,
        long_description              = LONG_DESCRIPTION,
        long_description_content_type = LONG_DESCRIPTION_CONTENT_TYPE,
        author                        = __author__,
        author_email                  = __author_email__,
        maintainer                    = __author__,
        maintainer_email              = __author_email__,
        url                           = __url__,
        # download_url                  = ,
        platforms                     = __platforms__,
        license                       = __license__,
        license_files                 = __license_files__,
        python_requires               = PYTHON_REQUIRES,
        packages                      = find_namespace_packages(include=[f'{PKG_DIR}.*']), #, exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
        # packages                      = find_packages(where=PKG_DIR),
        # namespace_packages            = ['dhp'],
        install_requires              = parse_requirements(REQUIREMENTS_PATH),
        keywords                      = __keywords__,
        classifier                    = CLASSIFIER,
        # $ setup.py publish support.
        # cmdclass={
        #     'upload': UploadCommand,
        # },
    )
