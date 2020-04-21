# Python Discord Transport

A custom message transporter to Discord for Python.


## Install
Install via pip: `pip install discord-transport`


## Basic Usage
```
from discord-transport import DiscordTransport

discord_messager = DiscordTransport(webhook_url=)
```

The `Host` is automatically added for every message for easy identification.


## Examples

- Send messages with different log-levels

- Set Service name, icon and environment for easy identification

- Send complete error traceback
