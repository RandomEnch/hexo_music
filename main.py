import os
import json

music_list = os.listdir("./audio")
cover_dict = {}

def create_file():
    for music in music_list:
        music_name = music.split(".")[0]
        # 新建歌词文件，已有则跳过
        if not os.path.exists(f"./lyric/{music_name}.lrc"):
            with open(f"./lyric/{music_name}.lrc", "w", encoding="utf-8") as f:
                f.write("")

        # 新建封面文件，JSON格式【music_name： cover_url】
        if music_name not in cover_dict:
            music_data = {music_name: ""}
            cover_dict.update(music_data)


    with open("./cover.json", "w", encoding="utf-8") as f:
        json.dump(cover_dict, f, ensure_ascii=False, indent=4)


def contact_file():
    song_data = []
    with open("./cover.json", "r", encoding="utf-8") as f:
        cover_data = json.load(f)
    for music in music_list:
        music_name = music.split(".")[0]
        music_data = {
            "name": music_name,
            "artist": "周杰伦",
            "url": f"https://cdn.jsdelivr.net/gh/RandomEnch/music/{music_name}.mp3",
            "cover": cover_data[music_name],
            "lrc": f"https://cdn.jsdelivr.net/gh/RandomEnch/lyric/{music_name}.lrc"
        }
        song_data.append(music_data)

    with open("./song.json", "w", encoding="utf-8") as f:
        json.dump(song_data, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    contact_file()

