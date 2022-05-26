#!/bin/bash

sleep 10
docker-compose ps

running="$(docker-compose ps --services --filter "status=running")"
services="$(docker-compose ps --services)"

if [ "$running" != "$services" ]; then
    echo "Following services are not running:"
    # выводим список сервисов с ошибкой
    comm -13 <(sort <<<"$running") <(sort <<<"$services")
    exit 1
else
    echo "All services are running"
fi