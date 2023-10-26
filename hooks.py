from datetime import datetime
def on_config(config, **kwargs):
    config.copyright = f"版权所有 © 2023-{datetime.now().year} <a href=\"https://github.com/byronlauee/discussions\" target=\"_blank\">橘涂拾捌</a>"
