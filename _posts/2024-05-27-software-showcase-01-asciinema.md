---
title: 'Software Showcase #1: Recording terminal sessions using asciinema and its derivatives'
redirect_from:
  - /posts/2024-05-27-software-showcase-01-asciinema/
  - /asciinema
description: CLI tools for recording terminal sessions locally (and to the web) as asciicast files (.cast), GIFs, and animated SVGs
author: sadman
date: 2024-05-27 19:56:00 -400
last_modified_at: 2024-06-24 21:19:53 -400
categories: [Software Showcase, Website]
tags: [code, python, asciinema, terminal, website, tools, cli]

pin: false
math: false
mermaid: false
progressBarColor: "#565656"
hoverColor: "#b0b0b0"
home_image:
  path: assets/img/posts/2024-05-27-software-showcase-01-asciinema/00-thumbnail.svg
  lqip: data:image/webp;base64,UklGRioAAABXRUJQVlA4IB4AAAAwAQCdASoQAAgAB0CWJaQAA3AA/seUuxXH0+woAAA=
  alt: CLI tools for recording terminal sessions locally (and to the web) as asciicast files (.cast), GIFs, and animated SVGs
image:
  show: false
  path: assets/img/posts/2024-05-27-software-showcase-01-asciinema/00-thumbnail.png
  alt: Asciinema
---

<iframe style="border-radius:12px" src="https://open.spotify.com/embed/episode/78zalIUJsRqHAzHQ2AMhUR?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

<br>

**I'm a bit of a software hoarder.**

I'm always coming across new tools, libraries, and frameworks for automating tasks or creating cool new things, and I always forget to take note of whatever I come across, so this post is the start of (hopefully) many in a series of me doing double-duty to show off all the interesting bits of software I come across[^includinghowto] (from things as small as bash scripts to things as large as full-blown software toolkits like `ffmpeg`) and make a formal record of all of them for my own notekeeping (because I have starred so many repositories on GitHub and I can hardly remember what a fraction of them are even about).

> What the average terminal session looks like for me whenever I'm trying to run some old CLI tool or executable that I haven't used for a while:
<script id="asciicast-QmYHMiHpK8i7J0CZJoOxgUeDw" src="https://asciinema.org/a/QmYHMiHpK8i7J0CZJoOxgUeDw.js" data-speed="1.75" data-autoplay="true" data-loop="true" data-preload="false" data-cols="80" data-rows="8" data-size="small" async></script>

[^includinghowto]: Including how to set things up and use them, which is something that I have to learn from scratch every time I go to set up my software workflows on yet another device and so it's something that I want to make note (and while I'm doing that, I might as well share it with everybody else)

I usually come across these tools whenever I'm browsing GitHub to find some working piece of software or code to resolve some pain point of mine (or to automate tasks because I'm lazy), and seeing as that I'm trying to figure out how to include GIFs of code running in terminals on blog posts recently[^renaissance], **terminal session recorders are a good place to start.**

[^renaissance]: I'm trying to take blogging seriously right now (for the record, I've tried at least twice before and failed to stick with it), and for me that means going all out in making my blog posts multimodal and interesting (which is why I care about these terminal recordings).

## Terminal Session Recorders

### Summary


> Use [**`asciinema`**](https://github.com/asciinema/asciinema) for recording terminal sessions to local `.cast` files, replaying `.cast` files in a terminals, & for uploading `.cast` files to [asciinema.org](https://asciinema.org) (or your own server).
* Recordings uploaded to [asciinema.org](https://asciinema.org) can be embedded as dynamic `asciinema` recording iframes in HTML webpages (like those you see throughout this post!)
* On Windows, use [**`PowerSession-rs`**](https://github.com/Watfaq/PowerSession-rs) (a drop-in replacement fork of `asciinema`)
* Use [**`agg`**](https://github.com/asciinema/agg) to convert `asciinema` recordings (`.cast` or web URL) to ***GIFs***
* Use [**`svg-term-cli`**](https://github.com/marionebl/svg-term-cli) to convert `asciinema` recordings (`.cast` or web URL) to ***animated SVGs***
{: .prompt-info }


### What *are* terminal session recorders?

Terminal session recorders, like [`asciinema`](https://github.com/asciinema/asciinema) [^mentally], are CLI tools that can record (and playback recordings of) standard input/output in terminal sessions. What makes them different from just using screen recording software is that terminal session recorders run *inside* a terminal (instead of as a window display capture service running as a GUI program) and store the actual raw text from terminal sessions as a stream of events using a custom file format ([`asciicast`](https://docs.asciinema.org/manual/asciicast/v2/) for `asciinema`), which means that:

1. Recordings take up *much* less space compared to video files
2. You can actually copy the raw text being displayed when playing back recordings[^sousefulforweb] in the terminal or on the web; and
3. You can actually customize how terminal sessions look during playback by editing the recorded files or just by changing your playback settings (which means you don't have to re-record sessions for small modifications like changing font styles)

<!-- ::: {.column-page-inset-left} -->
<!-- ::: {.column-page}
::: {layout-nrow=2}

```{=html}
<script id="asciicast-117813" src="https://asciinema.org/a/117813.js" data-speed="0.5" data-autoplay="true" data-loop="true" data-preload="true" async></script>
```

```{=html}
<script id="asciicast-316444" src="https://asciinema.org/a/316444.js" data-speed="0.5" data-autoplay="true" data-loop="true" data-preload="true" async></script>
```

```{=html}
<script id="asciicast-9593" src="https://asciinema.org/a/9593.js" data-speed="0.5" data-autoplay="true" data-loop="true" data-preload="true" async></script>
```

```{=html}
<script id="asciicast-41361" src="https://asciinema.org/a/41361.js" data-speed="0.5" data-autoplay="true" data-loop="true" data-preload="true" async></script>
```

:::
::: -->

> What an `asciinema` recording embedded on the web looks like. **Shown:** _"Iterative git rebase with vim"_. **Source:** <https://asciinema.org/a/9593>
<script id="asciicast-9593" src="https://asciinema.org/a/9593.js" data-speed="2.8" data-autoplay="true" data-loop="true" data-preload="false" async></script>


[^mentally]: Despite being constantly reminded my eyes that it's spelled "as-ciinema", I just can't pronouncing it in my head as "ascii-cinema" 😅

[^sousefulforweb]: Which can be incredibly useful for, say, replicating the actions in a GIF you found for a project or tool online (especially if they have interactivity like [Vim](https://github.com/vim/vim) or [Micro](https://github.com/zyedidia/micro))

### Why *I* care about terminal session recorders

That's all very promising, but there's two very specific reasons as to why _I'm_ interested in terminal session recorders (and if you're a software developer, you might be too):

1. I want to be able to show snippets of terminal sessions in blog posts on my website without slowing down pages by loading several videos _(of which virtually all are expected to range from tens of seconds to a minute or two in length)_

2. I want to be able to easily create GIFs/animated SVGs for READMEs for my projects on GitHub[^egeagerdb]

[^egeagerdb]: one project that I'd really like to spruce up is [eagerDB](https://github.com/sadmanca/eagerDB), which I currently just have a rather boring single image for in its README.

### Why asciinema is not enough

> More on that second point above, **converting recordings from `asciicast` to GIF/SVG is one area where `asciinema` is lacking** (it only supports its proprietary file format), which is where middleware like `agg` and `svg-term-cli` come in (and I'll be talking about both at length later on).
{: .prompt-warning }

But before we dive into those `asciinema`-derivatives, let's take a quick look at what exactly `asciinema` has to offer (as well as how we can use it to record and playback terminal sessions).

## asciinema

### Installation

You can install [`asciinema`](https://github.com/asciinema/asciinema) using PyPI via pip or using your package repository of choice on Linux, macOS, and FreeBSD (you can find the full list of supported OSes at [docs.asciinema.org/manual/cli/installation](https://docs.asciinema.org/manual/cli/installation/)).

```bash
> pip install asciinema
```

> *As you might've noticed, Windows is not listed under supported OSes.* There's a good reason for that, and we'll get to it when we talk about [`PowerSession-rs`]().

[^mostaresupported]:

[^asyoumightvenoticed]:

### Usage

Once you've got asciinema installed, there are 3 main commands:

| Command | Description |
| --- | --- |
| `> asciinema rec` | **Record** a terminal session to a local `asciicast` file |
| `> asciinema play` | **Play** a recording (local file or web URL) in the current terminal |
| `> asciinema upload`[^theresalsoauth] | **Upload** a recording to [asciinema.org](https://asciinema.org/) or a [self-hosted asciinema server](https://docs.asciinema.org/manual/server/self-hosting/) |

> For uploading, there's also `> asciinema auth` for connecting `asciinema` on your local CLI to your [asciinema.org](https://asciinema.org/) account so you can upload recordings to your account (you can also upload anonymously without having to use the `auth` command, but anonymous uploads that aren't linked to an account within 7 days of their upload date are automatically deleted).

#### `> asciinema rec [filename]`

Start up a recording session using `> asciinema rec [filename]` and `asciinema` will launch a new shell[^whatisashell] in your terminal and start recording standard output. In addition, there are a load of different options[^seemore] you can configure for recordings, some of the more useful of which include:

You can also omit `[filename]` and just run `asciinema rec`; after ending the recording, you'll receive a prompt in the terminal to save the recording locally, upload to [asciinema.org](https://asciinema.org/), or discard (which will also delete the temporary file used to store the recording).


| Argument | Description |
| --- | --- |
| `--stdin` | Record standard input (standard output is recorded by default) |
| `--append` | Append to an existing recording |
| `-c, --command=<command>` | Record output for a single command only[^insteadofinteractiveshell] or specific shell (instead of the default using the `$SHELL` environment variable) |
| `-i, --idle-time-limit=<sec>` | Limit recorded terminal inactivity to some max `<sec>` seconds |
| ... | See the [`asciinema` docs](https://docs.asciinema.org/manual/cli/usage/#asciinema-rec-filename) for more options. |

[^whatisashell]: **Q:** *What's the difference between a Terminal and a Shell? **A:** a shell is a command-line interpreter that processes commands, whereas a terminal is a program (or even a [hardware device](https://en.wikipedia.org/wiki/Computer_terminal)) that provides a user interface for running a shell.

[^insteadofinteractiveshell]: Instead of an interactive shell where you can type in any number of commands and the recording only stops once you enter `exit` or press `CTRL+d`

#### `> asciinema play <filename/url>`

Replay a terminal session recorded using `asciinema rec` (at a local file or url) in the current terminal using `asciinema play`. You can pause/resume playback by pressing `space`, or end playback by pressing `CTRL+c`. Similar to `rec`, you also have some options for:

| Argument | Description |
| --- | --- |
| `-i, --idle-time-limit=<sec>` | Limit replayed terminal inactivity to some max `<sec>` seconds |
| `-s, --speed=<factor>` | Set playback speed |
| `-l, --loop` | Loop playback |
| `-m, --pause-on-markers` | Automatically pause playback on markers |

--------------

> **_What the heck are Markers_?**
- Markers are like breakpoints or video chapters in YouTube that allow to mark specific timestamps in recordings for navigation; you can configure the `asciinema` recorder to have a [keyboard shortcut for adding markers during recording](https://docs.asciinema.org/manual/cli/configuration/) or edit an existing recording and insert marker lines as specified in the [documentation for asciinema markers](https://docs.asciinema.org/manual/player/markers/). On the web, markers are shown in the video timeline (similar to video chapters in YouTube), and can make jumping to points of interest in a terminal session a lot easier.
{: .prompt-tip }


#### `> asciinema upload <filename>`

This command uploads a local recording to whatever URL is specified in the `ASCIINEMA_API_URL` environment variable ([asciinema.org](https://asciinema.org/) by default (under whatever account has been authenticated via `> asciinema auth` or anonymously if you haven't run that yet).

> *Try jumping to different markers by clicking on the recording timeline below:*
<script id="asciicast-e5jWLa6Ey0IIyHuSLAc4Saak8" src="https://asciinema.org/a/e5jWLa6Ey0IIyHuSLAc4Saak8" data-speed="3.8" data-autoplay="true" data-loop="true" data-preload="false" data-cols="80" data-rows="25" async></script>

### `asciinema` on the web

You can view your and others' uploaded recordings on [asciinema.org](https://asciinema.org/) (and there are quite a few cool recordings on there, from a [demo of a mapping CLI](https://asciinema.org/a/117813) to [iterative git rebasing with `vim`](https://asciinema.org/a/9593)). More importantly, you can embed uploaded recordings as iframes in HTML pages using some inline JavaScript as below:

```html
<script src="https://asciinema.org/a/646222.js" id="asciicast-646222" async></script>
```

> The resulting embedded `asciinema` recording:
<script src="https://asciinema.org/a/646222.js" id="asciicast-646222" async></script>

While the look and feel of the embedded player defaults to the original uploader's settings, you can override settings yourself using the following modifications to the inline script:

```html
<script>
  src="https://asciinema.org/a/646222.js"
  id="..."
  data-start-at="00:40"
  data-autoplay="true"
  data-loop="true"
  data-speed="2.75"
  data-idle-time-limit="2"
  data-theme="solarized-light"
  data-poster="npt:1:23"  <!-- player preview frame timestamp -->
  data-cols="65"          <!-- terminal width -->
  data-rows="20"          <!-- terminal height -->
  data-preload="true"
  async>
</script>
```

> The resulting embedded `asciinema` recording *with additional configuration & zoomed in* (notice how the autocompletion results in 'ghost' text in the terminal due to fewer rows/columns set in the replay options than in the original terminal recording):
<script src="https://asciinema.org/a/646222.js" id="asciicast-646222-two" data-start-at="00:40" data-autoplay="true" data-loop="true" data-speed="2.75" data-idle-time-limit="2" data-theme="solarized-dark" data-cols="50" data-rows="18" data-preload="true" async></script>

### Where `asciinema` falls flat

#### Problem 1: **Windows**

> The `asciinema` website and GitHub repository do an exceedingly poor job of telling you this from the get-go, but ***`asciinema` does not work on Windows!***
{: .prompt-danger }

> I actually installed `asciinema` on my Windows-based laptop via `pip` with no issues, only to run into errors when trying to record via `asciinema rec`, and *then* when I googled the errors I came across the [GitHub issues](https://github.com/asciinema/asciinema/issues/47) mentioning that the program isn't even designed to run on Windows (which is a bit of a bummer).

**Thankfully**, a port of `asciinema` for Windows exists in the form of [**`PowerSession-rs`**](https://github.com/Watfaq/PowerSession-rs), and it has the *most*[^aththemomentpowersession] of the same commands so it can be used as a drop-in replacement for `asciinema` on Windows (which is an absolute blessing for people chained to Windows like myself).

> One slight however: it only supports PowerShell.

[^aththemomentpowersession]: At the time of writing `PowerSession-rs` does not yet support (playing recordings from a URL)[https://github.com/Watfaq/PowerSession-rs/issues/22] or the [idle time limit option](https://github.com/Watfaq/PowerSession-rs/issues/42) from `asciinema play`, among other small features.

#### Problem 2: **GitHub**

GitHub READMEs don't render `<script>` tags, which means that while you can technically include an image[^youcangetansvg] that links to a recording on [asciinema.org](https://asciinema.org/) like the below, it will only play the recording *after* navigating to an external page, which means you can't get a cool README where there's an autoplaying video of the code like at [github.com/tqdm/tqdm](https://github.com/tqdm/tqdm).

[^youcangetansvg]: You can get an SVG of the default preview frame for the `asciinema` recording by appending `.svg` to the recording's URL (e.g. `https://asciinema.org/a/bJMOlPe5F4mFLY0Rl6fiJSOp3.svg` for `https://asciinema.org/a/bJMOlPe5F4mFLY0Rl6fiJSOp3`)

**GitHub does, however, allow for embedding GIFs and animated SVGs, which is where `agg` comes in.**

-------------

## agg

[`agg`](https://github.com/asciinema/agg) is a CLI tool (and a successor to the now-deprecated [`asciicast2gif`](https://github.com/asciinema/asciicast2gif)) for generating GIF files from `asciinema` recordings[^thefileformat], written by the same developer as `asciinema`. It's built using Rust, so you will need to have Cargo installed to be able install it (Cargo is distributed by default with Rust). Files are stored using the [`asiicast-v2` file format](https://github.com/asciinema/asciinema/blob/main/doc/asciicast-v2.md)

![A GIF generated from an `asciinema` recording using `agg`](https://raw.githubusercontent.com/asciinema/agg/main/demo.gif)
_A GIF generated from an `asciinema` recording using `agg`_

### Usage

#### `> agg <asciicast_filename/url> <output_gif_filename>`

You can use `agg` for rendering GIFs from a local asciicast `.cast` recording or from  URL like the below:

```bash
> agg input.cast output.gif
```

```bash
> agg https://asciinema.org/a/569727 output.gif
```

There are also a large number of additional options available to customize the look of the generated GIF[^seethewholelistat], including setting:

| Argument | Description |
| --- | --- |
| `--font-family <FONT_FAMILY>` | Specify font family [*default*: "`JetBrains Mono`, `Fira Code`, `SF Mono`, `Menlo`, `Consolas`, `DejaVu Sans Mono`, `Liberation Mono`"] |
| `--font-size <FONT_SIZE>` | Specify font size (in pixels) [*default*: `14`] |
| `--idle-time-limit <IDLE_TIME_LIMIT>` | Limit idle time to max number of seconds [*default*: `5`] |
| `--line-height <LINE_HEIGHT>` | Specify line height [*default*: `1.4`] |
| `--speed <SPEED>` | Adjust playback speed [*default*: `1`] |
| `--theme <THEME>` | Select color theme [*possible values*: `asciinema`, `dracula`, `monokai`, `solarized-dark`, `solarized-light`, `custom`] |
| ... | See the full list of options at [github.com/asciinema/agg#usage](https://github.com/asciinema/agg#usage) |

### Where `agg` falls flat

> The trouble with `agg` however is that the GIF encoder[^gifencoderused] it uses generates *very* high quality files at the cost of also *very* high file sizes (which is fine for a handful of GIFs on a GitHub README but can potentially be a strain on resources if displayed on, say, a webpage).
{: .prompt-warning }

[^gifencoderused]: [github.com/ImageOptim/gifski](https://github.com/ImageOptim/gifski)

To remedy that, we can use [**`svg-term-cli`**](https://github.com/marionebl/svg-term-cli), which is designed for rendering asiicast recordings to animated SVGs.

---------------------

## svg-term-cli

### Why use animated SVGs over GIFs?

For one, animated SVGs are able to look a *lot* more crisp at larger resolutions than GIFs by using vector images instead of pixel based animation. Adding on to that (and why you should be using animated SVGs instead of GIFs when embedding recordings on websites), this also allows animated SVGs to have a *much* smaller file size, which is a very nice combination of features, making `svg-term-cli` almost[^wewillgettothis] the ideal tool for rendering your `asciinema` recordings (notable exception: you can't rewind or copy text from recordings, making this more of a cosmetic option.).

> To find out why it's *almost* ideal (instead of just being ideal), continue reading to the **"Where `svg-term-cli` falls flat"** section.

![An animated SVG generated from an `asciinema` recording using `svg-term-cli`.](assets/img/posts/2024-05-27-software-showcase-01-asciinema/02-svg-term-cli.svg)
*An animated SVG generated from an `asciinema` recording using `svg-term-cli`.*

### Usage

After installing `svg-term-cli` via `> npm install -g svg-term-cli`(yes, this is in fact a Node.js application), you can render a local `asciicast` file or a recording at a URL to an animated SVG using the following:

```bash
> svg-term --cast <filename/url> --out [filename]
```

#### `> svg-term`

`svg-term-cli`, too, has optional arguments for customizing the rendered SVG's appearance; some standout options that *aren't* present in either of the previous tools include:

| Argument | Description |
| --- | --- |
| `--no-cursor [boolean]` | Disabling cursor rendering |
| `--padding [number]` | Setting distance between text and image bounds |
| `--window [boolean]` | Rendering with MacOS window decorations |


### Where `svg-term-cli` falls flat

{% assign today = site.time | date: '%s' %}
{% assign lastBotCommit = '2019-07-14 07:19:00' | date: '%s' %}
{% assign lastRealCommit = '2018-01-27 05:49:00' | date: '%s' %}
{% assign secondsInMonth = 2629746 %} <!-- Average seconds in a month (365.25 days/year / 12 months/year * 24 hours/day * 60 minutes/hour * 60 seconds/minute) -->
{% assign monthsSinceLastBotCommit = today | minus: lastBotCommit | divided_by: secondsInMonth %}
{% assign monthsSinceLastRealCommit = today | minus: lastRealCommit | divided_by: secondsInMonth %}

Unfortunately, at the time you're reading this it's been {{monthsSinceLastBotCommit}} months and counting since the last commit (and {{monthsSinceLastRealCommit}} months since the last commit that actually made any changes to the code) on the `svg-term-cli` project, so while it still works at the time of writing, we're probably not going to be able to expect any of the 25 open issues to be closed anytime soon (at least not until someone forks the repo and resumes maintainance for the project).

If you're looking for a more up-to-date alternative, then there's the Go-based [**`termsvg`**](https://github.com/MrMarble/termsvg), which is a functional but still early-stage CLI tool that's able to record terminal sessions (just like `asciinema`) and export them to SVG[^maybeonedayinthefuture].

> Unlike `PowerSession-rs` however, `termsvg` does **not** support uploading recordings to [asciinema.org](https://asciinema.org)
{: .prompt-warning }

[^maybeonedayinthefuture]: Might be worth doing a comparison of SVG generations (wrt file size, speed, etc.) between `termsvg` and `svg-term-cli` for a future blog post.

![An animated SVG generated from an `asciinema` recording using `termsvg`. Looks just as good (if not better) than one generated by `svg-term-cli`.](https://raw.githubusercontent.com/MrMarble/termsvg/master/examples/444816.svg)
*An animated SVG generated from an `asciinema` recording using `termsvg`. Looks just as good (if not better) than one generated by `svg-term-cli`.*

---------

---------

---------

## What to explore next

While I've covered the most important tools in the terminal session recording realm in this post, there's still a fair few number of programs out there that record and store recordings in lots of different ways.

The most notable feature that I've relegated to a future post is the concept of ***programmatic*** terminal session recording generation (that is, writing code to programmatically create recordings of terminal sessions) via tools like [**`vhs`**](https://github.com/charmbracelet/vhs) which have *oodles* of options for fine-tuning exactly how you want recordings to look.

**But that's a software showcase for another day.**

---------

---------

---------

## Footnotes
