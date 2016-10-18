from conans import ConanFile, tools
import os


class Rangev3Conan(ConanFile):
    name = "rangev3"
    version = "master"
    license = "Boost"
    url = "https://github.com/memsharded/conan-range-v3"
    code_url = "https://github.com/ericniebler/range-v3"
    # No settings/options are necessary, this is header only
    build_policy="always"

    def source(self):
        self.run("git clone %s --depth=1" % self.code_url)

    def package(self):
        self.copy("*.hpp", dst="include", src="range-v3/include")
