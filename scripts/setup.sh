#!/bin/bash
set -euo pipefail
echo "Setting up Enterprise Knowledge Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
