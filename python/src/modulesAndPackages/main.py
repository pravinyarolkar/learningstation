from utils import get_caps

print(get_caps("this is sample text"))

# importing main module from main package
from myMainPackage import main_module

print(main_module.myMainPackageFunc())

# importing sub function from sub module from sub package inside main package
from myMainPackage.mySubPackage.sub_module import my_sub_package_func

print(my_sub_package_func())

from myMainPackage.mySubPackage import sub_module_1

print(f"we are in {__name__} module")

if __name__ == "__main__":
    print("as we are in __main__ module this line is printing")