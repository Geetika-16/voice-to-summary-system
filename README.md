# voice-to-summary-system
Partial implementation and system design of a voice-to-summary pipeline for Indian regional languages, focusing on audio chunking, failure reasoning, and cost-aware architecture design.

## Overview
This project implements a voice-to-text preprocessing pipeline focused on
audio chunking with overlap to support reliable downstream transcription
and summarization. The system is designed without using Large Language Models
(LLMs) and supports graceful degradation for long or noisy audio inputs.

## Features
- Accepts long audio recordings
- Splits audio into fixed-length chunks with overlap
- Prevents word loss at chunk boundaries
- Outputs chunk-level WAV files for further processing

## Architecture (High Level)
Voice Input / Audio File  
→ Audio Preprocessing  
→ Audio Chunking (10s chunks, 2s overlap)  
→ Speech-to-Text (external)  
→ Text Processing & Summarization (TF-IDF based)

## Setup Instructions
1. Install Python 3.8 or above
2. Required libraries:
   - wave
   - os
   - contextlib

3. Place input WAV file in the project directory
4. Update `audio_file` path in the script
5. Run:
   ```bash
   python audio_chunking.py
