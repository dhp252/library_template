# also available through the world wide web at this URL:
# http://opensource.org/licenses/OSL-3.0
# If you did not receive a copy of the license and are unable to obtain it
# Copyright (c) 2008 - 2013, EllisLab, Inc. (http://ellislab.com/)
# http://opensource.org/licenses/OSL-3.0 Open Software License (OSL 3.0)

from dhp.lib_utils import import_submodules as _import_submodules

modules = _import_submodules(__name__)
for module in modules:
    exec(f"from {module} import *")
