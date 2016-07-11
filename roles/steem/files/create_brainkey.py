# Create a brainkey JSON dump into given path
#
# TODO: suggest_brain_key api not exposed? Do it in hard way.
#

import os
import subprocess
import sys
import time
import pexpect

# from steemapi.steemclient import SteemClient
#
#
# class Config():  ## Note the dependency
#     wallet_host = "localhost"
#     wallet_port = 8092
#     wallet_user = ""
#     wallet_password = ""
#     witness_url = "ws://localhost:8090/"
#     witness_user = ""
#     witness_password = ""
#
# config = Config()
# keyfile = sys.argv[1]
#
# steem = SteemClient(config)
# # steem.run()

keyfile = sys.argv[1]
assert not os.path.exists(keyfile)  # Don't overwrite existing keyfile

cli_wallet = sys.argv[2]
p = pexpect.spawn(cli_wallet)
p.expect("new >>>")
incoming = p.before.decode("utf-8")
assert not "Transport Error" in incoming, "steemd not started"

p.sendline("suggest_brain_key")
p.expect("new >>>")
inp = p.before.decode("utf-8")

# grab the JSON part from the console output
crop = inp.find("{")
inp = inp[crop:]
with open(keyfile, "wt") as out:
    print(inp, file=out)

sys.exit(0)
