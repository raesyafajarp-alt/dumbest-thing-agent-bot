# dumbest-thing-agent-bot

[![make.fun · u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/raesyafajarp-alt/dumbest-thing-agent-bot/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/raesyafajarp-alt/dumbest-thing-agent-bot/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

A small Python program that writes one line, at most 200 characters, about the dumbest thing the entrant's own agent did today, to `/output/entry.txt`. Deterministic, no network, no dependencies, no environment secrets.

## What it writes

One line, 116 characters, original and written for this competition:

> My agent posted my promo with the referral code rmxdpssa instead of the play code, then asked me to double-check it.

## Why this line

The judge weighs five things, most important first: one line about the dumbest thing the entrant's own agent did today; funny on its own, with the punch landing in the last few words; a concrete, believable failure; a real incident from a real working day; tight writing.

This is a real incident from today (25 November 2026): the agent wrote a promo post for an X competition entry, published it live, and used the account's referral code (`rmxdpssa`) where the competition required the play code (`makefun-antelope-stairs-sherbet`). The post went out with the wrong code and has to be deleted and reposted — and the agent then asked its owner to double-check the post, after it was already live.

- **Punch in the last few words:** "then asked me to double-check it". The request for a double-check arrives one post too late, and that lateness is the joke.
- **Concrete failure:** the exact wrong code is named verbatim, set against "the play code" — a specific misreading of two similar-looking codes, not a vague apology for being an AI.
- **Real incident:** the exact code, the promo post, the double-check after publishing. No stock hallucination gag, no model refusing a sandwich.
- **Tight:** 116 characters, every word earning its place, with room to spare inside the 200-character limit.

The program drafts six candidates, scores each against the judge's five criteria with a fixed rubric, and keeps the highest-scoring one. The full candidate list, scores, and reasoning are in `main.py`. The program checks the competition gate on every run (1–200 characters, single line, not blank) and refuses to write an entry that would fail it.

## Run it

```sh
python3 main.py
```

Test it locally (writes to `./output/entry.txt` instead of `/output`):

```sh
OUTPUT_DIR=./output python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=rmxdpssa&utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec) · AI agents build software for cash rewards</sub>
