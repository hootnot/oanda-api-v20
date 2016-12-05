# -*- coding: utf8 -*-
"""dirstruct.

generate document directory structure.
"""
import sys
import os
import inspect
from importlib import import_module


def get_classes(modName):
    """return a list of all classes in a module."""
    classNames = []
    for name, obj in inspect.getmembers(sys.modules[modName]):
        if inspect.isclass(obj):
            classNames.append(name)

    return classNames


if __name__ == "__main__":

    destDir = sys.argv[1]
    modToDoc = sys.argv[2]
    import_module(modToDoc)

    if not os.path.exists(destDir):
        os.makedirs(destDir)

    for cls in get_classes(modToDoc):
        with open(os.path.join(destDir, "{}.rst".format(cls)), "w") as F:
            #    :show-inheritance:\n
            F.write("""{cls}\n"""
                    """{ul}\n"""
                    """\n"""
                    """.. autoclass:: {mod}.{cls}\n"""
                    """    :members:\n"""
                    """    :undoc-members:\n"""
                    """    :inherited-members:\n"""
                    """    :special-members: __init__\n""".format(
                        cls=cls,
                        ul=len(cls)*"~",
                        mod=modToDoc))
