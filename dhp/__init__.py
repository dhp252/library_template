# also available through the world wide web at this URL:
# http://opensource.org/licenses/OSL-3.0
# If you did not receive a copy of the license and are unable to obtain it
# Copyright (c) 2008 - 2013, EllisLab, Inc. (http://ellislab.com/)
# http://opensource.org/licenses/OSL-3.0 Open Software License (OSL 3.0)

# from pkg_resources import declare_namespace
# declare_namespace(__name__)

__packagename__      = 'dhp'
__version__          = '1.0.0'
__description__      = 'Private Multi-purpose library'
__author__           = 'Đỗ Hồng Phương'
__author_email__     = 'dhp252@gmail.com'
__url__              = 'https://github.com/dhp252/dhp'
__platforms__        = ['any']
__license__          = 'Open Software License (OSL-3.0)'
__license_files__    = 'LICENSE'
__keywords__         = ['computer vision', 'natural language processing',
                        'artificial intelligent', 'computer science',
                        'data science','data analysis','toolbox','utilities']


import pkgutil as _pkgutil
__all__ = []
_modules = []
for loader, module_name, is_pkg in  _pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    _module = loader.find_module(module_name).load_module(module_name)
    # re-export child symbols into toplevel
    # exec(f"from {module_name} import *")
    globals()[module_name] = _module # idk what this line do
    _modules.append(_module)
    # module_level = len(module_name.split('.'))
    # if is_pkg and module_level == 1:
    #     [i for i in cls.__dict__.keys() if i[:1] != '_']


def print_all_modules():
    for module in __all__:
        print(module)


def find(string, module:object=None, alternatives=True,show=True,
         full=False, caseSensity=False) -> list :
    """
    examples:
    >>> import cv2
    >>> find('sift',cv2)
    ['xfeatures2d_SIFT']
    >>> find('hist') # search within this module
    ['equalize_hist_color', 'plot_color_hist', 'visualize_model_history']
    """

    def ordered_unique(seq:iter) -> list :
        """get unique values with reserved order from seq"""
        seen = set()
        seen_add = seen.add
        return [x for x in seq if not (x in seen or seen_add(x))]


    def find_in_list(string, list_to_search,
                    alternatives=None, caseSensity=True) -> list :
        """
        ! NOTICE: alternatives not work if caseSensity is True
        params
        ------
        alternatives: list of list
            example: [
                ['find','search','explore'],
                ['save','export']
            ]
        """
        result = []

        if caseSensity:
            result = list(filter(lambda s: string in s, list_to_search))

        else:
            if alternatives is None:
                result = list(filter(lambda s: string in s.lower(), list_to_search))

            else:
                # get alt lists that contains string
                alts = list(filter(lambda alt: string in alt, alternatives))
                # flatten the list of list, remove duplications, bring "string" on top
                alts = [string] + [item for items in alts for item in items]
                alts = ordered_unique(alts)
                for alt in alts:
                    result += list(filter(lambda s: alt in s.lower(), list_to_search))

        result = ordered_unique(result)
        return result


    if module is None:
        # if module is specified, search within this module
        # memory = globals()
        memory = []
        for _module in _modules:
            pkg_name = _module.__name__.split('.')[0]
            local_in_module = [f'{pkg_name}.{mod}' for mod in dir(_module)]
            memory += local_in_module
    else:
        # or search specified module. Remember, pass "module" as obj, not name.
        memory = dir(module)

    if not full:
        # remove objects starts with "__", like "__init__"
        memory = list(filter(lambda s: s.split('.')[-1][:1] != '_', memory))

    COMMON_ALT = [
        # VERBS
        ['show','plot','print','display','visualize'],
        ['find','search','get'],
        ['extract','get'],
        ['group','combine','merge'],
        ['set','modify','change','update','convert','cvt'],
        ['add','insert','join'],
        ['pred','clf','reg','predict','classify','regression','detect','infer',
         'inference'],
        ['del','delete','remove','drop'],
        ['save','write','dump','to','store','export'],
        ['read','load','from','import'],
        ['has','in','have'],
        ['calc','calculate','compute','get'],
        ['process','preprocess'],
        ['init','make','create'],
        ['select','choose'],
        ['count','len'],
        ['test','eval','evaluate','check'],
        ['split','separate','sep'],
        ['fix','repair'],
        ['exec','run','execute'],

        # NOUNS
        ['source', 'src'],
        ['extension','ext'],
        ['len','length'],
        ['alt','alternative','alternatives'],
        ['box','bbox','boxes','bboxes'],
        ['time','timing'],
    ]

    if alternatives is True:
        alternatives = COMMON_ALT

    functions = list(map(lambda x: x.split('.')[-1], memory))
    found_symbols = find_in_list(string,
                                 list_to_search = functions,
                                 alternatives   = alternatives,
                                 caseSensity    = caseSensity)

    IGNORE_SYMBOLS = [
        'os', 'cv2', 'np', 'numpy', 'matplotlib', 'plt', 'PIL', 'Image', 'math',
        'importlib','pkgutil','functools','random','base64','warnings','tf',
        'tensorflow','inspect','re','itertools','subprocess','json','pprint',
        'pickle','six','sys','torch','time','sklearn','seabons','pandas','pd'
    ]

    filtered_symbols = [symbol for symbol in found_symbols
                     if symbol not in IGNORE_SYMBOLS]

    results = [x for y in filtered_symbols for x in memory if y in x]
    results = ordered_unique(results)
    if show:
        for result in results:
            print(result)
    else:
        return results

ff = find

if __name__=='__main__':
    pass