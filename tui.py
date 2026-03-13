#!/usr/bin/env python3
import curses
import os
import subprocess
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATE_DIR = ROOT / '.state'
LESSON = ROOT / 'lesson.md'
OUTPUT_LOG = STATE_DIR / 'tui.log'
PROGRESS = STATE_DIR / 'progress.env'
LEVELS = ['L0', 'L1', 'L2', 'L3', 'L4', 'L5']
LEVEL_TITLES = {
    'L0': 'Vim 新生训练营',
    'L1': '数据考古学家（Terminal + Git）',
    'L2': '环境炼金术（Python venv）',
    'L3': '午夜排障（PDB Debug）',
    'L4': '安全隧道员（SSH）',
    'L5': '双模型调度官（API）',
}


def read_progress():
    level_index, step = 0, 1
    if PROGRESS.exists():
        for line in PROGRESS.read_text().splitlines():
            if line.startswith('LEVEL_INDEX='):
                level_index = int(line.split('=', 1)[1])
            elif line.startswith('STEP='):
                step = int(line.split('=', 1)[1])
    return level_index, step


def total_steps(level: str) -> int:
    tut = ROOT / 'levels' / {
        'L0': 'L0_vim',
        'L1': 'L1_git_terminal',
        'L2': 'L2_python_env',
        'L3': 'L3_pdb_debug',
        'L4': 'L4_ssh',
        'L5': 'L5_model_api',
    }[level] / 'tutorial'
    return len(list(tut.glob('step*.md')))


def progress_bar(cur, total, width=18):
    total = max(total, 1)
    fill = int(cur * width / total)
    return '█' * fill + '·' * (width - fill)


def append_log(text: str):
    OUTPUT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_LOG.open('a', encoding='utf-8') as f:
        f.write(text.rstrip() + '\n')


def run_and_capture(cmd: str):
    proc = subprocess.run(cmd, shell=True, cwd=ROOT, text=True, capture_output=True)
    out = f"$ {cmd}\n{proc.stdout}{proc.stderr}"
    append_log(out)
    return proc.returncode, out


def run_interactive(stdscr, cmd: str):
    curses.endwin()
    os.system('clear')
    print(f'>>> Running: {cmd}\n')
    rc = subprocess.call(cmd, shell=True, cwd=ROOT)
    print(f"\n[exit code: {rc}] Press Enter to return to Terminal Quest...")
    try:
        input()
    except EOFError:
        pass
    stdscr.refresh()
    append_log(f"$ {cmd}\n[interactive command exited with {rc}]\n")
    return rc


def sync_materials():
    subprocess.run('./quest sync', shell=True, cwd=ROOT)


def draw_box(win, y, x, h, w, title=''):
    win.attron(curses.color_pair(1))
    win.border()
    if title:
        win.addnstr(0, 2, f' {title} ', w - 4, curses.color_pair(1) | curses.A_BOLD)
    win.attroff(curses.color_pair(1))


def wrap_lines(text, width):
    lines = []
    for raw in text.splitlines():
        if not raw.strip():
            lines.append('')
            continue
        if raw.startswith('```'):
            lines.append(raw)
            continue
        wrapped = textwrap.wrap(raw, width=width, replace_whitespace=False, drop_whitespace=False)
        lines.extend(wrapped or [''])
    return lines


def render(stdscr, lesson_scroll=0):
    stdscr.erase()
    h, w = stdscr.getmaxyx()
    left_w = max(50, int(w * 0.62))
    right_w = w - left_w - 1
    header_h = 5
    footer_h = 5
    body_h = h - header_h - footer_h

    level_index, step = read_progress()
    level = LEVELS[min(level_index, len(LEVELS)-1)] if level_index < len(LEVELS) else 'DONE'
    if level == 'DONE':
        title = '全部完成'
        total = 1
        current = 1
    else:
        title = LEVEL_TITLES[level]
        total = total_steps(level)
        current = step

    stdscr.attron(curses.color_pair(2) | curses.A_BOLD)
    stdscr.addstr(0, 2, 'TERMINAL QUEST')
    stdscr.attroff(curses.color_pair(2) | curses.A_BOLD)
    stdscr.addstr(1, 2, f'关卡: {level} · {title}')
    stdscr.addstr(2, 2, f'当前步骤: [{progress_bar(min(current, total), total)}] {min(current, total)}/{total}')
    stdscr.addstr(3, 2, f'总体进度: [{progress_bar(min(level_index, len(LEVELS)), len(LEVELS))}] {min(level_index, len(LEVELS))}/{len(LEVELS)}')

    lesson_win = stdscr.derwin(body_h, left_w, header_h, 0)
    out_win = stdscr.derwin(body_h, right_w, header_h, left_w + 1)
    draw_box(lesson_win, 0, 0, body_h, left_w, '教学 / 当前任务')
    draw_box(out_win, 0, 0, body_h, right_w, '最近输出')

    lesson_text = LESSON.read_text(encoding='utf-8') if LESSON.exists() else 'lesson.md not found'
    lesson_lines = wrap_lines(lesson_text, left_w - 4)
    max_scroll = max(0, len(lesson_lines) - (body_h - 2))
    lesson_scroll = max(0, min(lesson_scroll, max_scroll))
    for idx, line in enumerate(lesson_lines[lesson_scroll:lesson_scroll + body_h - 2], start=1):
        lesson_win.addnstr(idx, 2, line, left_w - 4)

    log_text = OUTPUT_LOG.read_text(encoding='utf-8') if OUTPUT_LOG.exists() else '欢迎来到真正的 TUI 模式。\n按 :help 查看命令。'
    log_lines = wrap_lines(log_text, right_w - 4)
    start = max(0, len(log_lines) - (body_h - 2))
    for idx, line in enumerate(log_lines[start:start + body_h - 2], start=1):
        out_win.addnstr(idx, 2, line, right_w - 4)

    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(h - 4, 2, '快捷键: ↑↓滚动教学  |  F5/ctrl-s 提交  |  F6 刷新  |  :命令  |  q 退出')
    stdscr.addstr(h - 3, 2, '可直接输入命令，例如: vim out/hello_vim.txt   或   ls lab')
    stdscr.addstr(h - 2, 2, '> ')
    stdscr.attroff(curses.color_pair(3))
    stdscr.refresh()
    return lesson_scroll


def prompt_command(stdscr):
    h, w = stdscr.getmaxyx()
    curses.echo()
    stdscr.move(h - 2, 4)
    stdscr.clrtoeol()
    cmd = stdscr.getstr(h - 2, 4, w - 6).decode('utf-8').strip()
    curses.noecho()
    return cmd


def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_CYAN, -1)
    curses.init_pair(2, curses.COLOR_MAGENTA, -1)
    curses.init_pair(3, curses.COLOR_YELLOW, -1)
    curses.init_pair(4, curses.COLOR_GREEN, -1)
    sync_materials()
    lesson_scroll = 0
    while True:
        lesson_scroll = render(stdscr, lesson_scroll)
        ch = stdscr.getch()
        if ch in (ord('q'), 27):
            break
        elif ch == curses.KEY_UP:
            lesson_scroll = max(0, lesson_scroll - 1)
        elif ch == curses.KEY_DOWN:
            lesson_scroll += 1
        elif ch in (curses.KEY_F5, 19):
            run_and_capture('./quest submit')
            sync_materials()
        elif ch == curses.KEY_F6:
            sync_materials()
        elif ch in (ord(':'), ord('/')):
            stdscr.addstr(stdscr.getmaxyx()[0] - 2, 2, '> ')
            cmd = prompt_command(stdscr)
            if not cmd:
                continue
            if cmd in ('submit', './quest submit'):
                run_and_capture('./quest submit')
                sync_materials()
            elif cmd in ('status', './quest status'):
                run_and_capture('./quest status')
            elif cmd in ('help', ':help'):
                append_log('可用方式:\n- 直接输入 shell 命令，如 ls lab / cat lesson.md / vim out/file\n- submit 提交当前步骤\n- status 查看进度\n- refresh 刷新材料\n- q 退出 TUI')
            elif cmd in ('refresh', 'sync'):
                sync_materials()
                append_log('已刷新当前材料与视图。')
            else:
                interactive = cmd.startswith('vim ') or cmd.startswith('python -m pdb') or cmd.startswith('less ') or cmd.startswith('ssh ')
                if interactive:
                    run_interactive(stdscr, cmd)
                else:
                    run_and_capture(cmd)
                sync_materials()
        elif ch in (10, 13):
            cmd = prompt_command(stdscr)
            if not cmd:
                continue
            if cmd == 'submit':
                run_and_capture('./quest submit')
                sync_materials()
            else:
                interactive = cmd.startswith('vim ') or cmd.startswith('python -m pdb') or cmd.startswith('less ') or cmd.startswith('ssh ')
                if interactive:
                    run_interactive(stdscr, cmd)
                else:
                    run_and_capture(cmd)
                sync_materials()


if __name__ == '__main__':
    curses.wrapper(main)
