from conans import ConanFile
import os

class CLI11Conan(ConanFile):
    name = "CLI11"
    license = "https://github.com/CLIUtils/CLI11/blob/master/LICENSE"
    description = "CLI11 is a command line parser for C++11 and beyond that provides a rich feature set with a simple and intuitive interface."
    url = "https://github.com/CLIUtils/CLI11"

    # Iceshard conan tools
    python_requires = "conan-iceshard-tools/0.5.4@iceshard/stable"
    python_requires_extend = "conan-iceshard-tools.IceTools"

    settings = "compiler"

    def package_id(self):
        self.info.header_only()

    def init(self):
        self.ice_init("none")

    def package(self):
        self.copy("*", src=os.path.join(self._ice.out_dir, "include"), dst="include")
        self.copy("LICENSE", src=self._ice.out_dir)
        self.copy("README.md", src=self._ice.out_dir)

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
