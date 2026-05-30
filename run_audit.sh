#!/bin/bash
# run_audit.sh — full audit runner with conditionals

# Change 1: timestamp header
echo "=============================="
echo "  Audit started: $(date)"
echo "=============================="

# Change 11: count servers in data file
SERVER_COUNT=$(wc -l < data/server_usage.txt)
echo "Servers in file: $SERVER_COUNT"
echo ""

# Change 4: if/else exit code check
if py scripts/check_usage.py; then
    echo "[OK] Usage check passed."
else
    echo "[ERROR] Usage check failed!"
    exit 1
fi

# Change 6: invoke second python script
echo ""
py scripts/top_server.py

# Change 5: check if report was generated
if [ -f reports/audit.log ]; then
    echo ""
    echo "[LOG] Report saved to reports/audit.log"
else
    echo "[WARN] No log file found."
fi

# Change 2: disk usage
echo ""
echo "=== Disk Usage ==="
df -h

# Change 3: who is logged in
echo ""
echo "=== Active Users ==="
who

echo ""
echo "Audit complete: $(date)"