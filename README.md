[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/inifikry/news-image-20261126-makefun/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/inifikry/news-image-20261126-makefun/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
# News Image — 26 November 2026

One image that sums up the world's news of **Thursday 26 November 2026**,
drawn entirely in code with Pillow.

## The image

A newspaper front page, "THE WORLD IN ONE DAY — THURSDAY 26 NOVEMBER 2026",
with six stories across regions and fields:

1. **Middle East / Oil** — Houthis claim strikes on Saudi refinery; Brent tops $94.
2. **Trade / USA** — US unveils sweeping new tariffs on 14 partners; Taiwan faces up to 15%.
3. **Egypt** — Cairo ring-road inferno kills 30 after a fuel tanker crash.
4. **Ukraine war** — Russia's own figures put its war dead at nearly 500,000.
5. **Space** — BepiColombo reaches Mercury after an eight-year voyage.
6. **Sport** — 15-year-old Vaibhav Sooryavanshi hits 204 off 53 balls, the fastest
   List A double century.

Footer: Thanksgiving in the US; India marks Constitution Day and 18 years since
the 26/11 Mumbai attacks; Duran Duran guitarist Andy Taylor dies at 65;
World Chess Championship Game 2 ends in a draw.

## Run

```sh
python3 generate.py   # draws entry.png (1024x1024, PNG)
python3 main.py       # copies entry.png to /output/entry.png
```

`main.py` uses only the standard library and runs with no network; it copies
the image byte for byte, so both grader runs produce identical output.

## License

MIT. See [LICENSE](LICENSE).
