from benchwork import BenchSet, BenchSetTable

from .cases import BenchCasePackageInfo, BenchCaseAccessValue
from .apis import APIBase


class BenchSetPackageInfo(BenchSet):

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


class BenchSetAccessValue(BenchSetTable):
    """How the packages to access values

    Literally `1` from `{"a": {"b": {"c": 1}}}`
    """

    api_base = APIBase
    case = BenchCaseAccessValue
    title = "Accessing values"
    header = "Way to access value"
