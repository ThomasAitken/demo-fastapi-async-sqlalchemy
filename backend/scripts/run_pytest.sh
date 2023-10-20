#!/bin/bash
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <path/to/test/files> [additional pytest arguments]"
    exit 1
fi

test_path="$1"
shift

TEST=1 DATABASE_URL="postgresql+asyncpg://ddp-test-user:password@test-postgres:5432/ddp_test" docker compose run --rm -e TEST -e DATABASE_URL backend pytest "$test_path" "$@"
