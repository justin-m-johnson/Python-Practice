#pip install cowsay
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])

#output:
'''
python say.py Justin
  _____________
| Hello, Justin |
  =============
             \
              \
                ^__^
                (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
'''

#cowsay.trex is another example