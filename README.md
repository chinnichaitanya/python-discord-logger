# Python Discord Logger

A custom message logger to Discord for Python 3.

## Install

Install via pip: `pip install discord-logger`

## Basic Usage

```python
from discord_logger import DiscordLogger

options = {
    "application_name": "My Server",
    "service_name": "My API",
    "service_icon_url": "your icon url",
    "service_environment": "Production",
    "default_level": "info",
}

logger = DiscordLogger(webhook_url="your discord webhook url", **options)
logger.construct(title="Health Check", description="All services are running normally!")

response = logger.send()
```

![Image](images/basic_message.png "Basic Usage")

## Examples

### Set Service Name, Icon and Environment for easy identification

You can configure the log message with service name, icon and environment for easy identification. The `Host` field which is the hostname of the server is automatically added for every message.

```python
from discord_logger import DiscordLogger

webhook_url = "your discord webhook url"
options = {
    "application_name": "My Server",
    "service_name": "Backend API",
    "service_icon_url": "your icon url",
    "service_environment": "Production",
    "default_level": "info",
}

logger = DiscordLogger(webhook_url=webhook_url, **options)
logger.construct(
    title="Health Check",
    description="Issue in Auth API!",
    error="Traceback (most recent call last):\n ValueError: Database connect accepts only string as a parameter!",
)

response = logger.send()
```

![Image](images/error_message.png "Message with Service Name, Icon and Environment")

### Send messages with different log-levels

The log-level indicates the importance of the message. It changes the color of the discord message in particular. Currently supported levels are,

- `error`
- `warn`
- `info`
- `verbose`
- `debug`
- `success`

The log-level can be set during construction of the message like through the parameter `level`.

If the parameter isn't provided, it'll be set to the one given in `default_level`. Any invalid input would be ignored and the log-level would be automatically be set to `default`.

```python
from discord_logger import DiscordLogger

options = {
    "application_name": "My Server",
    "service_name": "My API",
    "service_icon_url": "your icon url",
    "service_environment": "Production",
    "default_level": "info",
}

logger = DiscordLogger(webhook_url=webhook_url, **options)
logger.construct(
    title="Celery Task Manager",
    description="Successfully completed training job for model v1.3.3!",
    level="success",
)

response = logger.send()
```

![Image](images/success_message.png "Message with success log-level")

- Send complete error traceback

The `error` field can contain any error message. It will be automatically be formatted in the final message. For example, you can send a complete traceback of an error message to debug faster!

```python
import traceback

from discord_logger import DiscordLogger


def get_traceback(e):
    tb = (
        "Traceback (most recent call last):\n"
        + "".join(traceback.format_list(traceback.extract_tb(e.__traceback__)))
        + type(e).__name__
        + ": "
        + str(e)
    )
    return tb


webhook_url = "your discord webhook url"
options = {
    "application_name": "My Server",
    "service_name": "Backend API",
    "service_icon_url": "your icon url",
    "service_environment": "Production",
    "default_level": "info",
}

err = KeyError("`email` field cannot be None")

logger = DiscordLogger(webhook_url=webhook_url, **options)
logger.construct(
    title="Runtime Exception", description=err.__str__(), error=get_traceback(err),
)

response = logger.send()
```

![Image](images/complete_error_traceback.png "Message with complete error traceback")
