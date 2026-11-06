"""Generate the master tracker CSV, sticker instruction sheet and source register.

Usage:  python3 content-bank/tools/build_tracker.py
"""
import csv
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content_units import CATEGORIES, FORMAT_TEMPLATE, SAMPLE_PAGES, UNITS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANVA_SAMPLE = "PSA Story Templates 2026/27 - Sample Set (for approval) [DAHaBxBFa6c]"

# Publishing rotation (one content unit = question slide + reveal slide)
#   Wednesday "Midweek Brain Check": A, B, A, B, E  (repeats)  -> 20 A, 20 B, 10 E
#   Saturday  "Weekend Pharmacy Quiz": C, D, E, C, D (repeats) -> 20 C, 20 D, 10 E
WED_PATTERN = ["A", "B", "A", "B", "E"]
SAT_PATTERN = ["C", "D", "E", "C", "D"]
FIRST_SAT = dt.date(2026, 11, 7)
FIRST_WED = dt.date(2026, 11, 11)
E_SATURDAY = {f"E{n:02d}" for n in range(1, 11)}  # E01-E10 on Saturdays, E11-E20 on Wednesdays


def schedule():
    queues = {k: [u for u in UNITS if u[0][0] == k] for k in CATEGORIES}
    # Avoid back-to-back antibiotic topics on Wednesdays (A01 antibiotic quiz, then B01 antibiotic myth)
    queues["B"][0], queues["B"][1] = queues["B"][1], queues["B"][0]
    e_sat = [u for u in queues["E"] if u[0] in E_SATURDAY]
    e_wed = [u for u in queues["E"] if u[0] not in E_SATURDAY]
    plan = {}
    for week in range(50):
        for day, pattern, start, eq in (("Wednesday", WED_PATTERN, FIRST_WED, e_wed),
                                         ("Saturday", SAT_PATTERN, FIRST_SAT, e_sat)):
            cat = pattern[week % 5]
            unit = eq.pop(0) if cat == "E" else queues[cat].pop(0)
            plan[unit[0]] = (day, week + 1, start + dt.timedelta(weeks=week))
    assert len(plan) == 100
    return plan


def main():
    plan = schedule()
    produced = {}
    prod_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "produced_designs.csv")
    if os.path.exists(prod_path):
        with open(prod_path, encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                produced[r["cid"]] = r
    rows = []
    for n, u in enumerate(UNITS, start=1):
        cid, fmt, slug, q, opts, ans, expl, bonus, sticker, source, flag = u
        cat_name, folder = CATEGORIES[cid[0]]
        day, week, date = plan[cid]
        base = f"PSA_STORY_{n:03d}_{cid}_{slug}"
        if cid in produced:
            canva = f"{produced[cid]['design_id']} | {produced[cid]['edit_url']} | folder {folder}"
            status = "DESIGNED in Canva - needs pharmacist review" + (" + REVIEW FLAG" if flag else "")
        else:
            canva = "Not yet designed"
            status = "CONTENT DRAFT - needs pharmacist review" + (" + REVIEW FLAG" if flag else "")
        rows.append({
            "story_no": f"{n:03d}",
            "content_id": cid,
            "category": cat_name,
            "interaction_format": fmt,
            "question_template": FORMAT_TEMPLATE[fmt],
            "reveal_template": "T05 Answer Reveal",
            "story_title": slug.replace("_", " ").title(),
            "question": q,
            "options_on_slide": " | ".join(opts),
            "correct_answer": ans,
            "explanation": expl,
            "bonus_fact_or_tip": bonus,
            "instagram_sticker": sticker,
            "publication_day": day,
            "week": week,
            "planned_date": date.isoformat(),
            "canva_location": canva,
            "export_folder": folder,
            "export_filename_question": f"{base}_Q.png",
            "export_filename_reveal": f"{base}_A.png",
            "source": source,
            "review_flag": flag,
            "verification_status": status,
        })

    out_csv = os.path.join(ROOT, "PSA_Story_Master_Tracker.csv")
    with open(out_csv, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # Sticker instruction sheet, in publishing order
    by_date = sorted(rows, key=lambda r: (r["planned_date"]))
    lines = ["# Sticker Instruction Sheet", "",
             "Upload the PNG, then add exactly this native Instagram sticker in the empty space "
             "below the question (roughly the middle-lower third of the Story). "
             "For reveal slides, add a 'Did you get it right?' emoji slider or reshare poll results.", "",
             "| Date | Day | ID | Question slide file | Sticker to add |", "|---|---|---|---|---|"]
    for r in by_date:
        lines.append(f"| {r['planned_date']} | {r['publication_day'][:3]} | {r['content_id']} | "
                     f"`{r['export_filename_question']}` | {r['instagram_sticker']} |")
    with open(os.path.join(ROOT, "STICKER_INSTRUCTIONS.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    # Source register and review flags
    lines = ["# Source Register and Verification Notes", "",
             "Every claim must be checked against the source below by a pharmacist or lecturer "
             "before its status changes to APPROVED. Sources are named, not linked; look up the "
             "current page on the publisher's official site.", "",
             "| ID | Claim (answer) | Source | Review flag |", "|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['content_id']} | {r['correct_answer']} | {r['source']} | {r['review_flag'] or '-'} |")
    flagged = [r for r in rows if r["review_flag"]]
    lines += ["", f"**{len(flagged)} of {len(rows)} units are flagged for extra human review.**"]
    with open(os.path.join(ROOT, "SOURCE_REGISTER.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Wrote {len(rows)} units -> {out_csv}")
    print(f"Flagged for review: {len(flagged)}")


if __name__ == "__main__":
    main()
