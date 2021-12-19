TRAIN_DATASET_PATH = 'train'
TRAIN_TEXT_FILE_NAME = 'train'
VALID_DATASET_PATH = 'validate'
VALID_TEXT_FILE_NAME = 'validate'

import os
from tqdm import tqdm


def create_text_conf_file(dataset_path, text_file_name):
    with open(f"data/{text_file_name}.txt", "w") as text_file:
        print(f'Generating {text_file_name}.txt ...')
        for f in tqdm(os.listdir(f'data/{dataset_path}/')):
            if f.endswith(".jpg"):
                text_file.\
                write(f'data/{dataset_path}/' + f + '\n')
        text_file.close()


def main():
    if os.path.exists(f'./{TRAIN_TEXT_FILE_NAME}.txt'):
        os.remove(f'./{TRAIN_TEXT_FILE_NAME}.txt')
    if os.path.exists(f'./{VALID_TEXT_FILE_NAME}.txt'):
        os.remove(f'./{VALID_TEXT_FILE_NAME}.txt')
    create_text_conf_file(dataset_path=TRAIN_DATASET_PATH,\
    text_file_name=TRAIN_TEXT_FILE_NAME)
    create_text_conf_file(dataset_path=VALID_DATASET_PATH,\
    text_file_name=VALID_TEXT_FILE_NAME)


if __name__ == '__main__':
    main()