"""r2e: zoom wrapper.  python r2e_z.py <page> <line> <xa> <xb> [sc] [hh] [dy] [tag]"""
import sys, importlib.util, pathlib
spec = importlib.util.spec_from_file_location('r', str(pathlib.Path(__file__).with_name('r2e_crop.py')))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
a = sys.argv[1:]
m.zoom(int(a[0]), int(a[1]), int(a[2]), int(a[3]), float(a[4]) if len(a) > 4 else 3.0,
       int(a[5]) if len(a) > 5 else 60, int(a[6]) if len(a) > 6 else 0, a[7] if len(a) > 7 else 'z')
