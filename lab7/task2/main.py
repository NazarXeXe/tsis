import pygame
import os
import sys
from pygame import mixer


class MusicPlayer:
    def __init__(self):
        pygame.init()
        mixer.init()

        self.screen_width = 600
        self.screen_height = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pygame Music Player")

        self.font = pygame.font.SysFont('Arial', 24)
        self.large_font = pygame.font.SysFont('Arial', 32)

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GRAY = (100, 100, 100)
        self.BLUE = (0, 0, 255)

        # Music variables
        self.music_dir = 'music'
        self.playlist = self.load_music()
        self.current_track = 0
        self.playing = False
        self.paused = False

        # Controls info
        self.controls = {
            'SPACE': 'Play/Pause',
            'LEFT': 'Previous',
            'RIGHT': 'Next',
            'ESCAPE': 'Quit',
            'S': 'Stop'
        }

        if self.playlist:
            self.load_track(self.current_track)

    def load_music(self):
        """Load music files from the music directory"""
        if not os.path.exists(self.music_dir):
            os.makedirs(self.music_dir)
            print(f"Created music directory: {self.music_dir}")
            print("Add .mp3 files to this directory and restart the program")
            return []

        playlist = []
        for file in os.listdir(self.music_dir):
            if file.endswith('.mp3'):
                playlist.append(os.path.join(self.music_dir, file))

        return playlist

    def load_track(self, index):
        """Load a specific track from the playlist"""
        if not self.playlist:
            return

        mixer.music.load(self.playlist[index])

    def play(self):
        """Play the current track"""
        if not self.playlist:
            return

        if self.paused:
            mixer.music.unpause()
            self.paused = False
        else:
            mixer.music.play()

        self.playing = True

    def stop(self):
        mixer.music.stop()
        self.playing = False
        self.paused = False

    def pause(self):
        if self.playing and not self.paused:
            mixer.music.pause()
            self.paused = True
            self.playing = False

    def next_track(self):
        if not self.playlist:
            return

        self.current_track = (self.current_track + 1) % len(self.playlist)
        self.load_track(self.current_track)
        if self.playing:
            self.play()

    def previous_track(self):
        if not self.playlist:
            return

        self.current_track = (self.current_track - 1) % len(self.playlist)
        self.load_track(self.current_track)
        if self.playing:
            self.play()

    def get_current_track_name(self):
        if not self.playlist:
            return "No tracks available"

        return os.path.basename(self.playlist[self.current_track])

    def draw_controls(self):
        y_offset = 300
        for key, action in self.controls.items():
            text = self.font.render(f"{key}: {action}", True, self.WHITE)
            self.screen.blit(text, (20, y_offset))
            y_offset += 30

    def draw(self):
        """Draw the music player interface"""
        self.screen.fill(self.BLACK)

        status = "PLAYING" if self.playing else "PAUSED" if self.paused else "STOPPED"
        status_text = self.large_font.render(status, True, self.BLUE)
        self.screen.blit(status_text, (self.screen_width // 2 - status_text.get_width() // 2, 50))

        track_text = self.font.render(f"Now Playing: {self.get_current_track_name()}", True, self.WHITE)
        self.screen.blit(track_text, (self.screen_width // 2 - track_text.get_width() // 2, 120))

        if self.playlist:
            track_number = self.font.render(f"Track {self.current_track + 1}/{len(self.playlist)}", True, self.WHITE)
            self.screen.blit(track_number, (self.screen_width // 2 - track_number.get_width() // 2, 160))

        self.draw_controls()
        pygame.display.flip()

    def run(self):
        """Main game loop"""
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_SPACE:
                        if self.playing:
                            self.pause()
                        else:
                            self.play()
                    elif event.key == pygame.K_s:
                        self.stop()
                    elif event.key == pygame.K_RIGHT:
                        self.next_track()
                    elif event.key == pygame.K_LEFT:
                        self.previous_track()
            self.draw()

            clock.tick(30)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    player = MusicPlayer()
    player.run()