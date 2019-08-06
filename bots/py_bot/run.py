import json
from bot import Regime


auth_path = "../auth.json"
package_path = "../package.json"
roles_path = "../roles.json"

if __name__ == "__main__":
    with open(roles_path) as roles_json:
        roles = json.load(roles_json)

    bot = Regime(roles)

    with open(auth_path) as auth_json:
        auth_data = json.load(auth_json)
        bot.run(auth_data["token"])

