from socket import gethostname

from discord_webhook import DiscordEmbed, DiscordWebhook


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

    def construct(self, title, description, level=None, error=None):
        self.__remove_embeds()

        if title is not None:
            title = str(title)
        if description is not None:
            description = str(description)

        if level is None:
            level = self.default_level

        color = self.COLORS.get(level)

        if error is not None:
            color = self.COLORS.get("error")
            if description is None:
                description = "```" + str(error) + "```"
            else:
                description = description + "\n" + "```" + str(error) + "```"

        embed = DiscordEmbed(title=title, description=description, color=color)

        embed.set_author(name=self.service_name, icon_url=self.service_icon_url)

        if self.service_environment is not None:
            embed.add_embed_field(name="Environment", value=self.service_environment)
        if self.host_name is not None:
            embed.add_embed_field(name="Host", value=self.host_name)

        embed.set_timestamp()

        self.discord.add_embed(embed)

    def send(self):
        response = self.discord.execute()
        return response
