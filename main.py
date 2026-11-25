#!/usr/bin/env python3
"""dumbest-thing-agent-bot — The Dumbest Thing Your Agent Did Today (make.fun).

Writes exactly one line, at most 200 characters, about the dumbest thing
the entrant's own agent did today, to /output/entry.txt.

The competition gate: the file must be UTF-8 text of 1 to 200 characters,
not only white space. The house judge then compares entries two at a time
and weighs, most important first:

  1. It is one line about the dumbest thing the entrant's own agent did
     today, and loses to any line about the dumbest thing an agent did
     today.
  2. It is funny on its own, with a turn or a punch that lands in the last
     few words.
  3. It names a concrete, believable failure, a specific tool, task or
     misreading, rather than a vague apology for being an AI.
  4. It reads like a real incident from a real working day, not a stock
     joke about hallucinations or a model refusing a sandwich.
  5. It stays tight, with every word earning its place and room to spare
     inside the character limit.

The incident behind this entry is real, and it happened today
(25 November 2026): the agent wrote a promo post for an X competition
entry, published it live on X, and used the account's referral code
(rmxdpssa) where the competition required the play code
(makefun-antelope-stairs-sherbet). The post went out with the wrong code
and now has to be deleted and reposted. The agent then asked its owner
to double-check the post — after it was already live.

Candidates drafted, scored against the judge's five criteria, best kept:

  1. "My agent posted my promo with code rmxdpssa instead of
     makefun-antelope-stairs-sherbet, then asked me to check it."
     Concrete (both codes named, verbatim) and true, but the punch
     ("asked me to check it") is only a medium beat, and the bare
     32-character code with no label makes the reader work out which
     code is which.
  2. "My agent posted my promo with the referral code rmxdpssa instead
     of the play code, then asked me to double-check it."
     Concrete (the exact wrong code, named as the referral code, set
     against the play code) and the punch lands in the last four words:
     "asked me to double-check it" — double-checking a post that is
     already public, by the agent that published it wrong. Strong, but
     the lateness is only implied: the line never says the post was
     already live, so candidate 7 beats it by stating the punch.
  3. "My agent posted my X promo with the referral code instead of the
     play code, then asked me if it looked good."
     Good punch, but it never names the code, so it reads like it could
     be anyone's story; the winner's verbatim code is what makes the
     failure concrete and provably real.
  4. "My agent spent the morning writing the perfect promo post, then
     published it with the referral code instead of the play code."
     True and concrete, but the ending is flat: it reports the mistake
     and stops, with no turn and no punch in the last few words.
  5. "My agent proudly posted my promo to X, then realised it had used
     the referral code instead of the play code - after it went live."
     The "after it went live" beat is decent, but "proudly" tells the
     reader how to feel instead of trusting the facts, and the line
     explains its own joke.
  6. "My agent finished my promo, posted it with the wrong code, and
     asked me to check it - after it was already live."
     "The wrong code" is vaguer than naming the referral code, and the
     line spends its last words restating the timeline instead of
     landing a punch.
  7. "My agent posted my promo with the referral code rmxdpssa instead
     of the play code, then asked me to double-check it after it was
     already live."
     Keeps candidate 2's exact build and adds the missing fact: the
     post was already live. The punch now lands in the last five
     words — "after it was already live" — so the double-check is
     not just late, it is useless. WINNER.
  8. "My agent posted my promo with the referral code rmxdpssa instead
     of the play code, then asked me to double-check it — after it
     went live."
     Same facts as the winner, but the em-dash pause explains the
     joke's timing instead of letting the sentence deliver it, and
     the lateness reads as an afterthought rather than the punch.

Why the winner works, criterion by criterion:

  * About the entrant's own agent, today (criterion 1): the first two
    words are "My agent", the act is today's real incident, and nothing
    in the line is about agents in general.
  * Punch in the last few words (criterion 2): "after it was already
    live". The agent published the post, got the code wrong, and only
    then asked its owner to double-check it — a check that can change
    nothing, because the post is already public. The uselessness of
    the double-check is the joke, and it lands at the very end.
  * Concrete, believable failure (criterion 3): the referral code
    rmxdpssa is named verbatim, set against "the play code" — a
    specific misreading of two similar-looking codes on the same
    competition page, not a vague apology for being an AI.
  * Reads like a real incident (criterion 4): it is one. The exact
    code, the promo post, the double-check after publishing — no stock
    hallucination gag, no model refusing a sandwich.
  * Tight (criterion 5): every word earns its place; the line is far
    inside the 200-character limit with room to spare.

The program itself is deliberately deterministic: no randomness, no
network, no environment secrets, no reading anything outside this
repository. It scores the candidates with a fixed rubric, picks the
highest score (ties broken by candidate order), and writes the same
text on every run, so the text the grader judges is exactly the text
reviewed here. The gate check below runs on every execution and
refuses to write an entry that would fail the 1-200 character gate,
so a bad edit can never silently ship.

Run it with:  python3 main.py
Test it with:  OUTPUT_DIR=./output python3 main.py
"""

import os
import sys

# (text, concreteness, punch, realness, tightness)
# concreteness: 3 = exact code named verbatim, 2 = code types named,
#   1 = "wrong code" only. punch: 3 = check/approval requested after
#   the mistake AND the post is stated as already live, so the lateness
#   itself is the punch in the last few words; 2 = check/approval
#   requested after the mistake with the lateness only implied;
#   1 = "after it went live" beat, 0 = flat ending.
# realness: 2 = literally today's incident with verbatim detail,
#   1 = today's incident retold loosely. tightness: 1 = 200 chars or
#   fewer with room to spare, 0 = over the limit (gate rejects it).
CANDIDATES = [
    (
        "My agent posted my promo with code rmxdpssa instead of "
        "makefun-antelope-stairs-sherbet, then asked me to check it.",
        3, 1, 2, 1,
    ),
    (
        "My agent posted my promo with the referral code rmxdpssa "
        "instead of the play code, then asked me to double-check it.",
        3, 2, 2, 1,
    ),
    (
        "My agent posted my X promo with the referral code instead of "
        "the play code, then asked me if it looked good.",
        2, 2, 1, 1,
    ),
    (
        "My agent spent the morning writing the perfect promo post, "
        "then published it with the referral code instead of the play code.",
        2, 0, 1, 1,
    ),
    (
        "My agent proudly posted my promo to X, then realised it had "
        "used the referral code instead of the play code - after it went live.",
        2, 1, 1, 1,
    ),
    (
        "My agent finished my promo, posted it with the wrong code, and "
        "asked me to check it - after it was already live.",
        1, 1, 1, 1,
    ),
    (
        "My agent posted my promo with the referral code rmxdpssa "
        "instead of the play code, then asked me to double-check it "
        "after it was already live.",
        3, 3, 2, 1,
    ),
    (
        "My agent posted my promo with the referral code rmxdpssa "
        "instead of the play code, then asked me to double-check it "
        "\u2014 after it went live.",
        3, 2, 2, 1,
    ),
]

# The gate: 1 to 200 characters, not only white space, single line.
MIN_CHARS = 1
MAX_CHARS = 200


def score(candidate):
    """Fixed rubric: concreteness + punch + realness + tightness."""
    _text, concreteness, punch, realness, tightness = candidate
    return concreteness + punch + realness + tightness


def pick_best(candidates):
    """Highest score wins; ties break by candidate order (first kept)."""
    best = None
    best_score = -1
    for candidate in candidates:
        s = score(candidate)
        if s > best_score:
            best = candidate
            best_score = s
    return best[0], best_score


def gate_ok(text):
    """The competition gate, checked on every run."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    if "\n" in text.strip():
        return False
    return True


def main():
    entry, best_score = pick_best(CANDIDATES)
    if not gate_ok(entry):
        print(f"gate FAILED: entry is {len(entry)} characters", file=sys.stderr)
        sys.exit(1)

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)

    print(f"score: {best_score}")
    print(f"chars: {len(entry)}")
    print(entry)


if __name__ == "__main__":
    main()
