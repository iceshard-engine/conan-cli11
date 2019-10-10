from conans import ConanFile, MSBuild, tools
from shutil import copyfile
import os

class CLI11Conan(ConanFile):
    name = "CLI11"
    version = "1.8.0"
    license = "https://github.com/CLIUtils/CLI11/blob/master/LICENSE"
    description = "CLI11 is a command line parser for C++11 and beyond that provides a rich feature set with a simple and intuitive interface."
    url = "https://github.com/CLIUtils/CLI11"

    CLI_FOLDER_NAME = "cli-{}".format(version)

    def package_id(self):
        self.info.header_only()

    def source(self):
        git = tools.Git(folder=self.CLI_FOLDER_NAME)
        git.clone("https://github.com/CLIUtils/CLI11.git")
        git.checkout("master")

    def package(self):
        # self.copy("*", src=os.path.join(self.source_subfolder, "glm"), dst=os.path.join("include", "glm"))
        # self.copy("copying.txt", dst="licenses", src=self.source_subfolder)
        pass

    def package_info(self):
        pass
