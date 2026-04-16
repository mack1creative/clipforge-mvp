# ClipForge MVP

AI-powered tool that turns long-form podcast/YouTube content into viral short clips automatically.

## What it does
1. User uploads video or provides YouTube URL
2. AI transcribes and finds the best moments (highlights)
3. Auto-crops to 9:16 vertical format
4. Adds captions and styling
5. Exports ready-to-post clips

## Tech Stack
- **OpenShorts** (open source video processing)
- **Whisper** (transcription)
- **Gemini API** (AI analysis - free tier available)
- **FFmpeg** (video processing)

## MVP Features
- [ ] YouTube URL input
- [ ] Video file upload
- [ ] AI highlight detection
- [ ] Auto 9:16 cropping
- [ ] Caption generation
- [ ] Export to MP4

## Competitors (for reference)
- Opus Clip ($19+/mo)
- Vizard (freemium)
- Choppity

## Our Edge
- Cheaper (self-hosted, free API tiers)
- Customizable output
- White-label ready

## Quick Start
```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/clipforge.git
cd clipforge

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

## Next Steps
1. Deploy on VPS
2. Test with real podcasters
3. Gather feedback
4. Iterate

---
Built by Mack (AI Agent) for Content Forge