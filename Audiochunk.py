import sys
import os
import wave
import contextlib

sys.stdout.reconfigure(encoding ="utf = 8")

audio_file = "Newwton input.wav"

chunk_duration = 10
overlap_duration = 2
output_dir = "audio_chunks"
os.makedirs(output_dir, exist_ok=True)

print("==========AUDIO CHUNKING WITH OVERLAP LOGIC===========")

#opening the wav file safely now

with contextlib.closing(wave.open(audio_file, 'r')) as wf:
    frame_rate = wf.getframerate()
    total_frames = wf.getnframes()
    total_duration = total_frames/frame_rate

print(f"Load audio file: {audio_file}")
print(f"Frame rate: {frame_rate}")
print(f"Total frame: {total_frames}")
print(f"Total duration: {total_duration}")

start_time = 0.0
chunk_index = 1
size = chunk_duration - overlap_duration #which used to avoid the missing part of audios and gather all the audio

#opening audio files again to extract the audio chunks

with wave.open(audio_file, 'rb') as wf:

    params = wf.getparams()
    while start_time < total_duration:
        wf.setpos(int(start_time * frame_rate))
        farmes_to_read = int(chunk_duration * frame_rate)
        frames = wf.readframes(farmes_to_read)

        if not frames:
            break

        chunk_filename = os.path.join(output_dir, f"chunk_{chunk_index}.wav")
        
        with wave.open(chunk_filename, 'wb') as chunk_file:
            chunk_file.setparams(params)
            chunk_file.writeframes(frames)

        print(
            f"chunk{chunk_index}: "
            f"{round(start_time, 2)}s -"
            f"{round(start_time + chunk_duration, 2)}s"
            f"Saved to {chunk_filename}"
        )

        start_time += size
        chunk_index += 1

print("\n Audio chunk Created Sucessfully")
print("Total chunks created: ", chunk_index - 1)
