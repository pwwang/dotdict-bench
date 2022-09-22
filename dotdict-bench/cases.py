from benchwork import BenchCase


class BenchCasePackageInfo(BenchCase):

    def run(self):
        packageinfo = self.api.github_meta
        version = self.api.version

        return (
            f"|{self.api.name}"
            f"|{version}"
            f"|{packageinfo['last_commit']}"
            f"|{packageinfo['stars']}"
            f"|{packageinfo['forks']}"
            f"|[(i)](# \"{packageinfo['descr']}\")|"
        )


class BenchCaseCreatingDict(BenchCase):

    def run(self):
        try:
            out = self.api.create({"a": {"b": {"c": 1}}})
            return f"`{out}` **Type**: `{type(out).__name__}`"
        except KeyError as e1:
            return f"KeyError: {e1}"
        except AttributeError as e2:
            return f"AttributeError: {e2}"
        except Exception as e3:
            return e3


class BenchCaseCreatingDictWithPresevedKeys(BenchCase):

    def run(self):
        try:
            return self.api.create({"keys": 1})
        except KeyError as e1:
            return f"KeyError: {e1}"
        except AttributeError as e2:
            return f"AttributeError: {e2}"
        except Exception as e3:
            return e3


class BenchCaseCreatingDictWithMagicKeys(BenchCase):

    def run(self):
        try:
            out = self.api.create({"__name__": 1})
            return f"`{out}`"
        except KeyError as e1:
            return f"KeyError: {e1}"
        except AttributeError as e2:
            return f"AttributeError: {e2}"
        except Exception as e3:
            return e3


class BenchCaseAccessValue(BenchCase):

    def run(self):
        return self.api.access_way


class BenchCaseAutomaticHierarchy(BenchCase):

    def run(self):
        try:
            d = self.api.create({})
            d.a.b.c = 1
        except KeyError as e1:
            return f"KeyError: {e1}"
        except AttributeError as e2:
            return f"AttributeError: {e2}"
        else:
            return f"`{d}`"


class BenchCasePreservedKeys(BenchCase):

    def run(self):
        out = []
        try:
            d = self.api.create({"keys": 1, "__name__": 2})
        except Exception:
            return ["Can't create"] * 4

        try:
            o = d.keys
        except KeyError as e1:
            o = f"KeyError: {e1}"
        except AttributeError as e2:
            o = f"AttributeError: {e2}"
        except Exception as e3:
            o = str(e3)
        out.append(o)

        try:
            o = d["keys"]
        except KeyError as e1:
            o = f"KeyError: {e1}"
        except AttributeError as e2:
            o = f"AttributeError: {e2}"
        except Exception as e3:
            o = str(e3)
        out.append(o)

        try:
            o = d.__name__
        except KeyError as e1:
            o = f"KeyError: {e1}"
        except AttributeError as e2:
            o = f"AttributeError: {e2}"
        except Exception as e3:
            o = str(e3)
        out.append(o)

        try:
            o = d["__name__"]
        except KeyError as e1:
            o = f"KeyError: {e1}"
        except AttributeError as e2:
            o = f"AttributeError: {e2}"
        except Exception as e3:
            o = str(e3)
        out.append(o)

        return out
