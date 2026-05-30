#!/usr/bin/env python3
# check_usage.py — full version with sorting, logging, summary, CLI arg

import sys
from datetime import datetime

# Change 12: accept optional filepath as CLI argument
filepath = sys.argv[1] if len(sys.argv) > 1 else "data/server_usage.txt"

def read_usage(filepath):
    servers = []
    with open(filepath, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                servers.append({"name": parts[0], "usage": int(parts[1])})
    return servers

def classify(usage):
    if usage >= 90: return "CRITICAL"
    if usage >= 75: return "WARNING"
    return "OK"

def report(servers):
    # Change 10: sort descending by usage
    servers = sorted(servers, key=lambda s: s["usage"], reverse=True)

    lines = []
    counts = {"OK": 0, "WARNING": 0, "CRITICAL": 0}
    lines.append(f"\n=== Server Usage Report — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")

    for s in servers:
        status = classify(s["usage"])
        counts[status] += 1
        lines.append(f"  {s['name']:12} {s['usage']:3}%  [{status}]")

    avg = sum(s["usage"] for s in servers) / len(servers)
    lines.append(f"\n  Average: {avg:.1f}%")

    # Change 8: status summary counts
    lines.append(f"  Summary: {counts['OK']} OK  |  {counts['WARNING']} WARNING  |  {counts['CRITICAL']} CRITICAL")
    lines.append("=" * 44)

    output = "\n".join(lines)
    print(output)

    # Change 7: write report to reports/audit.log
    with open("reports/audit.log", "a") as log:
        log.write(output + "\n")

if __name__ == "__main__":
    servers = read_usage(filepath)
    report(servers)