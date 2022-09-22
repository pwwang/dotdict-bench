from __future__ import annotations

import json
from abc import ABC, abstractproperty
from os import access
from pathlib import Path
from tempfile import gettempdir
from typing import TYPE_CHECKING, Mapping

import addict
import box
import glom
import dotmap
import dotwiz
import easydict
import dotsi
import dictlib
import diot

import importlib_metadata as im
from github import Github
from benchwork import BenchAPI

if TYPE_CHECKING:
    from types import ModuleType


class APIBase(BenchAPI, ABC):

    _SUBCLASSES = None

    @abstractproperty
    def package(self) -> ModuleType:
        ...

    @abstractproperty
    def repo(self) -> str:
        ...

    @property
    def github_meta(self) -> Mapping[str, str]:
        cachefile = Path(gettempdir()).joinpath(
            f"dotdict-{self._name}-v{self.version}.github_meta.json"
        )
        if cachefile.is_file():
            return json.loads(cachefile.read_text())

        token = self.args.token
        if token and Path(token).is_file():
            token = Path(token).read_text().strip()

        g = Github(token, per_page=1)
        r = g.get_repo(self.repo)
        data = {
            "stars": r.stargazers_count,
            "forks": r.forks_count,
            "last_commit": r.get_commits()[0].last_modified,
            "descr": r.description,
        }
        cachefile.write_text(json.dumps(data))
        return data

    @property
    def _name(self) -> str:
        return self.package.__name__

    @property
    def name(self) -> str:
        return (
            f'<a target="_blank" href="https://github.com/{self.repo}">'
            f'{self._name}</a>'
        )

    @property
    def access_way(self) -> str:
        return "`<dict>.a.b.c` or `<dict>['a']['b']['c']`"

    @property
    def version(self) -> str:
        return im.version(self._name)


class AddictAPI(APIBase):

    package = addict
    repo = "mewwts/addict"


class BoxAPI(APIBase):

    package = box
    repo = "cdgriffith/Box"

    @property
    def _name(self) -> str:
        return "python-box"


class GlomAPI(APIBase):

    package = glom
    repo = "mahmoud/glom"
    access_way = "`glom(<dict>, 'a.b.c')`"


class DotMapAPI(APIBase):

    package = dotmap
    repo = "drgrib/dotmap"


class DotwizAPI(APIBase):

    package = dotwiz
    repo = "rnag/dotwiz"


class EasydictAPI(APIBase):

    package = easydict
    repo = "makinacorpus/easydict"


class DotsiAPI(APIBase):

    package = dotsi
    repo = "polydojo/dotsi"


class DictLibAPI(APIBase):

    package = dictlib
    repo = "srevenant/dictlib"
    access_way = (
        "`dictlib.dig(<dict>, 'a.b.c')` "
        "or `dictlib.Dict(<dict>).a.b.c`"
    )


class DiotAPI(APIBase):

    package = diot
    repo = "pwwang/diot"
