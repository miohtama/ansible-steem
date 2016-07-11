# Read WIF key from brainkey file for ansible consumption

import sys
import json

keyfile = sys.argv[1]
data = json.load(open(keyfile, "rt"))
print(data["wif_priv_key"])


