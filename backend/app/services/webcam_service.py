import cv2
import os
from datetime import datetime
import threading
import time

class WebcamService:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.running = False

        if not self.cap.isOpened():
            self.cap = None
            return

        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        os.makedirs("app/recordings", exist_ok=True)

        filename = datetime.now().strftime("recording_%Y%m%d_%H%M%S.mp4")
        self.video_path = f"app/recordings/{filename}"

        self.writer = cv2.VideoWriter(
            self.video_path,
            cv2.VideoWriter_fourcc(*"mp4v"),
            20,
            (width, height)
        )

    def start(self, detect_callback):
        self.running = True

        def loop():
            while self.running:
                ret, frame = self.cap.read()
                if not ret:
                    break

                self.writer.write(frame)
                detect_callback(frame)

                time.sleep(0.05)  # ~20 FPS

        threading.Thread(target=loop, daemon=True).start()

    def stop(self):
        self.running = False
        time.sleep(0.2)

        if self.cap:
            self.cap.release()
        if self.writer:
            self.writer.release()