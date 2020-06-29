from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration
import os


class InchiConan(ConanFile):
    name = "inchi"
    # version = '1.04'
    description = "Open-source chemical structure representation algorithm"
    homepage = "https://www.inchi-trust.org/"
    url = "https://github.com/conan-io/conan-center-index"
    topics = ("conan", "chemistry")
    license = "IUPAC/InChI-Trust InChI Licence No.1.0"
    exports_sources = [ "CMakeLists.txt" ]
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = {
       "shared": [True, False],
       "fPIC": [True, False]
    }
    default_options = {
       "shared": True,
       "fPIC": True
    }

    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"
    
    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC
    
    def configure(self):
        del self.settings.compiler.libcxx
        del self.settings.compiler.cppstd
        
    def build_requirements(self):
        self.build_requires("cmake/3.17.3")
    
    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = 'INCHI-1-API'
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["INCHI_BUILD_SHARED"] = self.options.shared
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def _patch_sources(self):
        if "patches" in self.conan_data:
            if self.version in self.conan_data["patches"]:
                for patch in self.conan_data["patches"][self.version]:
                    tools.patch(**patch)

    def build(self):
        self._patch_sources()
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        tools.rmdir(os.path.join(self.package_folder, "lib", "cmake"))
        self.copy(pattern="LICENCE*", dst="licenses", src=self._source_subfolder)


    def package_info(self):
        self.cpp_info.names["cmake_find_package"] = "Inchi"
        self.cpp_info.names["cmake_find_package_multi"] = "Inchi"
        bin_path = os.path.join(self.package_folder, "bin")
        self.output.info("Appending PATH env var with : {}".format(bin_path))
        self.env_info.PATH.append(bin_path)

        self.cpp_info.libs = tools.collect_libs(self)
        if self.settings.os == "Linux":
            self.cpp_info.system_libs.append("m")
