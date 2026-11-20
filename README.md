# telegram — Flutter Tasbih Counter & Telegram Bot Starter

> Early learning project containing two small, independent experiments: a Flutter **digital tasbih (dhikr) counter** and a minimal **Python Telegram bot**.

![Status](https://img.shields.io/badge/status-experimental-orange) ![Flutter](https://img.shields.io/badge/Flutter-Dart-02569B?logo=flutter) ![Python](https://img.shields.io/badge/Python-python--telegram--bot-3776AB?logo=python)

---

## What's inside

### 1. Flutter tasbih counter — `main.dart`

A single-screen Flutter app titled **"المسبحه الالكترونية"** (Electronic Tasbih):

- Three buttons — *سبحان الله*, *الحمد لله*, *الله أكبر* — that update the displayed phrase and a counter.
- Material design, Arabic UI.
- Dart SDK `^3.9.2`; dependencies: `cupertino_icons`; dev: `flutter_lints`.

### 2. Telegram bot — `main.py`

A minimal bot built with `python-telegram-bot` 20.3 that replies to `/start`.

## Project structure

```text
.
├── main.dart            # Flutter app (single file)
├── pubspec.yaml         # Flutter package config (package name: sbha)
├── pubspec.lock
├── analysis_options.yaml
├── main.py              # Telegram bot
├── requirements.txt     # python-telegram-bot==20.3
└── ._*                  # macOS metadata files (not source code)
```

## Running

### Flutter app

The repository contains only the Dart entry file, not the full platform folders (`lib/`, `android/`, `ios/`, …). To run it:

```bash
flutter create sbha
# copy main.dart to sbha/lib/main.dart and pubspec.yaml to sbha/
cd sbha && flutter run
```

### Telegram bot

```bash
pip install -r requirements.txt
# set the TELEGRAM_BOT_TOKEN environment variable, then:
python main.py
```

> ⚠️ **Known issues (not yet fixed on `main`):**
> - `main.py` passes a literal value to `os.getenv(...)` instead of a variable name, and the entry guard is written as `if name == "main":` instead of `if __name__ == "__main__":`, so the script does not start as-is.
> - A credential was committed in an earlier version of `main.py`. It must be revoked in BotFather; see the open security pull request.

## Status

🧪 **Experimental / learning project** — not maintained for production use.

## License

No license has been chosen yet.
