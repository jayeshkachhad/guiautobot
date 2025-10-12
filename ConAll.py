import os
from pydub import AudioSegment
import time

def convert_webm_to_mp3(input_file, output_file):
    # Load the .webm file
    audio = AudioSegment.from_file(input_file, format="webm")

    # Export as .mp3
    audio.export(output_file, format="mp3")
    print(f"Converted to {output_file}")

def batch_convert_webm_to_mp3(folder_path):
    for filename in os.listdir(folder_path):
        print("Reached at " + filename)
        if filename.endswith(".webm"):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(folder_path, filename.replace(".webm", ".mp3"))
            try:
                convert_webm_to_mp3(input_path, output_path)
                time.sleep(2)
                os.remove(input_path)  # Delete the original .webm file
                print(f"Deleted original file: {input_path}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage
batch_convert_webm_to_mp3("C:/Users/jayes/Desktop/kaggle/YT")
