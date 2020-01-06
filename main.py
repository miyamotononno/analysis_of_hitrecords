import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config
import csv

class MySpotify:
  def __init__(self):
    self.username = config.USER_NAME
    self.client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(config.CLIENT_ID, config.CLIENT_SECRET)
    self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
  
  def search_playlists(self, query = ''):
    results = self.sp.search(q=query, type='playlist')['playlists']['items']
    if len(results) == 0:
      return []

    return [ {'playlist_name': item['name'], 'playlist_id': item['id'] } for item in results]

  def _unique(self, l, keyname):
    targets = [item[keyname] for item in l]
    new_targets = list(set(targets))
    new_list = []
    for t in new_targets:
      idx = targets.index(t)
      new_list.append(l[idx])

    return new_list


  def get_tracks_from_playlists(self):
    querys = ['playlist: Japan&playlist: Top', 'playlist: Japan&playlist: 2019']
    results = []
    for q in querys:
      r = self.search_playlists(q)
      results.extend(r)
    
    results = self._unique(results, 'playlist_id')
    tracks = []
    for r in results:
      r  = self.sp.user_playlist(self.username, r['playlist_id'])
      tracks.extend(r['tracks']['items'])
  
    data = []
    for item in tracks:
    
      t_name = item['track']['name']
      t_id = item['track']['id']
      artist = item['track']['artists'][0]['name']
      obj = {
        'track_id': t_id,
        'track_name': t_name,
        'main_artist_name': artist,
        'duration_second': 0,
      }
      data.append(obj)
    
    return data

  def get_audio_details(self):
    data = self.get_tracks_from_playlists()
    data = self._unique(data, 'track_id')
    if len(data) == 0:
      return
    track_ids = [item['track_id'] for item in data]
    audios = []
    uri_ids = []

    for idx, tid in enumerate(track_ids):
      if idx > 0 and idx % 100 == 0:
        ret = self.sp.audio_features(tracks=uri_ids)
        audios.extend(ret)
        uri_ids = []

      uri_ids.append(tid)

    if len(uri_ids) > 0:
      ret = self.sp.audio_features(tracks=uri_ids)
      audios.extend(ret)
      uri_ids = []


    for idx, song in enumerate(audios):
      time = song['duration_ms']
      second = time // 1000
      data[idx]['duration_second'] = second

    return data

  def write_csv(self, header, data):
    with open('data.csv', 'w') as f:
      writer = csv.DictWriter(f, header)
      writer.writeheader()
      writer.writerows(data)

if __name__ == "__main__":
    sp = MySpotify()
    r = sp.get_audio_details()
    sp.write_csv(['track_id', 'track_name', 'main_artist_name', 'duration_second'], r)