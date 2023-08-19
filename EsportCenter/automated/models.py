import re

from bs4 import BeautifulSoup
from django.contrib.sites import requests
import requests
from pytube import YouTube, Channel
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


# Create your models here.
class AutomatedListPage(Page):
    # my_books=["aaa","bbb","ccc"]
    #
    # books_list  = RichTextField(blank=True, default="\n".join(my_books))
    #
    # content_panels = Page.content_panels + [
    #     FieldPanel('books_list'),
    # ]

    def youtube_video_list(self):
        # Make a request to the YouTube channel page
        url = 'https://www.youtube.com/c/DylanIsInTrouble/videos'
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the video titles and links
        video_list = []
        for link in soup.find_all('a', {'id': 'video-title'}):
            title = link.get('title')
            video_url = 'https://www.youtube.com' + link.get('href')
            video_list.append({'title': title, 'url': video_url})
            if len(video_list) == 10:
                break
        print(len(video_list))
        return video_list

    def get_newest_youtube_videos(self):
        channel_url = 'https://www.youtube.com/c/DylanIsInTrouble/videos'
        num_videos=10

        channel_url = 'https://www.youtube.com/c/PewDiePie/videos'

        # Fetch the video titles and links using pytube
        yt = YouTube(channel_url)
        video_list = [{'title': video.title, 'url': video.watch_url} for video in yt.videos[:10]]



        for entry in video_list:
            title = entry.title
            video_url = entry.link
            video_list.append({'title': title, 'url': video_url})

        return video_list

    def get_videos_from_library(self):
        channel_url = 'https://www.youtube.com/c/DylanIsInTrouble/videos'
        c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')

        #video_list = [v.title for v in c.videos[:10]]

        video_list = []
        for v in c.videos[:10]:
            video_list.append(v.title)
            print(v.title)

        return video_list

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        # gamespages = self.get_children().live().order_by('-first_published_at')
        # context['gamespages'] = gamespages


        newest_videos = self.get_videos_from_library()


        my_books = newest_videos
        context['books_list'] = my_books

        return context