# dotdict-bench

Benchmarking for dot-accessible dict packages in python

[![deps](https://img.shields.io/librariesio/release/pypi/dotdict-bench?style=flat-square)](https://libraries.io/github/pwwang/dotdict-bench#repository_dependencies)


## Package Information

|Package|Version|Last Commit|Stars|Forks|Description|
|-------|-------|-----------|-----|-----|-----------|
|<a target="_blank" href="https://github.com/mewwts/addict">addict</a>|2.4.0|Tue, 05 Jan 2021 07:16:38 GMT|2277|137|[(i)](# "The Python Dict that's better than heroin.")|
|<a target="_blank" href="https://github.com/cdgriffith/Box">python-box</a>|6.0.2|Sat, 02 Apr 2022 02:24:21 GMT|2062|89|[(i)](# "Python dictionaries with advanced dot notation access")|
|<a target="_blank" href="https://github.com/mahmoud/glom">glom</a>|22.1.0|Tue, 05 Jul 2022 07:29:39 GMT|1575|52|[(i)](# "☄️ Python's nested data operator (and CLI), for all your declarative restructuring needs. Got data? Glom it! ☄️")|
|<a target="_blank" href="https://github.com/drgrib/dotmap">dotmap</a>|1.3.30|Wed, 06 Apr 2022 16:26:33 GMT|366|43|[(i)](# "Dot access dictionary with dynamic hierarchy creation and ordered iteration")|
|<a target="_blank" href="https://github.com/rnag/dotwiz">dotwiz</a>|0.4.0|Wed, 21 Sep 2022 22:23:19 GMT|20|1|[(i)](# "A blazing fast dict subclass that supports dot access notation.")|
|<a target="_blank" href="https://github.com/makinacorpus/easydict">easydict</a>|1.9|Sun, 28 Feb 2021 10:26:53 GMT|207|39|[(i)](# "Access dict values as attributes (works recursively)")|
|<a target="_blank" href="https://github.com/polydojo/dotsi">dotsi</a>|0.0.3|Sun, 22 Nov 2020 16:48:22 GMT|18|1|[(i)](# "Dot-accessible, update-aware Python dicts (& lists). Works recursively, like a charm.")|
|<a target="_blank" href="https://github.com/srevenant/dictlib">dictlib</a>|1.1.5|Thu, 15 Aug 2019 23:10:47 GMT|14|3|[(i)](# "python: a lightweight add-on for dictionaries, featuring deep dictionary union, dictionary keys as object attributes (in code dict.key.sub.value notation) as well as a separate string dig/dug for using strings with dot notation on native dictionaries")|
|<a target="_blank" href="https://github.com/pwwang/diot">diot</a>|0.1.6|Thu, 12 May 2022 20:37:59 GMT|7|2|[(i)](# "Python dictionary with dot notation")|

## Accessing values

How the packages to access values

Literally `1` from `{"a": {"b": {"c": 1}}}`


| |Way to access value|
|-|-----------------------|
|<a target="_blank" href="https://github.com/mewwts/addict">addict</a>|`<dict>.a.b.c` or `<dict>['a']['b']['c']`|
|<a target="_blank" href="https://github.com/cdgriffith/Box">python-box</a>|`<dict>.a.b.c` or `<dict>['a']['b']['c']`|
|<a target="_blank" href="https://github.com/mahmoud/glom">glom</a>|`glom(<dict>, 'a.b.c')`|
|<a target="_blank" href="https://github.com/drgrib/dotmap">dotmap</a>|`<dict>.a.b.c` or `<dict>['a']['b']['c']`|
|<a target="_blank" href="https://github.com/rnag/dotwiz">dotwiz</a>|`<dict>.a.b.c` or `<dict>['a']['b']['c']`|
|<a target="_blank" href="https://github.com/makinacorpus/easydict">easydict</a>|`<dict>.a.b.c` or `<dict>['a']['b']['c']`|
|<a target="_blank" href="https://github.com/polydojo/dotsi">dotsi</a>|`<dict>.a.b.c` or `<dict>['a']['b']['c']`|
|<a target="_blank" href="https://github.com/srevenant/dictlib">dictlib</a>|`dictlib.dig(<dict>, 'a.b.c')` or `dictlib.Dict(<dict>).a.b.c`|
|<a target="_blank" href="https://github.com/pwwang/diot">diot</a>|`<dict>.a.b.c` or `<dict>['a']['b']['c']`|

