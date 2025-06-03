#!/bin/bash

echo "🚀 Starting Cooper Penniman Portfolio Website..."
echo "📂 Serving from: $(pwd)"
echo "🌐 Local URL: http://localhost:8000"
echo "⏹️  Press Ctrl+C to stop the server"
echo ""

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    python3 -m http.server 8000
elif command -v python &> /dev/null; then
    python -m http.server 8000
else
    echo "❌ Python not found. Please install Python 3 to run this server."
    exit 1
fi 