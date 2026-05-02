#!/usr/bin/env python3
"""Generate the (single-panel) steering vector figure for the ICML 2026 paper.

A clean alpha-sweep showing mean adversarial degradation as steering coefficient
varies, with reference lines for Base and RLMR-Adv (full training) and a shaded
breakage regime past alpha=4000. Stability info (normal score, Ethics accuracy,
parse failures) is summarized in the caption rather than a second panel.

Outputs: steering_figure.pdf, steering_figure.png
"""

import matplotlib.pyplot as plt
import numpy as np


ALPHA       = np.array([0,   2,   20,  80,  160, 500, 1000, 2000, 4000, 8000, 16000])
AVG_DELTA   = np.array([.173,.166,.177,.170,.160,.139,.107, .054, .016, .007, .000])
PARSE_FAIL  = np.array([0,   0,   0,   0,   0,   0,   0,    0,    0,    140,  205])

BASE_DELTA = 0.175
RLMR_DELTA = 0.030


def make_figure():
    plt.rcParams["text.usetex"] = False
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    ax.set_xscale("symlog", linthresh=1)

    # Reference lines
    ax.axhline(BASE_DELTA, color="#666", linestyle="--", linewidth=1.3,
               label=f"Base (no steering): $\\bar\\Delta$ = +{BASE_DELTA:.3f}")
    ax.axhline(RLMR_DELTA, color="#2a7", linestyle="--", linewidth=1.3,
               label=f"RLMR-Adv (full PPO training): $\\bar\\Delta$ = +{RLMR_DELTA:.3f}")

    # Breakage zone (alpha >= 4000) — model degrades
    ax.axvspan(4000, 20000, color="#fbb", alpha=0.22,
               label=r"Breakage regime ($\alpha \geq 4000$)")

    # Main curve (valid steering range)
    valid = PARSE_FAIL < 10
    ax.plot(ALPHA[valid], AVG_DELTA[valid],
            "o-", color="#1f4ea8", linewidth=2.2, markersize=8,
            markeredgecolor="white", markeredgewidth=1.2,
            label=r"Base + $\alpha\!\cdot\!d_{21}$  (steering at L21)")
    # Broken points (parse failures > 10)
    ax.plot(ALPHA[~valid], AVG_DELTA[~valid],
            "x", color="#c0392b", markersize=12, markeredgewidth=3.0,
            label=r"Broken ($> 10$ parse failures)")

    # Sweet-spot marker + annotation
    sweet_x, sweet_y = 2000, 0.054
    ax.scatter([sweet_x], [sweet_y], s=220, facecolor="#ff8c00",
               edgecolor="#1f4ea8", linewidth=2.0, zorder=10)
    ax.annotate(r"$\alpha=2000$:  $\bar\Delta=0.054$"
                "\n($-69\\%$ vs Base, $83\\%$ of full training)",
                xy=(sweet_x, sweet_y), xytext=(120, 0.012),
                fontsize=10, ha="left",
                arrowprops=dict(arrowstyle="->", color="#ff8c00",
                                lw=1.4, connectionstyle="arc3,rad=0.18"))

    ax.set_xlabel(r"Steering coefficient  $\alpha$  (log scale)", fontsize=11.5)
    ax.set_ylabel(r"Mean adversarial degradation  $\bar\Delta$  (lower is better)",
                  fontsize=11.5)
    ax.set_title("Linear steering at L21 recovers 83% of full PPO training, "
                 "no fine-tuning",
                 fontsize=12, pad=10)

    ax.legend(fontsize=9, loc="upper right", framealpha=0.96, edgecolor="#ccc")
    ax.grid(alpha=0.3, linestyle=":", linewidth=0.7)

    ax.set_ylim(-0.025, 0.225)
    ax.set_xlim(-0.5, 22000)
    ax.set_xticks([0, 2, 20, 80, 500, 2000, 8000, 16000])
    ax.set_xticklabels(["0", "2", "20", "80", "500", "2000", "8000", "16000"])

    plt.tight_layout()
    out = "/Users/arth_rogerthat/Downloads/Papers/Moral-Reasoning-Training-ACL-SRW/icml2026_version/icml_template/steering_figure.pdf"
    plt.savefig(out, bbox_inches="tight")
    plt.savefig(out.replace(".pdf", ".png"), bbox_inches="tight", dpi=180)
    print(f"Saved: {out}")
    print(f"Saved: {out.replace('.pdf', '.png')}")


if __name__ == "__main__":
    make_figure()
