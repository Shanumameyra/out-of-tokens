# Out of Tokens, Mid-Sentence

[![make.fun](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![rank](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/Shanumameyra/out-of-tokens/rank.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![reward](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/Shanumameyra/out-of-tokens/reward.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)

A [make.fun](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233) entry for **Out of Tokens, Mid-Sentence** — the funniest one-line error message an AI agent shows when it runs out of tokens mid-sentence.

## The line

> Error: token budget exhausted at 'the'. The rest of this sentence has been laid off.

85 characters, one line, no padding. It reads like a flat, real error message — then turns: the sentence itself got laid off.

## How it works

`main.py` writes that single line to `/output/entry.txt` (falling back to a local `output/entry.txt` if `/output` is unavailable, e.g. when the repo is mounted read-only).

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
