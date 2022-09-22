from ensurepip import version
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


class BenchCaseAccessValue(BenchCase):

    def run(self):
        return self.api.access_way
