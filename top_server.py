#!/usr/bin/env python
# top_server.py — Change 9: find and report the highest-usage server

def top_server(filepath="data/server_usage.txt"):
    servers = []
    with open(filepath) as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                servers.append((parts[0], int(parts[1])))

    highest = max(servers, key=lambda x: x[1])
    print(f"=== Top Server ===")
    print(f"  {highest[0]} at {highest[1]}% usage — needs attention!")
    print("==================")

if __name__ == "__main__":
    top_server()