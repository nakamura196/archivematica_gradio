# convert

```bash
ffmpeg -i demo.mov demo.mp4
```

```bash
ffmpeg -i demo.mov -r 5 -filter:v "setpts=0.2*PTS" demo.gif
```
