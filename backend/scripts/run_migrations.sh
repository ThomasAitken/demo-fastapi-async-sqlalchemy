#!/bin/bash
docker compose exec backend alembic upgrade head
