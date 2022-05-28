import argparse, os
from glob import glob
from moviepy.editor import VideoFileClip



def folder_format_validator(temp: str) -> str:
    isMp4 = temp.endswith(".mp4") and os.path.isfile(temp)
    isFolder = os.path.isdir(temp)

    if isMp4 or isFolder:
        return temp
    else:
        raise argparse.ArgumentTypeError("Not a folder or an mp4 file")



def parse_arguments():
    parser = argparse.ArgumentParser(description="Optional app description")
    parser.add_argument("src", type=folder_format_validator, help="The folder where the mp4 files are (or an mp4 file)")
    parser.add_argument("dst", type=folder_format_validator, help="The folder where to put the .gif file")
    parser.add_argument("-del", "--delete", action="store_true", help="Use this flag to delete the original files after a successful convertion to gif")
    args = parser.parse_args()
    abs_src = os.path.abspath(args.src)
    abs_dst = os.path.abspath(args.dst)
    delete = bool(args.delete)
    return abs_src, abs_dst, delete



def to_gif(filename: str, dst_folder: str, delete: bool):
    try:
        videoClip = VideoFileClip(filename)
        basename = os.path.basename(filename)
        gifname = os.path.join(dst_folder, basename[:-4] + ".gif")
        videoClip.write_gif(gifname)
        if delete:
            os.remove(filename)
    except Exception as e:
        print("File " + filename + " could not be converted to gif")
        print(e)



def main():
    src, dst, delete = parse_arguments()
    dir_list = []
    file_list = []

    if  os.path.isdir(src):
        dir_list.append(src)
    else:
        file_list.append(src)

    while dir_list or file_list:
        if file_list:
            head = file_list.pop()
            to_gif(head, dst, delete)
        else:
            glob_pattern = os.path.join(dir_list.pop(), '*')
            files = sorted(glob(glob_pattern), key=os.path.getctime)
            videos = [f for f in files if f.endswith(".mp4")]
            folders = [f for f in files if os.path.isdir(f)]
            file_list.extend(videos)
            dir_list.extend(folders)














if __name__ == "__main__":
    main()