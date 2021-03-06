import json
import os
import sentry_sdk
from main.bot import Regime


roles_path = "data/roles.json"

if __name__ == "__main__":
    sentry_sdk.init(dsn=f"https://{os.environ['sentry-key']}@sentry.io/{os.environ['sentry-project']}")
    with open(roles_path) as roles_json:
        roles = json.load(roles_json)

    bot = Regime(roles)
    bot.run(os.environ["token"])

