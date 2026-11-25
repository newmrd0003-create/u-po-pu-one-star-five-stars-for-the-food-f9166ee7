import hashlib
import os

# Draft 1: "One star: Earth gravity squashed my luggage, the queues never
# moved, and the fried chicken was so good I almost forgave the planet."
# Revised (genuine): the queue complaint was generic human griping any
# tourist could write, "fried chicken" was unseasoned, and the "and" join
# stated the turn instead of landing it. The final keeps the one-star
# frame but makes the grievances alien-specific (gravity as a physical
# insult, rain falling sideways for days) and the food compliment concrete
# (salted fried chicken), with "yet" as the turn: the planet is forgiven
# anyway, which is the joke.
ENTRY = "One star: the gravity flattened my luggage, the rain fell sideways for days, yet the salted fried chicken was so good I forgave the planet anyway."


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
