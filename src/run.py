import json, os
from bot import Regime


package_path = "data/package.json"
roles_path = "data/roles.json"

if __name__ == "__main__":
    with open(roles_path) as roles_json:
        roles = json.load(roles_json)

    bot = Regime(roles)
    bot.run(os.environ["token"])

