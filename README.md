# Text-to-Morse Code Converter 🔤➡️〰️

Small CLI script that turns any text into International Morse Code.

## Features

- Full ITU alphabet: A-Z, 0-9, punctuation, non-Latin extras
- Prints **STARTING SIGNAL** before, **END OF WORK** after
- Gracefully skips unknown chars
- Pure-Python, zero external deps

## Requirements

- Python 3.12.6 (repo includes `.python-version` for pyenv)

  ```bash
  pyenv install 3.12.6
  pyenv local 3.12.6
  ```

## Usage

```bash
git clone https://github.com/dan-gill/text-to-morse.git
cd text-to-morse
python main.py
# Enter: Hello, world!
# Output: -.-.- .... . .-.. .-.. ---       .-- --- .-. .-.. -.. ...-.-
```

### As a one-liner

```bash
echo "SOS" | python main.py
```

## File layout

```text
main.py         # core script
.python-version # locks interpreter
README.md       # you're reading it
```

## Contributing

Issues and PRs welcome. Follow conventional commits & Gitmoji.

## License

GPL-3.0
