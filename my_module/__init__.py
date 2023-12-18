print(__file__)

import runfiles

r = runfiles.Create()
r.Rlocation("_main/my_module/test.txt")
