from scene_detector import get_scenes
from frame_extractor import extract_keyframes
from get_frames_position import get_frames_position
import json

video_path = "./videos/ed_ad.mp4"
keyframes_path = "./keyframes"

scene_list = get_scenes(video_path)
print(scene_list)

scene_data_okd = [
    {
        "scene_id": i,
        "timestamp_start": scene[0].get_timecode(),
        "timestamp_end": scene[1].get_timecode(),
        "frame_start": scene[0].get_frames(),
        "frame_end": scene[1].get_frames(),
    }
    for i, scene in enumerate(scene_list)
]
print("got scenes")

extract_keyframes(video_path, keyframes_path)
print("extracted")

keyframes_position = get_frames_position(video_path, keyframes_path)

print([(i,j) for i,j in keyframes_position])
file_name = 'scene_data.json'

# # Dumping the scene_data object to a JSON file
# with open(file_name, 'w') as file:
#     json.dump(scene_data, file, indent=4)

def get_images_in_scene(keyframes_position, frame_start, frame_end):
    images_in_scene = []
    for key, value in keyframes_position.items():
        if key > frame_start and key < frame_end:
            images_in_scene.append(value)
        if key > frame_end:
            break
    return images_in_scene

scene_data = []
for i, scene in enumerate(scene_list):
    frame_start = scene[0].get_frames()
    frame_end = scene[1].get_frames()
    images_in_scene = get_images_in_scene(keyframes_position, frame_start, frame_end)
    
    scene_data.append(
        {
        "scene_id": i,
        "timestamp_start": scene[0].get_timecode(),
        "timestamp_end": scene[1].get_timecode(),
        "frame_start": scene[0].get_frames(),
        "frame_end": scene[1].get_frames(),
        "images": images_in_scene
         }
    )