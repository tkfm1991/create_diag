import argparse
import csv


def target_list(target):
    """ターゲットを抽出
    arg:
        target[str]: ホスト名
    return:
        neighbor_list[list(str)]: 隣接情報のリスト
    """
    neighbor_list = []
    with open('static/resource/diag.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if target in row[0]:
                neighbor_list.append(row)

    return neighbor_list


def create_cli_diag(neighbor_list):
    """ネイバー情報からCLIで構成図を作成
    arg:
        neighbor_list[list(str)]: 隣接情報のリスト
    return:
        diag_list[list(str)]: 構成図のリスト
    """
    diag_list = []
    for row in neighbor_list:
        path = f'{row[0]}[{row[1]}] ----- [{row[3]}]{row[2]}'
        diag_list.append(path)

    return diag_list


def show_cli_diag(diag_list):
    """構成図の表示
    args:
        diag_list[list(str)]: 構成図のリスト
    """
    print('\n===== 構成図 =====')
    for line in diag_list:
        print(line)

    print('\n=================')


def setting_parser():
    """パーサーの設定
    return:
        parser.parse_args(): 設定した引数
    """
    parser = argparse.ArgumentParser(description='構成図作成ツール')
    parser.add_argument('hostname', help='ホスト名')
    return parser.parse_args()


if __name__ == '__main__':
    args = setting_parser()
    target = args.hostname
    neighbor_list = target_list(target)
    diag_list = create_cli_diag(neighbor_list)
    show_cli_diag(diag_list)
