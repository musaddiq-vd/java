# Orion

**A real-time voice AI assistant for your computer — by Musaddiq Khan.**

Talk to your PC in English, Hindi, Urdu or Hinglish. Orion listens, answers out loud and gets things done: opens and closes apps and browser tabs, controls volume, brightness and media, reads your screen and documents, sends WhatsApp messages, searches the web, checks the weather, sets reminders, writes code, and remembers what you tell it about yourself.

Powered by the Gemini Live API for low-latency, natural voice conversation, with a futuristic desktop window.

---

## Features

### The window
| | |
|---|---|
| 🔵 **Reactive orb** | Animated core and waveform that move with your voice and Orion's. |
| 💬 **Conversation panel** | Everything said, plus every action Orion took (✓ / ✗). |
| ⌨️ **Type or talk** | Type in the box at any time — same session, same tools. |
| 🎙️ **Mute / 💤 Sleep** | One click to mute the mic or put Orion to sleep. |
| ⚠️ **Real confirmation** | Shutdown, restart, WiFi off, delete and sending messages show a banner — **you** press Confirm. |
| ⚙️ **Settings** | API key, names, voice, city, accent colour, microphone/speakers, wake word, features, auto-start. |
| 🧠 **Memory panel** | See every fact Orion stored about you and forget any of them. |
| 🧩 **Tools panel** | Every skill Orion has, including your plugins. |

### What Orion can do
| Area | Examples |
|---|---|
| Apps & windows | "Open Spotify" · "Close YouTube" (just the tab) · "Close Chrome" · "Switch to VS Code" · "Minimize everything" |
| Keyboard | "Press ctrl+shift+t" · "Type hello how are you and press enter" |
| System | Volume · brightness · dark mode · WiFi · lock / sleep / shutdown / restart · CPU, RAM, battery |
| Media | "Play Arijit Singh on YouTube" (plays the top result) · play/pause · next / previous |
| Vision | "What's on my screen?" · "Read this error" · "Look at the camera" (needs `opencv-python`) |
| Files & documents | List, read, write, move, create folders, delete to Recycle Bin · read PDF, Word, Excel, PowerPoint |
| Clipboard | "Translate what I copied" · "Fix the grammar of my clipboard" |
| Web | Web and news search · weather · Google Flights · Google Maps |
| Messages | WhatsApp to saved contacts (confirmed on screen) · email drafts |
| Code | "Write a Python snake game in a folder called snake" — creates the files and opens VS Code · explain/review a code file |
| Games | Open Steam / Epic downloads, library or store |
| Memory | Remembers your name, city, people, preferences, contacts · "What do you know about me?" |
| Reminders | "Remind me in 20 minutes to call mom" |
| Undo | "Undo" reverses file changes, brightness, dark mode, clipboard and saved memories |

### On its own
| | |
|---|---|
| 🌅 **Morning briefing** | First start of the day: greeting, time, weather for your city, top news, and what you talked about last time. |
| 💬 **Check-ins** | After a long quiet spell (daytime only) Orion makes one short, useful check-in. |
| 📊 **Hardware alerts** | Warns about CPU above 90% for 3 minutes, almost-full RAM, or battery below 20%. |
| 📰 **Watched topics** | "Watch news about Bitcoin" — Orion checks a few times a day and tells you about new headlines. |
| 🗓️ **Session memory** | Each conversation is summarised when you close Orion and mentioned in the next briefing. |
| 💤 **Wake word** | Offline "Hey Jarvis" (or Alexa / Hey Mycroft). While asleep no audio leaves your computer. |
| 🚀 **Auto-start** | Optionally start with Windows. |
| 🔁 **Auto-reconnect** | Dropped connections reconnect and resume the same conversation. |

---

## Quick start

Requirements: Windows 10/11 (macOS/Linux work with fewer system controls), Python 3.10+, a microphone and speakers, and a free [Gemini API key](https://aistudio.google.com/apikey).

```bash
git clone https://github.com/musaddiq-vd/orion.git
cd orion
python -m venv .venv
.venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m orion                 # opens the window; paste your API key on first start
```

Double-click `orion_launcher.pyw` to start without a console window.

Other modes:

```bash
python -m orion --cli           # voice in the terminal, no window
python -m orion --text          # typed chat in the terminal
python -m orion --setup         # terminal setup (API key, names, voice)
python -m orion --tools         # list all tools
python -m orion --devices       # list microphones / speakers
```

> **Tip:** Without headphones Orion mutes your mic while it speaks, so it doesn't hear itself. With headphones, turn on *Let me talk over Orion* in Settings → Audio.

---

## Configuration

Settings live in `~/.orion/config.json` (or the `ORION_HOME` folder), **never inside the repo**, so your API key and memories can't be pushed to GitHub by mistake. Everything is editable from the Settings window.

| Key | Meaning |
|---|---|
| `api_key` | Gemini API key (the `GEMINI_API_KEY` env var overrides it) |
| `assistant_name`, `user_name`, `city` | Names and city used in conversation and the briefing |
| `voice` | `Charon`, `Puck`, `Kore`, `Fenrir` or `Aoede` |
| `live_model`, `text_model` | Gemini models for voice and for text work |
| `theme_color` | Accent colour of the window |
| `input_device`, `output_device` | Microphone and speakers by name; empty = default |
| `allow_interrupt` | Talk over Orion (headphones) |
| `wake_word`, `sleep_after_seconds` | Wake word model and auto-sleep time |
| `morning_briefing`, `proactive`, `proactive_minutes`, `hardware_alerts` | Background features |
| `allowed_roots` | Folders the file tools may use; empty = your home folder |

Memories: `~/.orion/memory.json` · app state (watched topics, last summary): `~/.orion/state.json`.

---

## Writing a plugin

Create `plugins/hello.py`:

```python
from orion.tools import tool

@tool("say_hello", "Greet someone by name.",
      {"name": {"type": "string"}}, required=["name"])
def say_hello(ctx, name):
    return f"Hello, {name}!"
```

Restart Orion and say *"say hello to Ali"*. `ctx` gives you `settings`, `memory`, `undo`, `confirm`, `notify`, `state`, `llm` and `attach_image`. See [`plugins/_example.py`](plugins/_example.py). Plugins can also go in `~/.orion/plugins/`.

---

## Safety by design

- No `exec()` of model output and no `shell=True` anywhere.
- File tools only work inside allowed folders; deletes go to the Recycle Bin.
- Irreversible actions need a click from you — the model can't confirm them itself.
- Keyboard shortcuts are limited to a known key list; URLs must be http(s).
- Secrets and personal data stay in `~/.orion`, outside the repository.

---

## Project structure

```
orion/
├── orion/
│   ├── cli.py            # entry point (window by default)
│   ├── app.py            # wires settings, memory, tools, events and the system prompt
│   ├── live.py           # Gemini Live voice session (mic, speaker, tools, vision, reconnect)
│   ├── background.py     # briefing, check-ins, hardware alerts, watched topics, summaries
│   ├── text_chat.py      # typed chat with the same tools
│   ├── llm.py            # text model with automatic fallback
│   ├── events.py         # event bus between core and window
│   ├── audio.py · wake.py · net.py
│   ├── config.py · memory.py · state.py · undo.py · confirm.py
│   ├── tools/            # built-in tools, one file per area
│   └── ui/               # PyQt6 window, orb, settings
├── plugins/              # your own tools
├── tests/                # pytest suite
└── orion_launcher.pyw    # start without a console
```

## Development

```bash
pip install pytest
python -m pytest
```

---

## Copyright

© 2026 Musaddiq Khan. All rights reserved.
