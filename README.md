# mp4 to gif
This app (no GUI, this is a CLI app) will convert mp4 files to gifs.
## Usage
Example on WSL2: ```python3 mp4_to_gif.py -src /mnt/e/drive/documents -dst /mnt/e/drive/compressed -d```
CLI Argument | Short | Description |
--- | --- | --- | 
src | N/A (positional) | The directory where to find the files (or just an mp4 file).|
dst | N/A (positional) | The directory where to put the compressed folders.|
--delete | -del | If this flag is used, original files will be delete if the convertion is successful |
