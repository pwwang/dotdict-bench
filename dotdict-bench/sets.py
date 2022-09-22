from datetime import datetime
from benchwork import BenchSet, BenchSetTable

from .cases import (
    BenchCasePackageInfo,
    BenchCaseCreatingDict,
    BenchCaseCreatingDictWithPresevedKeys,
    BenchCaseCreatingDictWithMagicKeys,
    BenchCaseAccessValue,
    BenchCaseAutomaticHierarchy,
    BenchCasePreservedKeys,
    BenchCaseDashKeys,
)
from .apis import APIBase
from .utils import format_doc


@format_doc(now=datetime.now())
class BenchSetPackageInfo(BenchSet):
    """As of {now}"""

    case = BenchCasePackageInfo
    api_base = APIBase
    title = "Package Information"

    def run_cases(self):
        out = [
            f"|Package|Version|Last Commit|Stars|Forks|Description|",
            f"|-------|-------|-----------|-----|-----|-----------|",
        ]
        for case in self.cases:
            ret = str(case.run())
            ret = ret.replace("\n", "<br />")
            out.append(ret)
        return "\n".join(out)


class BenchSetCreatingDict(BenchSetTable):
    """How the packages create an object of the dict subclass"""

    api_base = APIBase
    case = BenchCaseCreatingDict
    title = "Creating an object of the dict subclass"
    header = "Created"


class BenchSetCreatingDictWithPresevedKeys(BenchSetTable):
    """How the packages create a dict with preserved keys
    (e.g. `keys`, `values`, `items`, etc)

    Literally, `{"keys": 1}`
    """

    api_base = APIBase
    case = BenchCaseCreatingDictWithPresevedKeys
    title = "Creating a dict with preserved keys"
    header = "Created or error"


class BenchSetCreatingDictWithMagicKeys(BenchSetTable):
    """How the packages create a dict with magic keys
    (e.g. `__name__`, `__class__`, etc)

    Literally, `{"__name__": 1}`
    """

    api_base = APIBase
    case = BenchCaseCreatingDictWithMagicKeys
    title = "Creating a dict with magic keys"
    header = "Created or error"


class BenchSetAccessValue(BenchSetTable):
    """How the packages to access values

    Literally `1` from `{"a": {"b": {"c": 1}}}`
    """

    api_base = APIBase
    case = BenchCaseAccessValue
    title = "Accessing values"
    header = "Way to access value"


class BenchSetAutomaticHierarchy(BenchSetTable):
    """Whether a hierarchical structure is created by dot notation

    Literally `<dict>.a.b.c = 1` creates `{"a": {"b": {"c": 1}}}`
    """

    api_base = APIBase
    case = BenchCaseAutomaticHierarchy
    title = "Automatic Hierarchy"
    header = "Created or error"


class BenchSetConflictKeys(BenchSet):
    """How to access values with conflict keys

    Literally, accessing values from `{"keys": 1, "__name__": 2}`
    """

    api_base = APIBase
    case = BenchCasePreservedKeys
    title = "Accessing values with preserved keys"

    def run_cases(self):
        out = [
            "|Package|`obj.keys`|`obj['keys']`"
            "|`obj.__name__`|`obj['__name__']`|",
            f"|---|---|---|---|---|",
        ]
        for case in self.cases:
            ret = case.run()
            ret = [str(r).replace("\n", "<br />") for r in ret]
            ret = [f"`{r}`" for r in ret]
            out.append(f"|{case.api.name}|{'|'.join(ret)}|")
        return "\n".join(out)


class BenchSetDashKeys(BenchSet):
    """How the values with keys with dash are accessed

    Literally `<dict>.a_b` for `{"a-b": 1}`
    """

    api_base = APIBase
    case = BenchCaseDashKeys
    title = "Accessing dashed keys"

    def run_cases(self):
        out = [
            "|Package|`obj.a_b`|`obj['a_b']`|`obj['a-b']`|",
            f"|---|---|---|---|",
        ]
        for case in self.cases:
            ret = case.run()
            ret = [str(r).replace("\n", "<br />") for r in ret]
            ret = [f"`{r}`" for r in ret]
            out.append(f"|{case.api.name}|{'|'.join(ret)}|")
        return "\n".join(out)
