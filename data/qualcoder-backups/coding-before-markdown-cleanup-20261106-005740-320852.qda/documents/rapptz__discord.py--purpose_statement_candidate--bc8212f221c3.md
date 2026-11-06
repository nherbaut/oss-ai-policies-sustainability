# discord.py

[![Discord server invite](https://discord.com/api/guilds/336642139381301249/embed.png)](https://discord.gg/r3sSKJJ)

[![PyPI version info](https://img.shields.io/pypi/v/discord.py.svg)](https://pypi.python.org/pypi/discord.py)

[![PyPI supported Python versions](https://img.shields.io/pypi/pyversions/discord.py.svg)](https://pypi.python.org/pypi/discord.py)

A modern, easy to use, feature-rich, and async ready API wrapper for Discord written in Python.

## Key Features

- Modern Pythonic API using `async` and `await`.
- Proper rate limit handling.
- Optimised in both speed and memory.

## Installing

**Python 3.8 or higher is required**

To install the library without full voice support, you can just run the following command:

> [!NOTE]
> A [Virtual Environment](https://docs.python.org/3/library/venv.html) is recommended to install the library, especially on Linux where the system Python is externally managed and restricts which packages you can install on it.

``` sh
# Linux/macOS
python3 -m pip install -U discord.py

# Windows
py -3 -m pip install -U discord.py
```

Otherwise to get voice support you should run the following command:

``` sh
# Linux/macOS
python3 -m pip install -U "discord.py[voice]"

# Windows
py -3 -m pip install -U discord.py[voice]
```

To install the development version, do the following:

``` sh
$ git clone https://github.com/Rapptz/discord.py
$ cd discord.py
$ python3 -m pip install -U .[voice]
```

### Optional Packages

- [PyNaCl](https://pypi.org/project/PyNaCl/) (for voice support)

Please note that when installing voice support on Linux, you must install the following packages via your favourite package manager (e.g. `apt`, `dnf`, etc) before running the above commands:

- libffi-dev (or `libffi-devel` on some systems)
- python-dev (e.g. `python3.8-dev` for Python 3.8)

## Quick Example

``` py
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('token')
```

### Bot Example

``` py
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('token')
```

You can find more examples in the examples directory.

## Links

- [Documentation](https://discordpy.readthedocs.io/en/latest/index.html)
- [Official Discord Server](https://discord.gg/r3sSKJJ)
- [Discord API](https://discord.gg/discord-api)
