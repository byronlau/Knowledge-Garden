from datetime import datetime
def on_config(config, **kwargs):
    config.copyright = f"版权所有 © 2023-{datetime.now().year} <a href=\"https://github.com/orgs/BioITee/discussions\" target=\"_blank\">BioIT 爱好者</a>"
