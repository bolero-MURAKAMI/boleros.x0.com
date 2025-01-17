# モジュール宣言/変数初期化
use strict;
my %cf;
#┌─────────────────────────────────
#│ DreamCounter : init.cgi - 2011/09/27
#│ Copyright (c) KentWeb
#│ http://www.kent-web.com/
#└─────────────────────────────────
$cf{version} = 'DreamCounter v4.1';
#┌─────────────────────────────────
#│ [注意事項]
#│ 1. このスクリプトはフリーソフトです。このスクリプトを使用した
#│    いかなる損害に対して作者は一切の責任を負いません。
#│ 2. 設置に関する質問はサポート掲示板にお願いいたします。
#│    直接メールによる質問は一切お受けいたしておりません。
#└─────────────────────────────────
#
# [ タグの書き方の例 ]
#
#  ・カウンタ <img src="http://〜/dream.cgi?id=[ログID名]">
#  ・時刻表示 <img src="http://〜/dream.cgi?mode=time">
#  ・カレンダ <img src="http://〜/dream.cgi?mode=date">
#  ・ファイルの更新時間
#             <img src="http://〜/dream.cgi?file=/home/〜/index.html">
#             [注意] "/home/〜/index.html" の部分はフルパス指定
#
#  * 応用例 (ログID名を index と仮定)
#    1.画像を変更するとき：(以下はgif2ディレクトリの画像指定例)
#      <img src="http://〜〜/count/dream.cgi?id=index&gif=2">
#    2.数字をランダムに表示するとき：
#      <img src="http://〜〜/count/dream.cgi?mode=rand">
#    3.カウンタ桁数を7桁にするとき：
#      <img src="http://〜〜/count/dream.cgi?id=index&fig=7">

#===========================================================
# ■ 基本設定
#===========================================================

# 管理パスワード（英数字で指定）
$cf{password} = '7344';

# 画像連結モジュール
# 0 : gifcat.pl
# 1 : Image-Magick（サーバにインストールされている必要あり）
$cf{image_pm} = 0;

# IPアドレスのチェック (0=no 1=yes) 
#  → yesの場合連続したIPアドレスはカウントアップしない
$cf{ip_chk} = 0;

# ログを置くサーバディレクトリ
# → 現行ディレクトリであればこのままでよい
$cf{datadir} = './data';

# 他サイトからアクセスを排除
#  → 排除する   : dream.cgiを設置するURLを http://から記述
#  → 排除しない : 何も記述しない（このまま）
#   注：ただし「排除する」とした場合、設置するサーバや利用者のブラウザ
#       によっては自サイトからでもアクセスを排除する場合があります。
$cf{base_url} = "";

# 画像のあるデフォルト（初期値）のディレクトリ指定【サーバパス】
$cf{gifdir} = './gif1';

# 桁数指定の最大値（セキュリティ対策）
#   → これを超える桁数は指定しても無視されます。
$cf{maxfig} = 12;

# 本体CGI【URLパス】
$cf{dream_cgi} = './dream.cgi';

# 管理CGI【URLパス】
$cf{admin_cgi} = './admin.cgi';

# gifcat.plのパス【サーバパス】
$cf{gifcat_pl} = './lib/gifcat.pl';

# magick.plのパス【サーバパス】
$cf{magick_pl} = './lib/magick.pl';

# 管理画面の最大受理サイズ（バイト）
$cf{maxdata} = 10240;

#===========================================================
# ■ 設定完了
#===========================================================

# 設定値を返す
sub init { return %cf; }


1;

