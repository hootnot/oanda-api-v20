"""dynamically add the classes for definition representations.

Most of the endpoint groups have some definitions that apply. These are
in the definitions package. It is conveniant to have access by a class
representing a specific group of definitions instead of a dictionary.
"""
import sys
from importlib import import_module


def make_definition_classes(mod):
    """Dynamically create the definition classes from module 'mod'."""
    rootpath = "oandapyV20"
    PTH = "{}.definitions.{}".format(rootpath, mod)

    M = import_module(PTH)
    for cls, cldef in M.definitions.items():
        # create the docstring dynamically
        dyndoc = """Definition representation of {}

        Definitions used in requests and responses. This
        class provides the ID and the description of the definitions.
        """.format(cls)

        # the class
        dyncls = type(cls, (object,), {'__doc__': dyndoc})

        definitions = dict()
        for K, V in cldef.items():
            setattr(dyncls, K, K)       # set as class attributes
            definitions.update({K: V})  # for mapping by __getitem__

        def mkgi(definitions):
            def __getitem__(self, definitionID):
                self._definitions = definitions
                return self._definitions[definitionID]
            return __getitem__

        setattr(dyncls, "__getitem__", mkgi(definitions))
        setattr(sys.modules["{}.definitions.{}".format(rootpath, mod)],
                cls, dyncls)

definitionModules = [
    'accounts',
    'instruments',
    'orders',
    'pricing',
    'primitives',
    'trades',
    'transactions'
]

# dynamically create all the definition classes from the modules
for M in definitionModules:
    make_definition_classes(M)
