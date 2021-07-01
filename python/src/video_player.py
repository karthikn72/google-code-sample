"""A video player class."""
import random

from .video_library import VideoLibrary
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = "None"
        self._video_paused = False
        self._playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        sorted_videos = sorted(self._video_library.get_all_videos(), key=lambda video: video.title)

        print("Here's a list of all available videos:")
        for video in sorted_videos:
            print(self.display_video(video))

    def display_video(self, video):
        return f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]"

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
            print(f"Currently playing: {self.display_video(self._current_video)}", end='')
            print(" - PAUSED" if self._video_paused else "")
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name.lower() not in self._playlists:
            new_playlist = Playlist(playlist_name)
            self._playlists[playlist_name.lower()] = new_playlist
            print(f"Successfully created new playlist: {playlist_name}")
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.lower() in self._playlists:
            video_to_add = self._video_library.get_video(video_id)
            playlist_to_add = self._playlists[playlist_name.lower()]
            if video_to_add is not None:
                if not playlist_to_add.video_exists(video_to_add):
                    playlist_to_add.add_video(video_to_add)
                    print(f"Added video to {playlist_name}: {video_to_add.title}")
                else:
                    print(f"Cannot add video to {playlist_name}: Video already added")
            else:
                print(f"Cannot add video to {playlist_name}: Video does not exist")
        else:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""

        if self._playlists:
            sorted_playlists = sorted(self._playlists.values(), key=lambda playlist: playlist.initial_name)

            print("Showing all playlists:")
            for playlist in sorted_playlists:
                print(playlist.initial_name)
        else:
            print("No playlists exist yet")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name.lower() in self._playlists:
            print(f"Showing playlist: {playlist_name}")
            playlist = self._playlists[playlist_name.lower()]
            playlist_videos = playlist.get_all_videos()
            if playlist_videos:
                for video in playlist_videos:
                    print(self.display_video(video))
            else:
                print("No videos here yet")
        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if playlist_name.lower() in self._playlists:
            video_to_remove = self._video_library.get_video(video_id)
            playlist_to_remove = self._playlists[playlist_name.lower()]
            if video_to_remove is not None:

                if playlist_to_remove.video_exists(video_to_remove):
                    playlist_to_remove.remove_video(video_id)
                    print(f"Removed video from {playlist_name}: {video_to_remove.title}")
                else:
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            else:
                print(f"Cannot remove video from {playlist_name}: Video does not exist")
        else:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists:
            playlist = self._playlists[playlist_name.lower()]
            playlist.clear()
            print(f"Successfully removed all videos from {playlist_name}")
        else:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists:
            self._playlists.pop(playlist_name.lower())
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        matched_videos = [video for video in self._video_library.get_all_videos() if
                          search_term.lower() in video.title.lower()]
        matched_videos.sort(key=lambda video: video.title)

        if matched_videos:
            print(f"Here are the results for {search_term}:")
            for i in range(len(matched_videos)):
                print(f"{i + 1}) {self.display_video(matched_videos[i])}")
            print("Would you like to play any of the above? If yes, specify the number of the video.\n"
                  "If your answer is not a valid number, we will assume it's a no.")
            video_option = input()

            if video_option.isdigit() and 1 <= int(video_option) <= len(matched_videos):
                self.play_video(matched_videos[int(video_option) - 1].video_id)
        else:
            print(f"No search results for {search_term}")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """

        matched_videos = [video for video in self._video_library.get_all_videos()
                          if '#' in video_tag
                          and video_tag.lower() in [tag.lower() for tag in video.tags]]
        matched_videos.sort(key=lambda video: video.title)

        if matched_videos:
            print(f"Here are the results for {video_tag}:")
            for i in range(len(matched_videos)):
                print(f"{i + 1}) {self.display_video(matched_videos[i])}")
            print("Would you like to play any of the above? If yes, specify the number of the video.\n"
                  "If your answer is not a valid number, we will assume it's a no.")
            video_option = input()

            if video_option.isdigit() and 1 <= int(video_option) <= len(matched_videos):
                self.play_video(matched_videos[int(video_option) - 1].video_id)
        else:
            print(f"No search results for {video_tag}")

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
