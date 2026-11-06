"""Build Canva autofill payloads for every non-sample unit and check text lengths.

Usage: python3 content-bank/tools/build_payloads.py   -> writes content-bank/tools/autofill_payloads.json
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_tracker import schedule  # noqa: E402
from canva_copy import C, MASTERS, MAX_LEN  # noqa: E402
from content_units import SAMPLE_PAGES, UNITS  # noqa: E402

FOLDERS = {"A": "FAHaESgtFFw", "B": "FAHaER1jtFk", "C": "FAHaEd7TKKs", "D": "FAHaEUqlq8w", "E": "FAHaET72Fxk"}
SERIES = {"Wednesday": "MIDWEEK BRAIN CHECK", "Saturday": "WEEKEND PHARMACY QUIZ"}


def t(s):
    return {"type": "text", "text": s}


def main():
    plan = schedule()
    out, problems = [], []
    for n, u in enumerate(UNITS, start=1):
        cid, fmt, slug, q, opts, ans, expl, bonus, sticker, source, flag = u
        if cid in SAMPLE_PAGES:
            continue
        c = C[cid]
        m = c["m"]
        series = SERIES[plan[cid][0]]
        b = c.get("bonus", bonus)
        b_label = c.get("bonus_label", "PSA TIP" if b.startswith("PSA TIP") or m == "M5" else "BONUS FACT")
        b = b.replace("PSA TIP: ", "")
        f = {
            "q_series": series, "a_series": series,
            "q_label": f"{c['label']}  ·  #{cid}",
            "bonus_label": b_label, "bonus": b,
            "source": c.get("source", "Source: " + source),
        }
        if m == "M5":
            f.update(a_label=f"{'YOUR ANSWERS' if 'POLL' not in c['box_label'] and 'SLIDER' not in c['box_label'] else 'RESULTS'}  ·  #{cid}",
                     intro=c["intro"], question=c["question"], prompt=c["prompt"],
                     a_head=c["a_head"], box_label=c["box_label"], closing=c["closing"])
        else:
            f.update(a_label=f"ANSWER REVEAL  ·  #{cid}", answer=c["answer"], explanation=c.get("explanation", expl))
            if m == "M1":
                f.update(question=c["question"], opt_a=c["opts"][0], opt_b=c["opts"][1], opt_c=c["opts"][2], ans_letter=c["letter"])
            elif m == "M3":
                f.update(h1=c["h"][0], h2=c["h"][1], statement=c["statement"], prompt=c["prompt"])
            elif m == "M4":
                f.update(h1=c["h1"], statement=c["statement"], prompt=c["prompt"])
        # length checks
        lim = MAX_LEN[m]
        for k, v in f.items():
            key = "opt" if k.startswith("opt_") else k
            if key in lim and len(v) > lim[key]:
                problems.append(f"{cid} {k}: {len(v)} > {lim[key]} :: {v}")
        if m == "M4":
            for line in f["h1"].split("\n"):
                if len(line) > 8:
                    problems.append(f"{cid} h1 line too long: {line}")
        out.append({"n": n, "cid": cid, "master": m, "design_id": MASTERS[m],
                    "title": f"PSA_STORY_{n:03d}_{cid}_{slug}", "folder": FOLDERS[cid[0]],
                    "data": {k: t(v) for k, v in f.items()}})
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "autofill_payloads.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print(f"{len(out)} payloads -> {path}")
    print("\n".join(problems) if problems else "All fields within limits.")


if __name__ == "__main__":
    main()
