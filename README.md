# Arabic YouTube Transcriber



A Python-based tool for transcribing Arabic YouTube videos that do not have available subtitles or closed captions (CC).



Powered by Faster-Whisper and the Whisper large-v3 model, the project generates Arabic transcripts with segment-level timestamps, making it easier to create, edit, and synchronize subtitles.



## Features



Arabic speech transcription from audio recordings.



Whisper large-v3 model for high transcription accuracy.



NVIDIA GPU acceleration using CUDA.



FP16 computation for GPU inference.



Segment-level timestamps for subtitle synchronization.



UTF-8 text output supporting Arabic characters.



Transcripts can be converted to SRT format and edited using subtitle editing software.



## Recommended Workflow



For the best transcription results, audio preparation is strongly recommended.



Based on testing, the following workflow produced the most accurate results:



### 1\. Obtain the YouTube audio



Download or extract the audio from the YouTube video you want to transcribe.



### 2\. Enhance the audio



Upload the audio to Adobe Podcast Enhance Speech.



This tool helps improve speech clarity and reduce background noise. Its free tier has offered two 30-minute enhancements, although availability and limits may change.



### 3\. Export as WAV



Download the enhanced recording in .wav format.



This was the preferred audio format in testing and provided the best results when combined with audio enhancement.



### 4\. Run the transcription



Place the enhanced WAV file in the project directory and run the Python script.



Important: Skipping audio enhancement or using unclear, noisy, or poorly processed recordings can significantly affect transcription quality. This may result in incorrect words, missing phrases, or AI-generated hallucinations.



## Technologies



Python



Faster-Whisper



Whisper large-v3



CTranslate2



NVIDIA CUDA



## Requirements



Python 3.9+



NVIDIA GPU with CUDA support (for GPU acceleration).



Compatible NVIDIA CUDA and cuDNN libraries.



Enhanced audio recording in WAV format (recommended).



## Installation



Clone the repository:



git clone https://github.com/elionrexhepi01-dev/arabic-youtube-transcriber.git

cd arabic-youtube-transcriber



Install dependencies:



pip install -r requirements.txt



For GPU acceleration, ensure the required NVIDIA CUDA and cuDNN libraries are installed and accessible.



## Usage



Place your enhanced .wav audio recording in the project directory.



Update the audio filename in transcribe.py if necessary:



segments, info = model.transcribe(

&#x20;   "lesson1.wav",

&#x20;   language="ar",

&#x20;   task="transcribe"

)



Run the script:



python transcribe.py



The transcription will be printed in the terminal and saved to a .txt file.



## Transcription Output



The generated text contains timestamps for each transcribed segment.



Example:



\[0.00s -> 4.52s] بسم الله الرحمن الرحيم

\[4.52s -> 8.31s] الحمد لله رب العالمين

\[8.31s -> 12.75s] والصلاة والسلام على رسول الله



These timestamps make it possible to convert the transcript into an .srt subtitle file.



The resulting subtitles can then be imported into Subtitle Edit for reviewing, correcting transcription errors, and adjusting subtitle timing.



Model



The project uses Whisper large-v3, prioritizing transcription accuracy over inference speed.



The model is downloaded automatically by Faster-Whisper on its first use.



## Accuracy Notes



Automatic speech recognition is not perfect. Even with large-v3, transcription errors and hallucinations can occur, particularly when audio quality is poor.



For the most reliable results, follow the recommended audio enhancement workflow and manually review the generated transcript before using it as subtitles.



## License



MIT License

