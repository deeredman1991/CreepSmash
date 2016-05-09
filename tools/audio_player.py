import threading
import time
import tools.pyaudio.pyaudio as pyaudio
import wave


class AudioPlayer(object):
    def __init__(self):
        self._audio_file = None
        self._music_track = None
        self._stop_music = False
        
    @property
    def music_track(self):
        return self._music_track
        
    @music_track.setter
    def music_track(self, track):
        if track != None:
            self.play_music(track)
        
    def stop_music(self):
        self._stop_music = True
        
    def play_music(self, musicfile):
        while self._music_track != None:
            self.stop_music()
            time.sleep(0.5)
        self._audio_file = musicfile
        self._music_track = self._audio_file
        music_thread = threading.Thread( target = (self._play_audio) )
        music_thread.setDaemon( True )
        music_thread.start()
        
    def play_sound(self, soundfile):
        self._audio_file = soundfile
        threading.Thread( target = (self._play_audio) ).start()
        time.sleep(0.5)
        
    def _play_audio(self):
        chunk_size = 1024
        _audio_file = self._audio_file
        
        wf = wave.open(_audio_file, 'rb')

        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
                
        data = wf.readframes(chunk_size)

        while data != '':
            if self._stop_music:
                break
            stream.write(data)
            data = wf.readframes(chunk_size)
            
        stream.stop_stream()
        stream.close()

        p.terminate()
        
        if _audio_file == self._music_track:
            if self._stop_music == True:
                self._stop_music = False
            self._music_track = None
            self.playing_music = False
            

if __name__ == '__main__':
    csAnthem = "sound/music/Creepsmash_Anthem.wav"
    tick = "sound/tick.wav"

    audio_player = AudioPlayer()
    audio_player.play_music(csAnthem)
    print ("Now playing Creepsmash Anthem!")