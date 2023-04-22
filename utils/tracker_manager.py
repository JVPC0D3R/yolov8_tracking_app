class TrackerManager:
    def __init__(self, max_missing_frames):
        self.tracks = {}
        self.max_frames = max_missing_frames

    def update(self, tracker_outputs):
        new_tracks = {}
        for track_id, bbox in tracker_outputs:
            if track_id in self.tracks:
                missing_frames = self.tracks[track_id]['missing_frames']
                new_tracks[track_id] = {'bbox': bbox, 'missing_frames': max(0, missing_frames - 1)}
            else:
                new_tracks[track_id] = {'bbox': bbox, 'missing_frames': 0}

        for track_id in self.tracks:
            if track_id not in new_tracks:
                missing_frames = self.tracks[track_id]['missing_frames'] + 1
                if missing_frames <= self.max_frames:
                    new_tracks[track_id] = {'bbox': self.tracks[track_id]['bbox'], 'missing_frames': missing_frames}

        self.tracks = new_tracks

    def get_tracks(self):
        return self.tracks