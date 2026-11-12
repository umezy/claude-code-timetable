# session-mark-waiting・session-mark-done 用: いまのセッション名の頭の印を付け替えた名前を 1 行で出す。
# 名前はデスクトップアプリの保存ファイルから読む（get_session を呼ぶ往復を省くため）。
# 保存ファイルの場所は Windows（%APPDATA%\Claude\claude-code-sessions）で確かめた物。
# 見つからないとき（Windows 以外など）は、Claude に get_session で取り直すよう 1 行を出す。
import glob, json, os, sys

MARKS = {"w": "⏸️", "d": "✅"}
OLD = ("⏸️", "⏸", "\ufe0f", "✅")  # 付け替える前に外す印（\ufe0f は絵文字の異体字セレクタ）
sys.stdout.reconfigure(encoding="utf-8")
mark = MARKS[sys.argv[1]]
sid = os.environ.get("CLAUDE_CODE_HOST_SESSION_ID", "")
appdata = os.environ.get("APPDATA", "")
hits = glob.glob(os.path.join(appdata, "Claude", "claude-code-sessions", "*", "*", sid + ".json")) if sid and appdata else []
try:
    title = json.load(open(hits[0], encoding="utf-8"))["title"]
except Exception:
    print(f"（読めなかった。get_session の self で今の名前を取り、頭の ⏸・✅ を外して {mark} を付けた名前を使う）")
    sys.exit()
changed = True
while changed:
    changed = False
    for m in OLD:
        if title.startswith(m):
            title = title[len(m):]
            changed = True
print(mark + title)
