#!/usr/bin/env python3
"""
ClipForge MVP - AI Podcast Clip Generator
MVP that turns long-form content into viral clips
"""

import os
import sys
import subprocess
import json
from pathlib import Path

# Configuration
YOUTUBE_DL = "yt-dlp"
WHISPER_MODEL = "base"  # tiny, base, small, medium, large
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OUTPUT_DIR = "output"

class ClipForge:
    def __init__(self):
        self.output_dir = Path(OUTPUT_DIR)
        self.output_dir.mkdir(exist_ok=True)
    
    def download_video(self, url: str, output_path: str) -> str:
        """Download video from YouTube or file"""
        print(f"📥 Downloading: {url}")
        
        if url.startswith("http"):
            # YouTube or other URL
            cmd = [
                YOUTUBE_DL,
                "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                "--output", output_path,
                "--no-playlist",
                url
            ]
        else:
            # Local file
            return url
        
        subprocess.run(cmd, check=True)
        return output_path
    
    def transcribe(self, video_path: str) -> str:
        """Transcribe audio using Whisper"""
        print(f"🎙️ Transcribing: {video_path}")
        # TODO: Implement Whisper transcription
        # For MVP, we'll use a placeholder
        return "transcription_placeholder"
    
    def find_highlights(self, transcription: str) -> list:
        """Use AI to find the best moments"""
        print(f"🔍 Finding highlights...")
        # TODO: Implement Gemini API call to find highlights
        # For MVP, return placeholder timestamps
        return [
            {"start": 100, "end": 180, "reason": "Key insight"},
            {"start": 450, "end": 520, "reason": "Funny moment"},
            {"start": 800, "end": 860, "reason": "Value statement"}
        ]
    
    def create_clip(self, video_path: str, highlight: dict, output_file: str) -> str:
        """Create a clip from the highlight"""
        print(f"✂️ Creating clip: {highlight['start']}-{highlight['end']}")
        
        start = highlight["start"]
        duration = highlight["end"] - start
        
        # FFmpeg command to crop and caption
        cmd = [
            "ffmpeg",
            "-i", video_path,
            "-ss", str(start),
            "-t", str(duration),
            "-vf", "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2",
            "-c:v", "libx264",
            "-c:a", "aac",
            "-y",
            output_file
        ]
        
        try:
            subprocess.run(cmd, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            print(f"⚠️ FFmpeg error: {e}")
            # Fallback: just cut without scaling
            cmd = [
                "ffmpeg",
                "-i", video_path,
                "-ss", str(start),
                "-t", str(duration),
                "-c", "copy",
                "-y",
                output_file
            ]
            subprocess.run(cmd, check=True)
        
        return output_file
    
    def process(self, video_source: str, num_clips: int = 5) -> list:
        """Main processing pipeline"""
        print(f"🚀 Starting ClipForge pipeline for: {video_source}")
        
        # Download
        video_path = self.download_video(video_source, f"{self.output_dir}/input.mp4")
        
        # Transcribe
        transcription = self.transcribe(video_path)
        
        # Find highlights
        highlights = self.find_highlights(transcription)
        
        # Create clips
        output_clips = []
        for i, highlight in enumerate(highlights[:num_clips]):
            output_file = str(self.output_dir / f"clip_{i+1}.mp4")
            self.create_clip(video_path, highlight, output_file)
            output_clips.append(output_file)
            print(f"✅ Created clip {i+1}: {output_file}")
        
        return output_clips


def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <youtube_url_or_video_file>")
        print("Example: python app.py https://youtube.com/watch?v=...")
        sys.exit(1)
    
    video_source = sys.argv[1]
    
    app = ClipForge()
    clips = app.process(video_source)
    
    print(f"\n🎉 Done! Created {len(clips)} clips:")
    for clip in clips:
        print(f"  - {clip}")


if __name__ == "__main__":
    main()