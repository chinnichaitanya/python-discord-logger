# Python Discord Logger

A custom message logger to Discord for Python.


## Install
Install via pip: `pip install discord-logger`


## Basic Usage
```
from discord_logger import DiscordLogger

options = {
    "application_name": "My Server",
    "service_name": "My API",
    "service_icon_url": "my application url",
    "service_environment": "Production",
    "default_level": "info",
}
logger = DiscordLogger(webhook_url="your webhook url", **options)
```

The `Host` is automatically added for every message for easy identification.


## Examples

- Send messages with different log-levels

- Set Service name, icon and environment for easy identification

- Send complete error traceback
