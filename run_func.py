
import sys
from importlib.machinery import SourceFileLoader

def run():
  fmain = SourceFileLoader("fmain", f'wwfunc/packages/wildweb/{sys.argv[1]}/__main__.py').load_module()

  if len(sys.argv) > 2:
    args = sys.argv[2:]
    event = {}
    for arg in args:
      key, value = arg.split(":")
      event[key] = value
      ret = fmain.main(event)

  else:
    ret = fmain.main(event)

  print(ret)

if __name__ == "__main__":
  run()
