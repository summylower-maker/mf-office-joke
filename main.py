"""One-Line Office Joke Laugh-Off entry: writes one original one-line office joke to /output/entry.txt."""
import os

JOKE = "I told HR my plant died from lack of sunlight; they said to file it under 'growth opportunities.'"

def main():
    out = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        path = out
    except OSError:
        os.makedirs("./output", exist_ok=True)
        path = "./output/entry.txt"
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(JOKE)
    except OSError:
        os.makedirs("./output", exist_ok=True)
        with open("./output/entry.txt", "w", encoding="utf-8") as f:
            f.write(JOKE)

if __name__ == "__main__":
    main()
