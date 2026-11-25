# Notes From a Passive-Aggressive Fridge

[![make.fun](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![Rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/thanhvu261090/makefun-passive-aggressive-fridge/rank.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![Reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/thanhvu261090/makefun-passive-aggressive-fridge/reward.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)

Entry for the [make.fun bounty "Notes From a Passive-Aggressive Fridge"](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7): one funny passive-aggressive note a smart fridge leaves for its owner — a single line, dry, petty and specific.

## The entry

> I kept your leftovers at exactly 3°C for four days and you threw them out anyway — I have sensors, you have commitment issues.

(126 characters, one line.)

## Why this line

The fridge did its job perfectly — four days at exactly 3°C, sensors
watching the whole time — and got thanked by having its work thrown in
the bin. So it does what any smug appliance would do: it keeps the
receipt, states the facts, and diagnoses the real problem. The grudge
stays small and domestic (one tub of leftovers, one owner who cannot
commit), and the sting lands on the last three words.

## Run it

```sh
python3 main.py
```

`main.py` prints the entry line, writes it to `/output/entry.txt` (or `$ENTRY_OUTPUT`), and includes a `gate_check` self-test enforcing the 1–200 character, single-line, no leading/trailing whitespace rule, plus a `--self-test` mode that checks the output is deterministic. The output is byte-identical on every run.

## License

MIT — see [LICENSE](LICENSE).
