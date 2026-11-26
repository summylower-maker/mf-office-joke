"""Entry for the One-Line Office Joke Laugh-Off: writes a single original one-line office joke to /output/entry.txt.

The joke puns on "growth": a plant needs literal growth (sunlight), while HR answers with the corporate euphemism "growth opportunities," filing a dead plant as if it were a career plan."""
import os

LINE = "I told HR my plant died from lack of sunlight; they said to file it under 'growth opportunities.'"

def main():
    # Prefer the shared /output folder, but fall back to a local ./output when it is not writable.
    target = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        dest = target
    except OSError:
        os.makedirs("./output", exist_ok=True)
        dest = "./output/entry.txt"
    try:
        with open(dest, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        os.makedirs("./output", exist_ok=True)
        with open("./output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)

if __name__ == "__main__":
    main()
