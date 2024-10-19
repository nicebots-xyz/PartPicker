# PartPicker Bot

>[!WARNING]
>This Discord bot is subject to special licensing terms. Please read the full [NiceBots Discord Bot License Agreement Version 1.0](https://docs.nicebots.xyz/en/NiceBots-Discord-Bot-License-Agreement-Version-1-0) for complete details.

>[!IMPORTANT]
>**Key License Points:**
>- Personal or internal business use only
>- No commercial or economic gain (including donations)
>- All modifications must be publicly shared
>- Clear attribution required
>- Contributions grant full rights to NiceBots.xyz
>- License termination upon legal dispute
>- No use of NiceBots.xyz trademarks

>[!NOTE]
>This summary is not legally binding. Refer to the full license text for all terms and conditions.

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

>[!IMPORTANT]
>Follow these steps carefully to comply with licensing terms:

1. **Clone the Repository**
```
git clone https://github.com/nicebots-xyz/auto-pc-part-picker.git
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

4. **Attribution and Disclosure**
>[!CAUTION]
>To follow the license terms, you must include the following in your Discord Bot Description:
```
This Discord Bot, [Bot Name], is based on [Software Name] by NiceBots.xyz.
Original Source: [Link to Original Source]
This version has been modified by [Your Name/Entity], accessible at [Link to Your Fork],
is operated by [Your Name/Entity] and is not affiliated with NiceBots.xyz or Discord Inc.
```

5. **Run the Bot**
   ```
   pdm run start
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

## Legal Compliance

>[!CAUTION]
>- Ensure all usage complies with the [full license agreement](https://docs.nicebots.xyz/en/NiceBots-Discord-Bot-License-Agreement-Version-1-0).
>- Maintain all copyright notices and license terms in your fork.
>- Do not use for any commercial purposes, including indirect methods like donations.

## Support

>[!NOTE]
>For issues or questions:
>- Join the [official Discord server](https://paill.at/OjTuQ)
>- Send an email to hello [at] nicebots.xyz

>[!IMPORTANT]
>By using, modifying, or distributing this bot, you agree to the terms of the NiceBots Discord Bot License Agreement Version 1.0.