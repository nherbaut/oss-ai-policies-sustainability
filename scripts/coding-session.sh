#!/usr/bin/env bash
# Interactive entrypoint; SQLite and Git/GitHub operations use the Python helper.
set -u
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd -- "$script_dir/.." || exit 1
export PYTHONDONTWRITEBYTECODE=1
if (( $# )); then
    exec python3 "$script_dir/coding_session.py" "$@"
fi
python3 "$script_dir/coding_session.py" protect || exit $?
while true; do
    printf '\n1) Start a coding session\n2) Complete the ongoing session\n3) Publish an unpublished session (automatic draft PR)\n4) Session status\n5) Integrate a PR or coding branch (maintainer)\n6) Synchronize shared theory into the ongoing session\nq) Quit\n'
    read -r -p 'Choose: ' choice || exit 0
    case "$choice" in
        1) python3 "$script_dir/coding_session.py" start ;;
        2) python3 "$script_dir/coding_session.py" finish ;;
        3) python3 "$script_dir/coding_session.py" request-merge ;;
        4) python3 "$script_dir/coding_session.py" status ;;
        5) read -r -p 'PR number or coding/... branch: ' target || exit 0
           case "$target" in
               coding/*) python3 "$script_dir/coding_session.py" integrate --branch "$target" ;;
               *) python3 "$script_dir/coding_session.py" integrate "$target" ;;
           esac ;;
        6) python3 "$script_dir/coding_session.py" sync ;;
        q|Q) exit 0 ;;
        *) printf 'Choose 1–6 or q.\n' ;;
    esac
done
