from socket import gethostname

from discord_webhook import DiscordEmbed, DiscordWebhook
from yaml import dump

from .utils import Code


class DiscordLogger:
    """
    Python message transporter for Discord
    """

    COLORS = {
        "default": 2040357,
        "error": 14362664,
        "warn": 16497928,
        "info": 2196944,
        "verbose": 6559689,
        "debug": 2196944,
        "success": 2210373,
    }
    EMOJIS = {
        "default": ":loudspeaker:",
        "error": ":x:",
        "warn": ":warning:",
        "info": ":bell:",
        "verbose": ":mega:",
        "debug": ":microscope:",
        "success": ":rocket:",
    }

    def __init__(self, webhook_url, **kwargs):
        if webhook_url is None:
            raise ValueError("The field webhook_url cannot be:", webhook_url)
        self.webhook_url = str(webhook_url)

        self.application_name = kwargs.get("application_name", "Application")
        if self.application_name is not None:
            self.application_name = str(self.application_name)

        self.service_name = kwargs.get("service_name", "Status Bot")
        if self.service_name is not None:
            self.service_name = str(self.service_name)

        self.service_icon_url = kwargs.get("service_icon_url")
        if self.service_icon_url is not None:
            self.service_icon_url = str(self.service_icon_url)

        self.service_environment = kwargs.get("service_environment")
        if self.service_environment is not None:
            self.service_environment = str(self.service_environment)

        self.host_name = gethostname()
        if kwargs.get("display_hostname") is False:
            self.host_name = None

        self.default_level = kwargs.get("default_level")
        if self.default_level not in self.COLORS.keys():
            self.default_level = "default"

        self.discord = DiscordWebhook(
            url=self.webhook_url, username=self.application_name
        )

    def __remove_embeds(self):
        existing_embeds = self.discord.get_embeds()
        for i in reversed(range(0, len(existing_embeds))):
            self.discord.remove_embed(i)

    def construct(
        self,
        title=None,
        description=None,
        level=None,
        error=None,
        metadata=None,
    ):
        self.__remove_embeds()

        _level = level
        if _level is None:
            _level = self.default_level
        if error is not None:
            _level = "error"

        _color = self.COLORS.get(_level)

        _title = ""
        if title is not None:
            _title = self.EMOJIS.get(_level) + " " + str(title)

        _description = ""
        if description is not None:
            _description = str(description)

        embed = DiscordEmbed(title=_title, description=_description, color=_color)
        embed.set_author(name=self.service_name, icon_url=self.service_icon_url)

        if metadata is not None:
            _metadata = dump(
                metadata, indent=4, default_flow_style=False, sort_keys=False
            )

            embed.add_embed_field(
                name="Metadata", value=Code(str(_metadata)), inline=False
            )

        if error is not None:
            embed.add_embed_field(name="Error", value=Code(str(error)), inline=False)

        if self.service_environment is not None:
            embed.add_embed_field(name="Environment", value=self.service_environment)
        if self.host_name is not None:
            embed.add_embed_field(name="Host", value=self.host_name)

        embed.set_timestamp()

        self.discord.add_embed(embed)

    def send(self):
        response = self.discord.execute()
        return response
