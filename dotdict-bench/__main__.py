from pyparam import Params
from benchwork import BenchSuite, run_suite

from .sets import (
    BenchSetPackageInfo,
    BenchSetCreatingDict,
    BenchSetCreatingDictWithPresevedKeys,
    BenchSetCreatingDictWithMagicKeys,
    BenchSetAccessValue,
    BenchSetRecursiveDotAccess,
    BenchSetAutomaticHierarchy,
    BenchSetConflictKeys,
    BenchSetDashKeys,
    BenchSetFrozenDict,
    BenchSetKeyTransform,
)


class BenchSuite(BenchSuite):
    """Benchmarking for dot-accessible dict packages in python

    [![deps](https://img.shields.io/librariesio/release/pypi/dotdict-bench?style=flat-square)](https://libraries.io/github/pwwang/dotdict-bench#repository_dependencies)
    """
    set_classes = [
        BenchSetPackageInfo,
        BenchSetCreatingDict,
        BenchSetCreatingDictWithPresevedKeys,
        BenchSetCreatingDictWithMagicKeys,
        BenchSetAccessValue,
        BenchSetRecursiveDotAccess,
        BenchSetAutomaticHierarchy,
        BenchSetConflictKeys,
        BenchSetDashKeys,
        BenchSetFrozenDict,
        BenchSetKeyTransform,
    ]


def main():
    params = Params(
        help_on_void=False,
        prog="dotdict-bench",
        desc="Benchmarking for dot-accessible dict packages in python",
    )
    params.add_param(
        "token",
        default=None,
        type=str,
        desc="Github token or a file containing the token",
    )
    params.add_param(
        "outfile",
        default="<stdout>",
        desc="Output file",
    )
    args = params.parse()
    run_suite(BenchSuite, args, "dotdict-bench", args.outfile)

if __name__ == "__main__":
    main()
