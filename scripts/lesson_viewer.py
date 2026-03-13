#!/usr/bin/env python3
import curses
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / '.state' / 'progress.env'
LANG_FILE = ROOT / '.state' / 'lang.env'
LESSON = ROOT / 'lesson.md'
LEVELS = ['L0', 'L1', 'L2', 'L3', 'L4', 'L5']
LEVEL_TITLES_ZH = {
    'L0': 'Vim 新生训练营',
    'L1': '数据考古学家（Terminal + Git）',
    'L2': '环境炼金术（Python venv）',
    'L3': '午夜排障（PDB Debug）',
    'L4': '安全隧道员（SSH）',
    'L5': '双模型调度官（API）',
}
LEVEL_TITLES_EN = {
    'L0': 'Vim Boot Sequence',
    'L1': 'Data Archaeologist (Terminal + Git)',
    'L2': 'Environment Alchemy (Python venv)',
    'L3': 'Midnight Debugging (PDB)',
    'L4': 'SSH Tunnel Basics',
    'L5': 'LLM API Playground',
}
LEVEL_DIRS = {
    'L0': 'L0_vim', 'L1': 'L1_git_terminal', 'L2': 'L2_python_env',
    'L3': 'L3_pdb_debug', 'L4': 'L4_ssh', 'L5': 'L5_model_api'
}


def read_lang():
    if LANG_FILE.exists():
        for line in LANG_FILE.read_text(encoding='utf-8').splitlines():
            if line.startswith('ALGOLAND_LANG='):
                return line.split('=', 1)[1].strip() or 'en'
    return 'en'


def read_progress():
    idx, step = 0, 1
    if STATE.exists():
        for line in STATE.read_text(encoding='utf-8').splitlines():
            if line.startswith('LEVEL_INDEX='):
                idx = int(line.split('=', 1)[1])
            if line.startswith('STEP='):
                step = int(line.split('=', 1)[1])
    return idx, step


def total_steps(level):
    tut = ROOT / 'levels' / LEVEL_DIRS[level] / 'tutorial'
    return len(list(tut.glob('step*.md')))


def bar(cur, total, width=14):
    total = max(total, 1)
    fill = int(cur * width / total)
    return '█' * fill + '·' * (width - fill)


HIDDEN_SECTIONS = {'先安抚一下', '这一步真正考你的是什么', '任务速览'}


def style_for_line(line):
    stripped = line.rstrip('\n')
    if stripped.startswith('# '):
        return ('h1', stripped[2:].strip())
    if stripped.startswith('## '):
        return ('h2', stripped[3:].strip())
    if stripped.startswith('### '):
        return ('h3', stripped[4:].strip())
    if stripped.startswith('> '):
        return ('quote', stripped[2:].strip())
    if stripped.startswith('- '):
        return ('bullet', stripped[2:].strip())
    if stripped[:2].isdigit() and '. ' in stripped:
        head, rest = stripped.split('. ', 1)
        if head.isdigit():
            return ('number', f'{head}. {rest}')
    return ('text', stripped)


def wrap_styled_line(kind, text, width, in_code=False):
    width = max(20, width)
    if in_code:
        chunks = textwrap.wrap(text or ' ', width=width - 4, replace_whitespace=False, drop_whitespace=False) or ['']
        return [('code', '  ' + c) for c in chunks]

    if kind == 'blank':
        return [('blank', '')]
    if kind == 'h1':
        return [('h1', text)]
    if kind == 'h2':
        return [('h2', text)]
    if kind == 'h3':
        wrapped = textwrap.wrap(text, width=width - 2) or ['']
        return [('h3', '▸ ' + wrapped[0])] + [('h3', '  ' + x) for x in wrapped[1:]]
    if kind == 'quote':
        wrapped = textwrap.wrap(text, width=width - 4) or ['']
        return [('quote', '│ ' + x) for x in wrapped]
    if kind == 'bullet':
        wrapped = textwrap.wrap(text, width=width - 4) or ['']
        return [('bullet', '• ' + wrapped[0])] + [('bullet', '  ' + x) for x in wrapped[1:]]
    if kind == 'number':
        wrapped = textwrap.wrap(text, width=width - 4) or ['']
        return [('number', wrapped[0])] + [('number', '   ' + x) for x in wrapped[1:]]

    wrapped = textwrap.wrap(text, width=width - 1, replace_whitespace=False, drop_whitespace=False) or ['']
    return [('text', x) for x in wrapped]


def extract_named_section(text, section_name):
    lines = text.splitlines()
    in_section = False
    buf = []
    for raw in lines:
        line = raw.rstrip('\n')
        if line.startswith('## '):
            section = line[3:].strip()
            if in_section:
                break
            in_section = (section == section_name)
            continue
        if in_section:
            buf.append(line)
    return '\n'.join(buf).strip()


def extract_task_summary(text):
    authored = extract_named_section(text, '任务速览')
    if not authored:
        return []
    out = []
    for raw in authored.splitlines():
        s = raw.strip()
        if not s:
            continue
        if s.startswith('- '):
            out.append(s[2:].strip())
        elif s[:2].isdigit() and '. ' in s:
            out.append(s.split('. ', 1)[1].strip())
        else:
            out.append(s)
        if len(out) >= 4:
            break
    return out[:4]


def render_lesson(width):
    text = LESSON.read_text(encoding='utf-8') if LESSON.exists() else 'lesson.md not found'
    out = []
    in_code = False
    skip_section = False
    for raw in text.splitlines():
        line = raw.rstrip('\n')
        if line.startswith('## '):
            section = line[3:].strip()
            skip_section = section in HIDDEN_SECTIONS
            if skip_section:
                continue
        if skip_section:
            continue
        if line.strip().startswith('```'):
            in_code = not in_code
            continue
        if not line.strip():
            out.append(('blank', ''))
            continue
        if in_code:
            out.extend(wrap_styled_line('code', line, width, in_code=True))
            continue
        kind, content = style_for_line(line)
        out.extend(wrap_styled_line(kind, content, width))
    return out, extract_task_summary(text)


def heading_positions(lines):
    out = []
    for i, (kind, _text) in enumerate(lines):
        if kind in ('h2', 'h3'):
            out.append(i)
    return out


def nearest_prev_heading(headings, scroll):
    prev = 0
    for pos in headings:
        if pos < scroll:
            prev = pos
        else:
            break
    return prev


def nearest_next_heading(headings, scroll):
    for pos in headings:
        if pos > scroll:
            return pos
    return scroll


def draw(stdscr, scroll):
    curses.curs_set(0)
    stdscr.erase()
    h, w = stdscr.getmaxyx()
    lang = read_lang()
    idx, step = read_progress()
    level = LEVELS[min(idx, len(LEVELS) - 1)] if idx < len(LEVELS) else 'DONE'
    total = total_steps(level) if level != 'DONE' else 1
    titles = LEVEL_TITLES_ZH if lang == 'zh' else LEVEL_TITLES_EN
    title = titles.get(level, 'Completed' if lang == 'en' else '全部完成')

    lines, task_summary = render_lesson(max(30, w - 2))
    headings = heading_positions(lines)

    header = f'ALGOLAND · {level} · {title}'
    if lang == 'zh':
        progress = f'步骤 [{bar(min(step, total), total)}] {min(step, total)}/{total}   总进度 [{bar(min(idx, len(LEVELS)), len(LEVELS))}] {min(idx, len(LEVELS))}/{len(LEVELS)}'
        task_top = '任务：' + ('；'.join(task_summary[:2]) if task_summary else '阅读当前讲义并完成本步要求')
        hint = '讲义区：j/k 上下  PgUp/PgDn 翻页  {/} 跳段  g/G 头尾（切回 shell: Ctrl-b ↓）'
    else:
        progress = f'Step [{bar(min(step, total), total)}] {min(step, total)}/{total}   Overall [{bar(min(idx, len(LEVELS)), len(LEVELS))}] {min(idx, len(LEVELS))}/{len(LEVELS)}'
        task_top = 'Task: ' + ('; '.join(task_summary[:2]) if task_summary else 'Read the lesson and finish the current step')
        hint = 'Lesson pane: j/k scroll  PgUp/PgDn page  {/} section jump  g/G top/bottom (Ctrl-b ↓ for shell)'

    summary_lines = []
    if task_summary:
        summary_lines.append(('summary', '任务速览：'))
        for item in task_summary[:3]:
            summary_lines.extend(wrap_styled_line('bullet', item, max(30, w - 4)))
        summary_lines.append(('blank', ''))

    visible_lines = summary_lines + lines
    body_h = max(1, h - 5)
    max_scroll = max(0, len(visible_lines) - body_h)
    scroll = max(0, min(scroll, max_scroll))

    try:
        stdscr.addnstr(0, 0, header, w - 1, curses.A_BOLD)
        stdscr.addnstr(1, 0, progress, w - 1, curses.A_DIM)
        stdscr.addnstr(2, 0, task_top, w - 1, curses.A_BOLD)
        stdscr.hline(3, 0, ord('-'), max(1, w - 1))
    except curses.error:
        pass

    palette = {
        'h1': curses.A_BOLD,
        'h2': curses.A_BOLD,
        'h3': curses.A_BOLD,
        'quote': curses.A_DIM,
        'bullet': curses.A_NORMAL,
        'number': curses.A_NORMAL,
        'text': curses.A_NORMAL,
        'code': curses.A_DIM,
        'blank': curses.A_NORMAL,
        'summary': curses.A_BOLD,
    }

    for row, (kind, text) in enumerate(visible_lines[scroll: scroll + body_h], start=4):
        attr = palette.get(kind, curses.A_NORMAL)
        if kind == 'h2':
            text = f'[{text}]'
        try:
            stdscr.addnstr(row, 0, text, w - 1, attr)
        except curses.error:
            pass

    footer = hint if max_scroll > 0 else '讲义已完整显示；切回 shell 用 Ctrl-b ↓，提交用 ./quest submit'
    try:
        stdscr.addnstr(h - 1, 0, footer, w - 1, curses.A_REVERSE)
    except curses.error:
        pass
    stdscr.refresh()
    return max_scroll, len(summary_lines), headings


def main(stdscr):
    curses.use_default_colors()
    stdscr.keypad(True)
    stdscr.timeout(400)
    scroll = 0
    while True:
        max_scroll, summary_len, headings = draw(stdscr, scroll)
        ch = stdscr.getch()
        if ch == -1:
            continue
        if ch in (ord('j'), curses.KEY_DOWN):
            scroll = min(max_scroll, scroll + 1)
        elif ch in (ord('k'), curses.KEY_UP):
            scroll = max(0, scroll - 1)
        elif ch in (curses.KEY_NPAGE, ord(' ')):
            scroll = min(max_scroll, scroll + max(1, stdscr.getmaxyx()[0] - 6))
        elif ch == curses.KEY_PPAGE:
            scroll = max(0, scroll - max(1, stdscr.getmaxyx()[0] - 6))
        elif ch == ord('g'):
            scroll = 0
        elif ch == ord('G'):
            scroll = max_scroll
        elif ch in (ord('}'), 29):
            body_scroll = max(0, scroll - summary_len)
            nxt = nearest_next_heading(headings, body_scroll)
            scroll = min(max_scroll, nxt + summary_len)
        elif ch in (ord('{'), 27):
            body_scroll = max(0, scroll - summary_len)
            prv = nearest_prev_heading(headings, body_scroll)
            scroll = max(0, prv + summary_len)
        elif ch == curses.KEY_RESIZE:
            pass


if __name__ == '__main__':
    curses.wrapper(main)
