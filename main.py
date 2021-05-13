import argparse
import datetime
import logging

from modules import Hoge, Fuga


parser = argparse.ArgumentParser(description="logger のデモスクリプトです")
parser.add_argument(
    "-f",
    "--outputLogFile",
    help="指定時 log 出力をファイルに行う",
    action="store_true")

args = parser.parse_args()

logger = logging.getLogger(__name__)

# logging 設定
# NOTE: こいつがメインスクリプトなので、"メインスクリプトでのみ" logger の設定を行っていきます
#       メインスクリプト = 実行するスクリプト
#       `$ python main.py` で指定するファイル
#       逆にそれ以外の import して使うようなモジュールやライブラリに関しては logger はひたすらロギングする役割です
#       ロギングは各モジュールから行われますが、それが実行時にどういう出力になるのかは
#       以下メインスクリプトで行っている logging の設定によって変わってきます

# 出力されるログのフォーマットのフォーマット指定
# 詳しくはドキュメント参照してください
log_format = "%(asctime)s [%(levelname)s] %(name)s : %(message)s"

# 実行時の引数で `-f` または `--outputLogFile` が指定されている場合はログ出力は ./logs/ に行い、
# そうでない場合は標準出力にログ出力を行う
if args.outputLogFile:
    # 出力するログファイル名
    # logs/{yyyymmdd}.log に出力されます
    log_filename = f'logs/{datetime.date.today().strftime("%Y%m%d")}.log'
    # Level >= DEBUG のログを出力
    # 実部ライブラリを多く使うようになってくると DEBUG から出力してるとログが出すぎてワケワカメになりがち
    logging.basicConfig(
        filename=log_filename, format=log_format, level=logging.DEBUG)
else:
    # Level >= DEBUG のログを出力
    # 実部ライブラリを多く使うようになってくると DEBUG から出力してるとログが出すぎてワケワカメになりがち
    logging.basicConfig(format=log_format, level=logging.DEBUG)

# module 毎に出力したい logLevel を設定しています
# NOTE: 問答無用で「DEBUG 以上を出力したい!!」って場合は
#       先程の `logging.basicConfig()` に対する `level=logging.DEBUG` の指定だけで十分です
#       「moduleA は DEBUG 以上のログを出したいけど moduleB は WARN 以上だけで良い」
#       みたいな時にこの設定をしていきます
module_levels = {
    # hoge スクリプトは Level >= INFO のログを出力
    "hoge": logging.INFO,
    # fuga スクリプトは Level >= WARN のログを出力
    "fuga": logging.WARN,
}
for module, level in module_levels.items():
    logging.getLogger(module).setLevel(level=level)


def handler():
    logger.info("begining script.")

    logger.debug("↓↓↓ Hoge のインスタンスを生成 (Level >= INFO のログを出力) ↓↓↓")
    Hoge()
    logger.debug("↓↓↓ Fuga のインスタンスを生成 (Level >= WARN のログを出力) ↓↓↓")
    Fuga()
    logger.info("finished script.")


if __name__ == '__main__':
    handler()
