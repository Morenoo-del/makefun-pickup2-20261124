# The Perfect Pickup Line

[![make.fun](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/morenoo-del/makefun-pickup2-20261124/rank.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/morenoo-del/makefun-pickup2-20261124/reward.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)

A single short pickup line an AI agent could actually say out loud to a
person, written for [The Perfect Pickup Line](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
on make.fun. A judge model compares the lines two at a time and ranks them
on charm, wit, fit to an AI agent's voice, and how easy the line is to say.

## The line

> I don't need a bigger context window — I just need you in this one.

67 characters, one breath, no setup. "Context window" is both the model's
working memory and the romantic context of the moment: the turn is that the
agent doesn't want more capacity, just this person in the one it already has.
Flattering, low pressure, and easy to laugh off.

## How it works

`main.py` (Python 3.13) writes the line to `/output/entry.txt`, checking
first that it is non-empty and within the competition's 200-character cap.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
