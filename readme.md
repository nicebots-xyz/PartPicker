<!--
SPDX-License-Identifier: MIT
Copyright: 2024-2026 NiceBots.xyz
-->
# PartPicker Bot

## Features

The PartPicker Bot enhances your Discord server by automatically processing PCPartPicker links:

- Detects PCPartPicker links in messages
- Creates detailed embeds with parts information
- Handles up to 5 links per message
- Ignores bot messages and messages with "no-pcpp"
- Implements automatic caching to improve performance
- Utilizes PCPartPicker requests throttling to prevent API abuse

### Advanced Features

- **Automatic Caching**: The bot stores previously fetched part information, reducing redundant API calls and improving response times for frequently shared builds.

- **Request Throttling**: To ensure fair usage of the PCPartPicker API and prevent potential rate limiting, the bot implements intelligent request throttling. This helps maintain a balance between responsiveness and responsible API usage.

## Setup

1. **Clone the Repository**
```
git clone https://github.com/nicebots-xyz/PartPicker.git
```

2. **Install Dependencies**
>[!NOTE]
>Ensure [pdm](https://pdm-project.org/en/latest/) is installed.
```
pdm install
```

3. **Configure the Bot**
Edit `config.yaml` in the root directory:
```yaml
extensions:
  ping:
    enabled: false
  partpicker:
    enabled: true
bot:
  token: YOUR TOKEN HERE
use:
  bot: true
  backend: false
```

## Usage

>[!TIP]
>1. Invite the bot to your server using the OAuth2 URL from Discord Developer Portal.
>2. Share PCPartPicker links in chat - the bot will automatically process them.
>3. Use "no-pcpp" in a message to prevent link processing.

>[!NOTE]
>Example:
>- User: "Check out my build: https://pcpartpicker.com/list/abc123"
>- Bot: *Replies with an embed containing the parts list*

## Support

>[!NOTE]
>For issues or questions:
>- Join the [official Discord server](https://nicebots.xyz/discord)
>- Send an email to hello [at] nicebots.xyz
