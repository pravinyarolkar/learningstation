from utils import get_caps

print(get_caps("this is sample text"))

# importing main module from main package
from myMainPackage import main_module

print(main_module.myMainPackageFunc())


# importing sub function from sub module from sub package inside main package
from myMainPackage.mySubPackage.sub_module import my_sub_package_func

print(my_sub_package_func())