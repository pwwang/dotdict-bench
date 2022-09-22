# dotdict-bench

Benchmarking for dot-accessible dict packages in python

[![deps](https://img.shields.io/librariesio/release/pypi/dotdict-bench?style=flat-square)](https://libraries.io/github/pwwang/dotdict-bench#repository_dependencies)


## Package Information

As of 2022-09-21 22:17:07.486334

|Package|Version|Last Commit|Stars|Forks|Description|
|-------|-------|-----------|-----|-----|-----------|
|<a target="_blank" href="https://github.com/mewwts/addict">addict</a>|2.4.0|Tue, 05 Jan 2021 07:16:38 GMT|2277|137|[(i)](# "The Python Dict that's better than heroin.")|
|<a target="_blank" href="https://github.com/cdgriffith/Box">python-box</a>|6.0.2|Sat, 02 Apr 2022 02:24:21 GMT|2062|89|[(i)](# "Python dictionaries with advanced dot notation access")|
|<a target="_blank" href="https://github.com/drgrib/dotmap">dotmap</a>|1.3.30|Wed, 06 Apr 2022 16:26:33 GMT|366|43|[(i)](# "Dot access dictionary with dynamic hierarchy creation and ordered iteration")|
|<a target="_blank" href="https://github.com/rnag/dotwiz">dotwiz</a>|0.4.0|Wed, 21 Sep 2022 22:23:19 GMT|20|1|[(i)](# "A blazing fast dict subclass that supports dot access notation.")|
|<a target="_blank" href="https://github.com/makinacorpus/easydict">easydict</a>|1.9|Sun, 28 Feb 2021 10:26:53 GMT|207|39|[(i)](# "Access dict values as attributes (works recursively)")|
|<a target="_blank" href="https://github.com/polydojo/dotsi">dotsi</a>|0.0.3|Sun, 22 Nov 2020 16:48:22 GMT|18|1|[(i)](# "Dot-accessible, update-aware Python dicts (& lists). Works recursively, like a charm.")|
|<a target="_blank" href="https://github.com/srevenant/dictlib">dictlib</a>|1.1.5|Thu, 15 Aug 2019 23:10:47 GMT|14|3|[(i)](# "python: a lightweight add-on for dictionaries, featuring deep dictionary union, dictionary keys as object attributes (in code dict.key.sub.value notation) as well as a separate string dig/dug for using strings with dot notation on native dictionaries")|
|<a target="_blank" href="https://github.com/pwwang/diot">diot</a>|0.1.6|Thu, 12 May 2022 20:37:59 GMT|7|2|[(i)](# "Python dictionary with dot notation")|

## Creating an object of the dict subclass

How the packages create an object of the dict subclass

| |Created|
|-|-----------------------|
|<a target="_blank" href="https://github.com/mewwts/addict">addict</a>|`{'a': {'b': {'c': 1}}}` **Type**: `Dict`|
|<a target="_blank" href="https://github.com/cdgriffith/Box">python-box</a>|`{'a': {'b': {'c': 1}}}` **Type**: `Box`|
|<a target="_blank" href="https://github.com/drgrib/dotmap">dotmap</a>|`DotMap(a=DotMap(b=DotMap(c=1)))` **Type**: `DotMap`|
|<a target="_blank" href="https://github.com/rnag/dotwiz">dotwiz</a>|`✫(a=✫(b=✫(c=1)))` **Type**: `DotWiz`|
|<a target="_blank" href="https://github.com/makinacorpus/easydict">easydict</a>|`{'a': {'b': {'c': 1}}}` **Type**: `EasyDict`|
|<a target="_blank" href="https://github.com/polydojo/dotsi">dotsi</a>|`{'a': {'b': {'c': 1}}}` **Type**: `DotsiDict`|
|<a target="_blank" href="https://github.com/srevenant/dictlib">dictlib</a>|`{'a': {'b': {'c': 1}}}` **Type**: `Dict`|
|<a target="_blank" href="https://github.com/pwwang/diot">diot</a>|`{'a': Diot({'b': Diot({'c': 1})})}` **Type**: `Diot`|

## Creating a dict with preserved keys

How the packages create a dict with preserved keys
(e.g. `keys`, `values`, `items`, etc)

Literally, `{"keys": 1}`


| |Created or error|
|-|-----------------------|
|<a target="_blank" href="https://github.com/mewwts/addict">addict</a>|{'keys': 1}|
|<a target="_blank" href="https://github.com/cdgriffith/Box">python-box</a>|{'keys': 1}|
|<a target="_blank" href="https://github.com/drgrib/dotmap">dotmap</a>|DotMap(keys=1)|
|<a target="_blank" href="https://github.com/rnag/dotwiz">dotwiz</a>|✫(keys=1)|
|<a target="_blank" href="https://github.com/makinacorpus/easydict">easydict</a>|{'keys': 1}|
|<a target="_blank" href="https://github.com/polydojo/dotsi">dotsi</a>|{'keys': 1}|
|<a target="_blank" href="https://github.com/srevenant/dictlib">dictlib</a>|Key 'keys' conflicts with reserved word|
|<a target="_blank" href="https://github.com/pwwang/diot">diot</a>|{'keys': 1}|

## Creating a dict with magic keys

How the packages create a dict with magic keys
(e.g. `__name__`, `__class__`, etc)

Literally, `{"__name__": 1}`


| |Created or error|
|-|-----------------------|
|<a target="_blank" href="https://github.com/mewwts/addict">addict</a>|`{'__name__': 1}`|
|<a target="_blank" href="https://github.com/cdgriffith/Box">python-box</a>|`{'__name__': 1}`|
|<a target="_blank" href="https://github.com/drgrib/dotmap">dotmap</a>|`DotMap(__name__=1)`|
|<a target="_blank" href="https://github.com/rnag/dotwiz">dotwiz</a>|`✫(__name__=1)`|
|<a target="_blank" href="https://github.com/makinacorpus/easydict">easydict</a>|`{'__name__': 1}`|
|<a target="_blank" href="https://github.com/polydojo/dotsi">dotsi</a>|`{'__name__': 1}`|
|<a target="_blank" href="https://github.com/srevenant/dictlib">dictlib</a>|`{'__name__': 1}`|
|<a target="_blank" href="https://github.com/pwwang/diot">diot</a>|`{'__name__': 1}`|

## Accessing values

How the packages to access values

Literally `1` from `{"a": {"b": {"c": 1}}}`


| |Way to access value|
|-|-----------------------|
|<a target="_blank" href="https://github.com/mewwts/addict">addict</a>|`<dict>.a.b.c` or `<dict>['a']['b']['c']`|
|<a target="_blank" href="https://github.com/cdgriffith/Box">python-box</a>|`<dict>.a.b.c` or `<dict>['a']['b']['c']`|
|<a target="_blank" href="https://github.com/drgrib/dotmap">dotmap</a>|`<dict>.a.b.c` or `<dict>['a']['b']['c']`|
|<a target="_blank" href="https://github.com/rnag/dotwiz">dotwiz</a>|`<dict>.a.b.c` or `<dict>['a']['b']['c']`|
|<a target="_blank" href="https://github.com/makinacorpus/easydict">easydict</a>|`<dict>.a.b.c` or `<dict>['a']['b']['c']`|
|<a target="_blank" href="https://github.com/polydojo/dotsi">dotsi</a>|`<dict>.a.b.c` or `<dict>['a']['b']['c']`|
|<a target="_blank" href="https://github.com/srevenant/dictlib">dictlib</a>|`dictlib.dig(<dict>, 'a.b.c')` or `dictlib.Dict(<dict>).a.b.c`|
|<a target="_blank" href="https://github.com/pwwang/diot">diot</a>|`<dict>.a.b.c` or `<dict>['a']['b']['c']`|

## Automatic Hierarchy

Whether a hierarchical structure is created by dot notation

Literally `<dict>.a.b.c = 1` creates `{"a": {"b": {"c": 1}}}`


| |Created or error|
|-|-----------------------|
|<a target="_blank" href="https://github.com/mewwts/addict">addict</a>|`{'a': {'b': {'c': 1}}}`|
|<a target="_blank" href="https://github.com/cdgriffith/Box">python-box</a>|KeyError: "'Box' object has no attribute 'a'"|
|<a target="_blank" href="https://github.com/drgrib/dotmap">dotmap</a>|`DotMap(a=DotMap(b=DotMap(c=1)))`|
|<a target="_blank" href="https://github.com/rnag/dotwiz">dotwiz</a>|AttributeError: 'DotWiz' object has no attribute 'a'|
|<a target="_blank" href="https://github.com/makinacorpus/easydict">easydict</a>|AttributeError: 'EasyDict' object has no attribute 'a'|
|<a target="_blank" href="https://github.com/polydojo/dotsi">dotsi</a>|KeyError: 'a'|
|<a target="_blank" href="https://github.com/srevenant/dictlib">dictlib</a>|KeyError: 'a'|
|<a target="_blank" href="https://github.com/pwwang/diot">diot</a>|AttributeError: a|

## Accessing values with preserved keys

How to access values with conflict keys

Literally, accessing values from `{"keys": 1, "__name__": 2}`


|Package|`obj.keys`|`obj['keys']`|`obj.__name__`|`obj['__name__']`|
|---|---|---|---|---|
|<a target="_blank" href="https://github.com/mewwts/addict">addict</a>|`<built-in method keys of Dict object at 0x7fa6dd61ae50>`|`1`|`2`|`2`|
|<a target="_blank" href="https://github.com/cdgriffith/Box">python-box</a>|`<bound method Box.keys of Box({'keys': 1, '__name__': 2})>`|`1`|`2`|`2`|
|<a target="_blank" href="https://github.com/drgrib/dotmap">dotmap</a>|`<bound method DotMap.keys of DotMap(keys=1, __name__=2)>`|`1`|`AttributeError: __name__`|`2`|
|<a target="_blank" href="https://github.com/rnag/dotwiz">dotwiz</a>|`1`|`1`|`2`|`2`|
|<a target="_blank" href="https://github.com/makinacorpus/easydict">easydict</a>|`1`|`1`|`2`|`2`|
|<a target="_blank" href="https://github.com/polydojo/dotsi">dotsi</a>|`<built-in method keys of DotsiDict object at 0x7fa6dd95d5e0>`|`1`|`2`|`2`|
|<a target="_blank" href="https://github.com/srevenant/dictlib">dictlib</a>|`Can't create`|`Can't create`|`Can't create`|`Can't create`|
|<a target="_blank" href="https://github.com/pwwang/diot">diot</a>|`<built-in method keys of Diot object at 0x7fa6dd61ae50>`|`1`|`2`|`2`|

