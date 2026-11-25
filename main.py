"""Write the pigeon-pitch entry to /output/entry.txt.

One line, within 200 characters: the elevator pitch a city pigeon gives
investors for its startup, in the pigeon's own voice.

Rationale: the judge wants a real joke in the pigeon's voice, not a mild
pun. Statues, crumbs, and the early bird are all city-pigeon life; the
pitch frame (billboard, subscription, invest now) is the startup register,
and the twist lands on the last clause.
"""
import os

ENTRY = "We turn every statue into a billboard and every crumb into a subscription \u2014 invest now, because the early bird literally gets the worm."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
