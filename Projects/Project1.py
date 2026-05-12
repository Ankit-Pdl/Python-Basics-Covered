import time
import sys
import random

# ── ANSI color codes ──────────────────────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
BLINK  = "\033[5m"

COLORS = {
    "red":     "\033[31m",
    "green":   "\033[32m",
    "yellow":  "\033[33m",
    "blue":    "\033[34m",
    "magenta": "\033[35m",
    "cyan":    "\033[36m",
    "white":   "\033[37m",
}

BG_COLORS = {
    "red":     "\033[41m",
    "green":   "\033[42m",
    "yellow":  "\033[43m",
    "blue":    "\033[44m",
    "magenta": "\033[45m",
    "cyan":    "\033[46m",
    "white":   "\033[47m",
}

COLOR_NAMES = list(COLORS.keys())


# ── Effects ───────────────────────────────────────────────────────

def colored(text, color, bold=False, bg=None):
    """Return text wrapped in color codes."""
    code = COLORS.get(color, "")
    bg_code = BG_COLORS.get(bg, "") if bg else ""
    bold_code = BOLD if bold else ""
    return f"{bold_code}{bg_code}{code}{text}{RESET}"


def rainbow(text):
    """Each character gets a different color."""
    result = ""
    for i, ch in enumerate(text):
        color = COLOR_NAMES[i % len(COLOR_NAMES)]
        result += colored(ch, color, bold=True)
    return result


def typewriter(text, color="white", delay=0.05):
    """Print text one character at a time."""
    for ch in text:
        sys.stdout.write(colored(ch, color, bold=True))
        sys.stdout.flush()
        time.sleep(delay)
    print()


def blink_text(text, color="yellow", times=4, delay=0.4):
    """Blink text on/off in the terminal."""
    for _ in range(times):
        sys.stdout.write("\r" + colored(text, color, bold=True))
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write("\r" + " " * len(text))
        sys.stdout.flush()
        time.sleep(delay)
    print(colored(text, color, bold=True))


def gradient_line(text):
    """Simulate a gradient left→right across the color spectrum."""
    spectrum = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    result = ""
    for i, ch in enumerate(text):
        color = spectrum[i % len(spectrum)]
        result += colored(ch, color, bold=True)
    print(result)


def highlight_words(sentence, highlights):
    """
    highlights: dict of {word: color}
    Prints the sentence with specific words highlighted.
    """
    words = sentence.split()
    result = []
    for word in words:
        clean = word.strip(".,!?")
        if clean.lower() in highlights:
            result.append(colored(word, highlights[clean.lower()], bold=True))
        else:
            result.append(colored(word, "white"))
    print(" ".join(result))


def random_colors(text):
    """Every character gets a random color."""
    result = ""
    for ch in text:
        if ch != " ":
            result += colored(ch, random.choice(COLOR_NAMES), bold=True)
        else:
            result += " "
    print(result)


def banner(text, color="cyan", bg=None):
    """Print text inside a decorative box."""
    border = "═" * (len(text) + 4)
    print(colored(f"╔{border}╗", color, bold=True))
    print(colored(f"║  {text}  ║", color, bold=True))
    print(colored(f"╚{border}╝", color, bold=True))


# ── Demo ──────────────────────────────────────────────────────────

def main():
    print()
    banner("Colorful Text Effects in Python", color="cyan")
    print()

    print(colored("── 1. Solid Colors ──", "magenta", bold=True))
    for name in COLOR_NAMES:
        print(colored(f"  Hello in {name}!", name))
    print()

    print(colored("── 2. Rainbow Text ──", "magenta", bold=True))
    print("  " + rainbow("The quick brown fox jumps over the lazy dog"))
    print()

    print(colored("── 3. Gradient Line ──", "magenta", bold=True))
    print("  ", end="")
    gradient_line("Python makes even plain text look amazing!")
    print()

    print(colored("── 4. Typewriter Effect ──", "magenta", bold=True))
    print("  ", end="")
    typewriter("Loading your colorful world...", color="green", delay=0.04)
    print()

    print(colored("── 5. Blinking Text ──", "magenta", bold=True))
    print("  ", end="")
    blink_text("⚡ Important Notice! ⚡", color="yellow", times=3)
    print()

    print(colored("── 6. Highlighted Words ──", "magenta", bold=True))
    print("  ", end="")
    highlight_words(
        "Python is fast, fun, and powerful!",
        {"python": "cyan", "fast": "green", "fun": "yellow", "powerful": "red"}
    )
    print()

    print(colored("── 7. Random Colors ──", "magenta", bold=True))
    print("  ", end="")
    random_colors("Every run looks different!")
    print()

    banner("Thanks for watching! 🎨", color="green")
    print()


if __name__ == "__main__":
    main()