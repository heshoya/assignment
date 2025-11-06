from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput
import jetson_inference
import jetson_utils

net = detectNet("ssd-mobilenet-v2",threshold=0.5)
camera = videoSource("/dev/video0")
display = videoOutput("display://0") # 'my_video.mp4' for file
while display.IsStreaming():
    img = camera.Capture()
    if img is None: #capture timeout
        continue
    detections = net.Detect(img)
    print(detections)
    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
