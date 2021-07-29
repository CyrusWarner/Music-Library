from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # read_only_fields = ("likes",)
        fields = ["id", "title", "artist", "album", "release_date", "do_you_like_the_song", "likes", "genre"]
