from setuptools import setup, Extension
from torch.utils import cpp_extension

module_name = "TCS_cuSol"
cpp_files = ["tcs_cuSol.cpp","tcs_cuSol_kernel.cu"]
#inc = ["/usr/include"]
setup(name=module_name,
      ext_modules=[Extension(
            name=module_name,
            sources=cpp_files,
            include_dirs=cpp_extension.include_paths(),
            libraries=["cusolver"],
            language='c++')],
      cmdclass={'build_ext': cpp_extension.BuildExtension})

