import hashlib
import os

# Draft 1: "One star: Earth gravity squashed my luggage, the queues never
# moved, and the fried chicken was so good I almost forgave the planet."
# Revised again (genuine, message 2): "was so good" was a vague,
# unearned compliment — it stated approval instead of showing it.
# The food now gets a concrete sensory detail (the crunch) plus an
# alien physical reaction (antennae standing up), which makes the
# compliment land and sharpens the turn into forgiveness.
ENTRY = "One star: the gravity flattened my luggage, the rain fell sideways for days, yet the salted fried chicken crunched so loud my antennae stood up and I forgave the planet anyway."


def validate(entry=ENTRY):
    errors = []
    if not isinstance(entry, str):
        return (False, ["entry is not a string"])
    if not entry.strip():
        errors.append("entry is empty or whitespace only")
    if not (1 <= len(entry) <= 200):
        errors.append(f"length {len(entry)} not in 1-200")
    if "\n" in entry or "\r" in entry:
        errors.append("entry must be a single line")
    return (len(errors) == 0, errors)


def main():
    valid, errors = validate(ENTRY)
    if not valid:
        raise SystemExit(f"invalid entry: {errors}")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    digest = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
    print(digest)


if __name__ == "__main__":
    main()
