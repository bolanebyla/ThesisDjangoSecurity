#!/bin/bash

running="$(docker-compose ps --services --filter "status=running")"
services="$(docker-compose ps --services)"
if [ "$running" != "$services" ]; then
    echo "Following services are not running:"
    # Bash specific
    comm -13 <(sort <<<"$running") <(sort <<<"$services")
else
    echo "All services are running"
fi