## Streaming frames extraction

=======

## Installing FFMPEG for MacOS
```
brew install ffmpeg
```

## Installing FFMPEG for Ubuntu 16.04
Install the "libav-tools" package:
```
sudo apt-get install libav-tools
```

Then, install FFMPEG by using PPA:
```
sudo add-apt-repository ppa:mc3man/trusty-media
sudo apt-get update
sudo apt-get install ffmpeg gstreamer0.10-ffmpeg
```

Run the "get_frames.py" script with input and fps arguments as in below.
```
python3 get_frames.py <URL streaming directly> <frame / every seconds>
```

## Example
```
python3 get_frames.py http://aldirect.hls.huya.com/huyalive/this_is_test_url.m3u8 1/60
```
- 1/60 is screenshot 1 frame every 60 seconds
