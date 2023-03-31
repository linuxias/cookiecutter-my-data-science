import os
import sys
import argparse
import stat

def parse_args():
    parser = argparse.ArgumentParser(
        description= \
            "Create HRM data analysis project template")

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--project_name',
                        required=True,
                        help='Input project name',)
    parser.add_argument('-r', '--root_dir',
                        default=os.getcwd(),
                        help='Root directory path where project created')
    return parser.parse_args()

def make_file_path_list(rootDir):
    file_path_list = []
    file_path_list.append("/README.md")
    file_path_list.append("/data/raw/.gitkeep")
    file_path_list.append("/data/processd/.gitkeep")
    file_path_list.append("/data/interim/.gitkeep")
    file_path_list.append("/models/.gitkeep")
    file_path_list.append("/reports/.gitkeep")
    file_path_list.append("/requirements.txt")
    file_path_list.append("/src/data/make_dataset.py")
    file_path_list.append("/src/features/build_fetures.py")
    file_path_list.append("/src/models/predict_model.py")
    file_path_list.append("/src/models/train.py")
    file_path_list.append("/src/visualization/visualize.py")
    file_path_list = [rootDir + path for path in file_path_list]

    return file_path_list

def make_project(project):
    try:
        os.makedirs(project)
    except OSError as e:
        print("{} is Exists, please check project name", project)

def main():
    args = parse_args()
    project_name = args.project_name
    root_dir = args.root_dir + "/" + project_name
    make_project(root_dir)
    path_list = make_file_path_list(root_dir)

    try:
        for filepath in path_list:
            if os.path.exists(filepath):
                pass
            dirname = os.path.dirname(filepath)
            os.makedirs(dirname, exist_ok=True)
            os.mknod(filepath, 0o0600 | stat.S_IFREG)
    except OSError as e:
        print(e.strerror)


if __name__ == '__main__':
    main()