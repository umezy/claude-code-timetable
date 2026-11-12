---
name: session-mark-waiting
description: セッション名の頭に「⏸️」を付ける（他の人の答えや時間を待っていて、進行中の物と分ける印）。メッセージが「ウェイト」「wait」の1語だけのときに使う。音声入力で化けた同じ音の1語（ウエート・ウエイト・上と など）も同じに扱う
allowed-tools:
  - Bash(python ~/.claude/skills/session-mark-waiting/mark.py *)
  - ToolSearch
  - mcp__ccd_session_mgmt__get_session
  - mcp__ccd_session_mgmt__set_session_title
---
新しい名前: !`python ~/.claude/skills/session-mark-waiting/mark.py w`

この名前（コマンドのままなら、実行して出た1行）を mcp__ccd_session_mgmt__set_session_title に session_id "self" で渡す。出た1行が「（読めなかった。…）」なら、それは名前ではないので、書いてあるとおり get_session で今の名前を取り、作り直した名前を渡す。ツールが未読み込みなら ToolSearch の select: で読む（コマンドと同時に呼ぶ）。返事は新しい名前を1行だけ。
