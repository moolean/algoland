#!/usr/bin/env python3
import os
import sys
import time
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / '.state' / 'progress.env'
LESSON = ROOT / 'lesson.md'
LEVELS = ['L0','L1','L2','L3','L4','L5']
LEVEL_TITLES = {
    'L0':'Vim 新生训练营',
    'L1':'数据考古学家（Terminal + Git）',
    'L2':'环境炼金术（Python venv）',
    'L3':'午夜排障（PDB Debug）',
    'L4':'安全隧道员（SSH）',
    'L5':'双模型调度官（API）',
}
LEVEL_DIRS = {
    'L0':'L0_vim','L1':'L1_git_terminal','L2':'L2_python_env','L3':'L3_pdb_debug','L4':'L4_ssh','L5':'L5_model_api'
}


def read_progress():
    idx, step = 0, 1
    if STATE.exists():
        for line in STATE.read_text().splitlines():
            if line.startswith('LEVEL_INDEX='): idx = int(line.split('=',1)[1])
            if line.startswith('STEP='): step = int(line.split('=',1)[1])
    return idx, step


def total_steps(level):
    tut = ROOT / 'levels' / LEVEL_DIRS[level] / 'tutorial'
    return len(list(tut.glob('step*.md')))


def bar(cur, total, width=22):
    total = max(total,1)
    fill = int(cur*width/total)
    return '█'*fill + '·'*(width-fill)


def color(code, s):
    return f'\033[{code}m{s}\033[0m'


def fit_lines(text, width, max_lines):
    import textwrap
    out=[]
    for raw in text.splitlines():
        if not raw.strip():
            out.append('')
            continue
        wrapped = textwrap.wrap(raw, width=width, replace_whitespace=False, drop_whitespace=False)
        out.extend(wrapped or [''])
        if len(out) >= max_lines:
            break
    return out[:max_lines]


def parse_lesson_sections(text):
    sections = {}
    current = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith('## '):
            current = line[3:].strip()
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(line)
    return {k: '\n'.join(v).strip() for k, v in sections.items()}


def first_bullets(block, limit=4):
    items = []
    for line in block.splitlines():
        s = line.strip()
        if s.startswith('- '):
            items.append(s[2:].strip())
        elif s[:2].isdigit() and '. ' in s:
            items.append(s.split('. ', 1)[1].strip())
        if len(items) >= limit:
            break
    return items


def first_code_block(block):
    lines = block.splitlines()
    inside = False
    buf = []
    for line in lines:
        if line.strip().startswith('```'):
            if inside:
                break
            inside = True
            continue
        if inside:
            buf.append(line)
    return '\n'.join(buf).strip()


def pick_goal(block):
    bullets = first_bullets(block, limit=3)
    return bullets if bullets else [ln.strip() for ln in block.splitlines() if ln.strip()][:3]


def print_card(title, lines, width=68, color_code='1;36'):
    print(color(color_code, f'┌─ {title} ' + '─' * max(1, width - len(title) - 4)))
    for raw in lines:
        print(raw)
    print(color(color_code, '└' + '─' * max(1, width - 1)))


def main():
    once = '--once' in sys.argv
    while True:
        cols, rows = shutil.get_terminal_size((120, 40))
        idx, step = read_progress()
        level = LEVELS[min(idx, len(LEVELS)-1)] if idx < len(LEVELS) else 'DONE'
        total = total_steps(level) if level != 'DONE' else 1
        lesson = LESSON.read_text(encoding='utf-8') if LESSON.exists() else 'lesson.md not found'
        sections = parse_lesson_sections(lesson)

        print('\033[H\033[2J', end='')
        print(color('1;36', '╔════════════════════════════════════════════════════════════════════╗'))
        print(color('1;36', '║ ') + color('1;35', 'TERMINAL QUEST · Live Teaching Dashboard'.ljust(58)) + color('1;36', ' ║'))
        print(color('1;36', '╚════════════════════════════════════════════════════════════════════╝'))
        title = LEVEL_TITLES.get(level, '全部完成')
        print(f"{color('1;33','[关卡]')} {level} · {title}")
        print(f"{color('1;33','[步骤]')} [{bar(min(step,total), total)}] {min(step,total)}/{total}")
        print(f"{color('1;33','[总进度]')} [{bar(min(idx, len(LEVELS)), len(LEVELS))}] {min(idx, len(LEVELS))}/{len(LEVELS)}")
        print(color('38;5;245', '─'*min(cols, 68)))

        comfort = sections.get('先安抚一下', '')
        topic = sections.get('这一步你在学什么', '')
        concepts = sections.get('核心概念', '')
        task = sections.get('本步任务', '')
        selfcheck = sections.get('自检', '')

        max_width = max(40, cols - 4)
        remaining = max(10, rows - 9)

        if comfort:
            comfort_lines = fit_lines(' '.join([x.strip() for x in comfort.splitlines() if x.strip()]), max_width, 4)
            print_card('先安抚一下', comfort_lines, width=min(cols, 68), color_code='1;32')
            remaining -= len(comfort_lines) + 2

        if topic and remaining > 6:
            topic_lines = fit_lines(' '.join([x.strip() for x in topic.splitlines() if x.strip()]), max_width, 4)
            print_card('这一步在学什么', topic_lines, width=min(cols, 68), color_code='1;36')
            remaining -= len(topic_lines) + 2

        if concepts and remaining > 8:
            concept_items = first_bullets(concepts, limit=4)
            if not concept_items:
                concept_items = [ln.strip() for ln in concepts.splitlines() if ln.strip()][:4]
            concept_lines = [f'  • {item}' for item in concept_items]
            print_card('核心概念', concept_lines, width=min(cols, 68), color_code='1;35')
            remaining -= len(concept_lines) + 2

        if task and remaining > 8:
            goals = pick_goal(task)
            goal_lines = [f'  • {item}' for item in goals]
            print_card('你的任务目标', goal_lines, width=min(cols, 68), color_code='1;33')
            remaining -= len(goal_lines) + 2

        code = first_code_block(selfcheck or lesson)
        if code and remaining > 6:
            sample_lines = ['  ' + ln for ln in code.splitlines()[:4]]
            print_card('自检时可以先看', sample_lines, width=min(cols, 68), color_code='1;34')
            remaining -= len(sample_lines) + 2

        footer = [
            '  lesson.md 里有完整讲义；下半屏是真实终端。',
            '  常用路径：lab/   out/   lesson.md',
            '  常用命令：./quest submit   ./quest status',
        ]
        print_card('操作区提示', footer, width=min(cols, 68), color_code='38;5;245')
        if once:
            break
        time.sleep(1.0)

if __name__ == '__main__':
    main()
