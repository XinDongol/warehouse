## If-or-not-dir

```Python
def ifornot_dir(directory):
##please give current dir
    import os
    if not os.path.exists(directory):
    	os.makedirs(directory)


```
