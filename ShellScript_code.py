#!/bin/bash
# Get today's date
TODAY=$(date +%F)

# 1. Log Running Processes
PROCESS_LOG="process_log_${TODAY}.log"
ps aux > "$PROCESS_LOG"

echo "📝 All running processes saved to $PROCESS_LOG"

# 2. Check for High Memory Usage
HIGH_MEM_LOG="high_mem_processes.log"
HIGH_MEM_PROCESSES=$(ps aux --sort=-%mem | awk '$4 > 30')

if [[ -n "$HIGH_MEM_PROCESSES" ]]; then
    echo "⚠️ WARNING: Some processes are using more than 30% memory!"
    echo "$HIGH_MEM_PROCESSES" >> "$HIGH_MEM_LOG"
else
    echo "✅ No processes using more than 30% memory."
fi

# 3. Check Disk Space on Root Partition
DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')

if [[ "$DISK_USAGE" -gt 80 ]]; then
    echo "⚠️ WARNING: Disk usage on / is above 80% ($DISK_USAGE%)"
else
    echo "✅ Disk usage on / is under control ($DISK_USAGE%)"
fi

# 4. Display Summary
TOTAL_PROCESSES=$(ps aux | wc -l)
HIGH_MEM_COUNT=$(echo "$HIGH_MEM_PROCESSES" | wc -l)

echo ""
echo "📊 Summary:"
echo "Total running processes         : $TOTAL_PROCESSES"
echo "Processes >30% memory usage     : $HIGH_MEM_COUNT"
echo "Disk usage on / partition       : $DISK_USAGE%"
