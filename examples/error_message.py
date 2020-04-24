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
