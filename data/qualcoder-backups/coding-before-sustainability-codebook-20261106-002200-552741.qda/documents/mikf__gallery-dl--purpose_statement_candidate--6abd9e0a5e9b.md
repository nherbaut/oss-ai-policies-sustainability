# gallery-dl

*gallery-dl* is a command-line program to download image galleries and collections from several image hosting sites (see [Supported Sites](docs/supportedsites.md)). It is a cross-platform tool with many [command-line](https://gdl-org.github.io/docs/options.html) and [configuration](https://gdl-org.github.io/docs/configuration.html) options, as well as powerful [file-naming capabilities](https://gdl-org.github.io/docs/formatting.html).

------------------------------------------------------------------------

## Migration

Active development has moved to [Codeberg](https://codeberg.org/mikf/gallery-dl)  
(see [\[Announcement\] Moving to Codeberg](https://github.com/mikf/gallery-dl/issues/9374) for details)

------------------------------------------------------------------------

<div class="contents">

</div>

[![pypi](https://img.shields.io/pypi/v/gallery-dl?logo=pypi&label=PyPI)](https://pypi.org/project/gallery-dl/) [![discord](https://img.shields.io/discord/1067148002722062416?logo=discord&label=Discord&color=blue)](https://discord.gg/rSzQwRvGnE) [![build](https://github.com/mikf/gallery-dl/actions/workflows/tests.yml/badge.svg)](https://github.com/mikf/gallery-dl/actions)

## Dependencies

- [Python](https://www.python.org/downloads/) 3.8+
- [Requests](https://requests.readthedocs.io/en/latest/)

### Optional

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) or [youtube-dl](https://ytdl-org.github.io/youtube-dl/): HLS/DASH video downloads, `ytdl` integration
- [FFmpeg](https://www.ffmpeg.org/): Pixiv Ugoira conversion
- [mkvmerge](https://www.matroska.org/downloads/mkvtoolnix.html): Accurate Ugoira frame timecodes
- [PySocks](https://pypi.org/project/PySocks/): SOCKS proxy support
- [brotli](https://github.com/google/brotli) or [brotlicffi](https://github.com/python-hyper/brotlicffi): Brotli compression support
- [zstandard](https://github.com/indygreg/python-zstandard): Zstandard compression support
- [PyYAML](https://pyyaml.org/): YAML configuration file support
- [toml](https://pypi.org/project/toml/): TOML configuration file support for Python\<3.11
- [SecretStorage](https://pypi.org/project/SecretStorage/): GNOME keyring passwords for `--cookies-from-browser`
- [Psycopg](https://www.psycopg.org/): PostgreSQL archive support
- [truststore](https://truststore.readthedocs.io/en/latest/): Native system certificate support
- [Jinja](https://jinja.palletsprojects.com/): Jinja template support

## Installation

### Pip

The stable releases of *gallery-dl* are distributed on [PyPI](https://pypi.org/) and can be easily installed or upgraded using [pip](https://pip.pypa.io/en/stable/):

``` bash
python -m pip install -U gallery-dl
```

Installing the latest dev version directly from `master` can be done with [pip](https://pip.pypa.io/en/stable/) as well:

``` bash
python -m pip install -U --force-reinstall --no-deps https://codeberg.org/mikf/gallery-dl/archive/master.tar.gz
```

Omit `--no-deps` if [Requests](https://requests.readthedocs.io/en/latest/) hasn't been installed yet.

Note: Windows users should use `py` instead of `python`.

It is advised to use the latest version of [pip](https://pip.pypa.io/en/stable/), including the essential packages `setuptools` and `wheel`. To ensure these packages are up-to-date, run

``` bash
python -m pip install --upgrade pip setuptools wheel
```

### Standalone Executable

Prebuilt executable files with a Python interpreter and required Python packages included are available for

- [Windows](https://codeberg.org/mikf/gallery-dl/releases/download/v1.32.6/gallery-dl.exe) (Requires [Microsoft Visual C++ Redistributable Package (x86)](https://aka.ms/vs/17/release/vc_redist.x86.exe))
- [Linux](https://codeberg.org/mikf/gallery-dl/releases/download/v1.32.6/gallery-dl.bin)

### Nightly Builds

Executables built from the latest commit can be found at  
<https://github.com/gdl-org/builds/releases>

### Snap

Linux users that are using a distro that is supported by [Snapd](https://docs.snapcraft.io/installing-snapd) can install *gallery-dl* from the Snap Store:

``` bash
snap install gallery-dl
```

### Chocolatey

Windows users that have [Chocolatey](https://chocolatey.org/install) installed can install *gallery-dl* from the Chocolatey Community Packages repository:

``` powershell
choco install gallery-dl
```

### Scoop

*gallery-dl* is also available in the [Scoop](https://scoop.sh/) "main" bucket for Windows users:

``` powershell
scoop install gallery-dl
```

### Homebrew

For macOS or Linux users using Homebrew:

``` bash
brew install gallery-dl
```

### MacPorts

For macOS users with MacPorts:

``` bash
sudo port install gallery-dl
```

### Docker

Using the Dockerfile in the repository:

``` bash
git clone https://codeberg.org/mikf/gallery-dl.git
cd gallery-dl/
docker build -t gallery-dl:latest .
```

Pulling image from [Docker Hub](https://hub.docker.com/r/mikf123/gallery-dl):

``` bash
docker pull mikf123/gallery-dl
docker tag mikf123/gallery-dl gallery-dl
```

Pulling image from [GitHub Container Registry](https://github.com/mikf/gallery-dl/pkgs/container/gallery-dl):

``` bash
docker pull ghcr.io/mikf/gallery-dl
docker tag ghcr.io/mikf/gallery-dl gallery-dl
```

Pulling *Nightly Build* images built from the latest commit by using the `dev` tag:

``` bash
docker pull mikf123/gallery-dl:dev
docker pull ghcr.io/mikf/gallery-dl:dev
```

To run the container you will probably want to attach some directories on the host so that the config file and downloads can persist across runs.

Make sure to either download the example config file reference in the repo and place it in the mounted volume location or touch an empty file there.

If you gave the container a different tag or are using podman then make sure you adjust. Run `docker image ls` to check the name if you are not sure.

This will remove the container after every use so you will always have a fresh environment for it to run. If you setup a ci-cd pipeline to autobuild the container you can also add a `--pull=newer` flag so that when you run it docker will check to see if there is a newer container and download it before running.

``` bash
docker run --rm  -v $HOME/Downloads/:/gallery-dl/ -v $HOME/.config/gallery-dl/gallery-dl.conf:/etc/gallery-dl.conf -it gallery-dl:latest
```

You can also add an alias to your shell for "gallery-dl" or create a simple bash script and drop it somewhere in your \$PATH to act as a shim for this command.

### Nix and Home Manager

Adding *gallery-dl* to your system environment:

``` nix
environment.systemPackages = with pkgs; [
  gallery-dl
];
```

Using `nix-shell`

``` bash
nix-shell -p gallery-dl
```

``` bash
nix-shell -p gallery-dl --run "gallery-dl <args>"
```

For Home Manager users, you can manage *gallery-dl* declaratively:

``` nix
programs.gallery-dl = {
  enable = true;
  settings = {
    extractor.base-directory = "~/Downloads";
  };
};
```

Alternatively, you can just add it to `home.packages` if you don't want to manage it declaratively:

``` nix
home.packages = with pkgs; [
  gallery-dl
];
```

After making these changes, simply rebuild your configuration and open a new shell to have *gallery-dl* available.

## Usage

To use *gallery-dl* simply call it with the URLs you wish to download images from:

``` bash
gallery-dl [OPTIONS]... URLS...
```

Use `gallery-dl --help` or see [docs/options.md](docs/options.md) for a full list of all command-line options.

### Examples

Download images; in this case from danbooru via tag search for 'bonocho':

``` bash
gallery-dl "https://danbooru.donmai.us/posts?tags=bonocho"
```

Get the direct URL of an image from a site supporting authentication with username & password:

``` bash
gallery-dl -g -u "<username>" -p "<password>" "https://twitter.com/i/web/status/604341487988576256"
```

Filter manga chapters by chapter number and language:

``` bash
gallery-dl --chapter-filter "10 <= chapter < 20" -o "lang=fr" "https://mangadex.org/title/59793dd0-a2d8-41a2-9758-8197287a8539"
```

Search a remote resource for URLs and download images from them:  
(URLs for which no extractor can be found will be silently ignored)

``` bash
gallery-dl "r:https://pastebin.com/raw/FLwrCYsT"
```

If a site's address is nonstandard for its extractor, you can prefix the URL with the extractor's name to force the use of a specific extractor:

``` bash
gallery-dl "tumblr:https://sometumblrblog.example"
```

## Configuration

Configuration files for *gallery-dl* use a JSON-based file format.

### Documentation

A list of all available configuration options and their descriptions can be found at <https://gdl-org.github.io/docs/configuration.html>.

For a default configuration file with available options set to their default values, see [docs/gallery-dl.conf](docs/gallery-dl.conf).

For a commented example with more involved settings and option usage, see [docs/gallery-dl-example.conf](docs/gallery-dl-example.conf).

### Locations

*gallery-dl* searches for configuration files in the following places:

Windows:  
- `%APPDATA%\gallery-dl\config.json`
- `%USERPROFILE%\gallery-dl\config.json`
- `%USERPROFILE%\gallery-dl.conf`

(`%USERPROFILE%` usually refers to a user's home directory, i.e. `C:\Users\<username>\`)

Linux, macOS, etc.:  
- `/etc/gallery-dl.conf`
- `${XDG_CONFIG_HOME}/gallery-dl/config.json`
- `${HOME}/.config/gallery-dl/config.json`
- `${HOME}/.gallery-dl.conf`

When run as [executable](#standalone-executable), *gallery-dl* will also look for a `gallery-dl.conf` file in the same directory as said executable.

It is possible to use more than one configuration file at a time. In this case, any values from files after the first will get merged into the already loaded settings and potentially override previous ones.

## Authentication

### Username & Password

Some extractors require you to provide valid login credentials in the form of a username & password pair. This is necessary for `nijie` and optional for `aryion`, `danbooru`, `e621`, `idolcomplex`, `imgbb`, `inkbunny`, `mangadex`, `mangoxo`, `pillowfort`, `sankaku`, `subscribestar`, `tapas`, `tsumino`, and `zerochan`.

You can set the necessary information in your [configuration file](#configuration)

``` json
{
    "extractor": {
        "subscribestar": {
            "username": "<username>",
            "password": "<password>"
        }
    }
}
```

or you can provide them directly via the `-u/--username` and `-p/--password` or via the `-o/--option` command-line options

``` bash
gallery-dl -u "<username>" -p "<password>" "URL"
gallery-dl -o "username=<username>" -o "password=<password>" "URL"
```

### Cookies

For sites where login with username & password is not possible due to CAPTCHA or similar, or has not been implemented yet, you can use the cookies from a browser login session and input them into *gallery-dl*.

This can be done via the [cookies](https://gdl-org.github.io/docs/configuration.html#extractor-cookies) option in your configuration file by specifying

- the path to a Mozilla/Netscape format cookies.txt file exported by a browser addon  
  (e.g. [Get cookies.txt LOCALLY](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc) for Chrome, [Export Cookies](https://addons.mozilla.org/en-US/firefox/addon/export-cookies-txt/) for Firefox)

- a list of name-value pairs gathered from your browser's web developer tools  
  (in [Chrome](https://developers.google.com/web/tools/chrome-devtools/storage/cookies), in [Firefox](https://developer.mozilla.org/en-US/docs/Tools/Storage_Inspector))

- the name of a browser to extract cookies from  
  (supported browsers are Chromium-based ones, Firefox, and Safari)

For example:

``` json
{
    "extractor": {
        "instagram": {
            "cookies": "$HOME/path/to/cookies.txt"
        },
        "patreon": {
            "cookies": {
                "session_id": "K1T57EKu19TR49C51CDjOJoXNQLF7VbdVOiBrC9ye0a"
            }
        },
        "twitter": {
            "cookies": ["firefox"]
        }
    }
}
```

You can also specify a cookies.txt file with the `--cookies` command-line option  
or a browser to extract cookies from with `--cookies-from-browser`:

``` bash
gallery-dl --cookies "$HOME/path/to/cookies.txt" "URL"
gallery-dl --cookies-from-browser firefox "URL"
```

### OAuth

*gallery-dl* supports user authentication via [OAuth](https://en.wikipedia.org/wiki/OAuth) for some extractors. This is necessary for `pixiv` and optional for `deviantart`, `flickr`, `reddit`, `smugmug`, `tumblr`, and `mastodon` instances.

Linking your account to *gallery-dl* grants it the ability to issue requests on your account's behalf and enables it to access resources which would otherwise be unavailable to a public user.

To do so, start by invoking it with `oauth:<sitename>` as an argument. For example:

``` bash
gallery-dl oauth:flickr
```

You will be sent to the site's authorization page and asked to grant read access to *gallery-dl*. Authorize it and you will be shown one or more "tokens", which should be added to your configuration file.

To authenticate with a `mastodon` instance, run *gallery-dl* with `oauth:mastodon:<instance>` as argument. For example:

``` bash
gallery-dl oauth:mastodon:pawoo.net
gallery-dl oauth:mastodon:https://mastodon.social/
```
