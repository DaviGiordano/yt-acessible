from scenedetect import SceneManager, open_video, AdaptiveDetector

def get_scenes(video_path):
    
    video = open_video(video_path)
    scene_manager = SceneManager()
    scene_manager.add_detector(AdaptiveDetector())
    scene_manager.detect_scenes(video)

    return scene_manager.get_scene_list()