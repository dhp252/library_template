# also available through the world wide web at this URL:
# http://opensource.org/licenses/OSL-3.0
# If you did not receive a copy of the license and are unable to obtain it
# Copyright (c) 2008 - 2013, EllisLab, Inc. (http://ellislab.com/)
# http://opensource.org/licenses/OSL-3.0 Open Software License (OSL 3.0)

def import_submodules(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    import importlib, pkgutil

    if isinstance(package, str):
        package = importlib.import_module(package)
    modules = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        modules[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            modules.update(import_submodules(full_name))
    return modules


def walk_path(path,exts='img'):
    """recursively walk into path to get files ended with "exts"
    """
    import os

    if exts == 'img':
        exts = ['jpg','jpeg','png']

    img_paths = [os.path.join(root, file)
                for root, dirs, files in os.walk(path)
                for file in files
                if  file.split('.')[-1].lower() in exts]

    return img_paths


def ensure_license(path='.', verbose=True):
    """add license to *.py files in path"""

    PHRASE = """# also available through the world wide web at this URL:
# http://opensource.org/licenses/OSL-3.0
# If you did not receive a copy of the license and are unable to obtain it
# Copyright (c) 2008 - 2013, EllisLab, Inc. (http://ellislab.com/)
# http://opensource.org/licenses/OSL-3.0 Open Software License (OSL 3.0)"""

    def module_has_license(module_path):
        with open(module_path,'r') as f:
            content = f.read()
        has_license = PHRASE in content
        return has_license, content

    module_paths = walk_path(path,exts='py')
    for module_path in module_paths:
        has_lis, content = module_has_license(module_path)
        if not has_lis:
            content = content.lstrip()
            with open(module_path, 'w') as f:
                f.write(PHRASE+'\n\n'+content)
            if verbose:
                print(f'Added license to {module_path}')


def parse_requirements(path='requirements.txt'):
    """
    example:
    >>> parse_requirements('requirements.txt')
    ['numpy>=1.18.5', 'matplotlib>=3.3.3', 'scikit-learn>=0.23.2']
    """
    with open(path,'r') as f:
        lines = f.read()
    lines = lines.split('\n')
    lines = list(filter(lambda line: not line.strip().startswith('#'), lines))
    lines = list(filter(lambda line: line != '', lines))
    return lines
