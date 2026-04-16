#!/bin/bash
# ClipForge MVP - Quick Test Script

echo "🧪 ClipForge MVP Test Runner"
echo "=============================="

# Check dependencies
echo "📋 Checking dependencies..."

command -v ffmpeg >/dev/null 2>&1 || { echo "❌ ffmpeg not found. Install: brew install ffmpeg"; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "❌ python3 not found"; exit 1; }

echo "✅ Basic dependencies OK"

# Check Python packages
echo "📦 Checking Python packages..."
python3 -c "import yt_dlp" 2>/dev/null || { echo "⚠️ Installing yt-dlp..."; pip install yt-dlp; }
python3 -c "import google.generativeai" 2>/dev/null || { echo "⚠️ Installing google-generativeai..."; pip install google-generativeai; }

echo "✅ Python packages OK"

# Test with sample video
echo ""
echo "🧪 Running test..."
echo "Note: For full test, provide a YouTube URL or video file"
echo ""
echo "Usage: python3 app.py <youtube_url_or_video_file>"
echo ""
echo "Example: python3 app.py https://www.youtube.com/watch?v=dQw4w9WgXcQ"
echo ""

# Quick sanity check
echo "🔬 Running basic functionality check..."
python3 -c "
from app import ClipForge
app = ClipForge()
print('✅ ClipForge imports OK')
print(f'📁 Output directory: {app.output_dir}')
"