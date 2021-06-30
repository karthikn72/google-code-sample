"""A video player class."""
import random

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = "None"
        self._video_paused = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        sorted_videos = sorted(self._video_library.get_all_videos(), key=lambda video: video.title)

        print("Here's a list of all available videos:")
        for video in sorted_videos:
            print(f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video_to_play = self._video_library.get_video(video_id)
        if self._current_video != "None" and video_to_play is not None:
            self.stop_video()

        if video_to_play is not None:
            print(f"Playing video: {video_to_play.title}")
            self._current_video = video_to_play
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self._current_video != "None":
            print(f"Stopping video: {self._current_video.title}")
            self._current_video = "None"
            self._video_paused = False
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        all_ids = [video.video_id for video in self._video_library.get_all_videos()]
        if all_ids is not None:
            random_id = random.choice(all_ids)
            self.play_video(random_id)
        else:
            print("No videos available")

    def pause_video(self):
        """Pauses the current video."""

        if not self._video_paused and self._current_video != "None":
            print(f"Pausing video: {self._current_video.title}")
            self._video_paused = True
        elif self._current_video == "None":
            print("Cannot pause video: No video is currently playing")
        elif self._video_paused:
            print(f"Video already paused: {self._current_video.title}")

    def continue_video(self):
        """Resumes playing the current video."""

        if self._video_paused and self._current_video != "None":
            print(f"Continuing video: {self._current_video.title}")
            self._video_paused = False
        elif self._current_video == "None":
            print("Cannot continue video: No video is currently playing")
        elif not self._video_paused:
            print("Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""
        if self._current_video != "None":
            print(
                f"Currently playing: {self._current_video.title} ({self._current_video.video_id}) [{' '.join(self._current_video.tags)}]",
                end='')
            print(" - PAUSED" if self._video_paused else "")
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
