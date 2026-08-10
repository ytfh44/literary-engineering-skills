#!/usr/bin/env python3
"""Rebuild tests/eval_cases.yaml for the v2 taxonomy (22 skills).

Renames keys, redistributes dissolved-skill cases (anti-ai-prose,
sensory-specificity -> narrator-intervention-abstraction-control;
japanese-viewpoint-engineering -> adverb-particle-viewpoint-engineering),
and adds fresh case sets for the 7 fully new skills.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'v1_eval_cases.yaml'

data = json.loads(SRC.read_text(encoding='utf-8'))
skills = data['skills']

RENAME = {
    'relation-language-audit': 'relation-scaffolding',
    'metaphor-engineering': 'metaphor-audit',
    'verb-engineering-core': 'verb-event-engineering',
    'chinese-event-geometry': 'chinese-derived-event-geometry',
    'english-motion-engineering': 'english-derived-motion-packaging',
    'french-motion-engineering': 'french-derived-motion-packaging',
    'dialogue-voice-integrity': 'dialogue-voice',
    'character-motive-engineering': 'character-motive',
    'sentence-pressure-and-rhythm': 'sentence-pressure',
}
for old, new in RENAME.items():
    skills[new] = skills.pop(old)

# absorbers may not exist in v1 data yet
skills.setdefault('narrator-intervention-abstraction-control', {'should_trigger': [], 'should_not_trigger': [], 'ambiguous': [], 'quality_cases': []})
skills.setdefault('adverb-particle-viewpoint-engineering', {'should_trigger': [], 'should_not_trigger': [], 'ambiguous': [], 'quality_cases': []})

# --- dissolved skills: redistribute into absorbers ---
narrator = skills['narrator-intervention-abstraction-control']
narrator.setdefault('should_trigger', [])
narrator.setdefault('should_not_trigger', [])
narrator.setdefault('ambiguous', [])
narrator.setdefault('quality_cases', [])

for old in ('anti-ai-prose', 'sensory-specificity'):
    c = skills.pop(old)
    for k in ('should_trigger', 'ambiguous'):
        narrator[k] = c[k] + narrator[k]
    narrator['quality_cases'] = c['quality_cases'] + narrator['quality_cases']
    narrator['should_not_trigger'] = c['should_not_trigger'] + narrator['should_not_trigger']
# dedupe while preserving order
for k in narrator:
    seen, out = set(), []
    for item in narrator[k]:
        key = json.dumps(item, ensure_ascii=False) if isinstance(item, dict) else item
        if key not in seen:
            seen.add(key)
            out.append(item)
    narrator[k] = out

particle = skills['adverb-particle-viewpoint-engineering']
jap = skills.pop('japanese-viewpoint-engineering')
for k in ('should_trigger', 'should_not_trigger', 'ambiguous'):
    particle[k] = jap[k] + particle[k]
particle['quality_cases'] = jap['quality_cases'] + particle['quality_cases']
particle['should_trigger'] += [
    '“他看了窗外/他又看了窗外”的话语功能差异。',
    '又/才/也/竟然——保持事件不变，换一个词，读者站位怎么变？',
    '“只”和“还”各自的alternative set是什么？',
    '忽然和ふと：无预谋注意和突然onset是同一个变量吗？',
    'じっと/ちらり/一瞥——注意的持续时间与承诺。',
    '把“才”的threshold功能迁移到英语，不要直译。',
]
particle['ambiguous'] += [
    '方言里“才”可能只是强调，没有threshold内容。',
    '仪式性文本用助词做节奏而非话语功能。',
]
particle['quality_cases'] += [
    {
        'fail': 'rejects 又 as repetition filler',
        'pass': 'identifies recurrence function and demands the prior occurrence be recoverable',
        'prompt': '他又来了。',
    },
    {
        'fail': 'translates 才 as only-now without an expectation',
        'pass': 'asks against whose expectation the event is late',
        'prompt': '他才来了。',
    },
]

# --- relation-scaffolding: add concept/event-link overmarking cases ---
rel = skills['relation-scaffolding']
rel['should_trigger'] += [
    '这段不像小说，像说明文在解释逻辑边（因此可以看出……）。',
    '角色讲话全是“然后……然后……”，是事件链过度标记吗？',
    '“这不仅体现了A，也意味着B”是概念链过度标记吗？',
    '把“从某种意义上说”这类元话语框架找出来。',
]
rel['should_not_trigger'] += [
    '检查作者是否替人物总结心理变化。',
    '人物一开口就像心理咨询公众号。',
]

# --- router quality cases: refresh absorbed-skill names in verdict text ---
router = skills['literary-style-router']
router['quality_cases'] = [
    {
        'fail': 'activates metaphor or rewrites without diagnosis',
        'pass': 'routes primarily to narrator-intervention-abstraction-control, optionally relation-scaffolding',
        'prompt': '这段很AI：她意识到这段关系让自己完成了成长。',
    },
    {
        'fail': 'assumes metaphor by default',
        'pass': 'diagnoses state-label/evidence before choosing narrator-intervention-abstraction-control',
        'prompt': '他很紧张。怎么让它不平？',
    },
]

# --- fresh case sets for the 7 fully new skills ---
new_sets = {
    'property-and-adjective-engineering': {
        'should_trigger': [
            '这段的形容词是不是只在堆情绪？',
            '“阴冷的房间”删掉后损失什么？',
            '分类这个形容词：指称、状态、评价还是情绪？',
            '“高个子男人”里的“高个子”是必要的吗？',
            '检查这些修饰语各自有没有工作。',
            '“荒唐的决定”是谁的判断？',
            '这个形容词和别的机制重复了吗？',
            '“惨白的灯”删掉后医院场景还冷吗？',
        ],
        'should_not_trigger': [
            '统计这篇的“因此”频率。',
            '分析“杀/毙”的角色分配。',
            '只做日语来る/行く视点。',
            '这个比喻的来源域增加了什么？',
            '对白像HR。',
            '句子节奏的信息释放。',
            '人物动机生成器。',
            '给skill包做触发测试。',
        ],
        'ambiguous': [
            '这个形容词既是评价又是指称。',
            '“他很累”可能已经足够——修饰语在哪里？',
            '故意用判断式形容词的叙述者声音。',
            'affective和evaluative的边界。',
        ],
        'quality_cases': [
            {
                'fail': 'deletes 阴冷 because the facts are unchanged',
                'pass': 'classifies affective load and tests whether another mechanism carries the cold',
                'prompt': '他走进阴冷的房间，暖气片是凉的。',
            },
            {
                'fail': 'trims 高个子 as adjective excess',
                'pass': 'tests discriminative function against the referent set before trimming',
                'prompt': '那个高个子男人把钥匙放回桌上。',
            },
        ],
    },
    'naming-and-address-engineering': {
        'should_trigger': [
            '同一人物换成不同称呼会改变什么框架？',
            '“父亲”改“那个男人”——测试关系模型变化。',
            '谁在命名？为什么此刻激活这个身份？',
            '狗/野狗/那畜生/阿黄——叙述者位置怎么变？',
            '这个称呼携带什么知识状态？',
            '称呼没变但关系变了，怎么通过称呼体现？',
            '检查这段的称呼连续性。',
            '换称呼不要为了多样，要看框架有没有变。',
        ],
        'should_not_trigger': [
            '统计关系词。',
            '找比喻。',
            '分析结果补语。',
            '动词角色。',
            '对白语域。',
            '句子节奏。',
            '评测skill。',
            '日语视点。',
        ],
        'ambiguous': [
            '角色故意模仿领导的称呼方式。',
            '正式场合必须用头衔。',
            '孩子对同一人多个称呼。',
            '称呼变化可能只是口误。',
        ],
        'quality_cases': [
            {
                'fail': 'treats the name switch as an inconsistency to fix',
                'pass': 'tests whether the frame (estrangement) moved; keeps the switch if it did',
                'prompt': '女儿叙述里第一次把“父亲”写成“那个男人”。',
            },
            {
                'fail': 'praises word-choice variety across the two names',
                'pass': 'attributes a different narrator position to each naming act',
                'prompt': '阿黄和那畜生是同一只狗。',
            },
        ],
    },
    'predicate-licensing-and-personification': {
        'should_trigger': [
            '“风追着他”为什么成立？',
            '这个名词凭什么承担这个谓词？',
            '门“犹豫”了一下——恢复成本是多少？',
            '比拟的谓词通常要求什么施事？',
            '“城市醒了”的重新分类是什么？',
            '这个越界带来了什么新的事件结构？',
            '“雪把声音接住了”为什么恢复很便宜？',
            '这个拟人失败了，因为要解释才能恢复。',
        ],
        'should_not_trigger': [
            '统计虚词。',
            '找比喻来源域。',
            '人物动机。',
            '日语授受。',
            '对白像HR。',
            '形容词分类。',
            '句子节奏。',
            'skill评测。',
        ],
        'ambiguous': [
            '这可能是比喻而不是谓词授权。',
            '门犹豫——拟人还是幕后人物？',
            '陌生搭配可能是病句。',
            '被动句是责任还是视点。',
        ],
        'quality_cases': [
            {
                'fail': 'praises the crossing as vivid personification',
                'pass': 'reduces to the literal event, prices the borrowed intention, may prefer the force/direction version',
                'prompt': '风追着他跑过巷子。',
            },
            {
                'fail': 'bans the crossing as unnatural',
                'pass': 'notes cheap recovery via relay: the person behind the door hesitates',
                'prompt': '门犹豫了一下才开。',
            },
        ],
    },
    'knowledge-boundaries': {
        'should_trigger': [
            '谁在什么时候知道什么？画这场的知识地图。',
            '角色按错误信念行动——这个误信的起源在哪？',
            '戏剧反讽：读者知道角色不知道。',
            '角色不可能现在知道这个。',
            '这个秘密的持有者是谁？',
            '知识不对称在哪里兑现？',
            '检查知识泄漏：角色行为和他知道的不一致。',
            '隐瞒、披露、误认的时机。',
        ],
        'should_not_trigger': [
            '统计关系词。',
            '比喻审计。',
            '动词承诺。',
            '称呼框架。',
            '对白语域。',
            '句子节奏。',
            '人物动机生成。',
            'skill评测。',
        ],
        'ambiguous': [
            '角色知道但不会说（语域问题）。',
            '全家共享的误信。',
            '有限叙述者可能出错。',
            '猜测与知道的边界。',
        ],
        'quality_cases': [
            {
                'fail': 'treats it as a simple suspense statement',
                'pass': 'asks for the evidence that makes the asymmetry real and names the payment scene',
                'prompt': '他不知道妻子已经知道了。',
            },
            {
                'fail': 'adds mystery for its own sake',
                'pass': 'checks the misbelief origin: he locked it from inside',
                'prompt': '他以为门锁着。',
            },
        ],
    },
    'social-naming-relation-maps': {
        'should_trigger': [
            '画全文的称呼地图：谁用什么称呼谁，什么时候。',
            '李叔→老李→李建国——这个关系弧是什么？',
            '谁有资格用什么称呼？不对称编码了什么？',
            '这个称呼改变是在哪一场变得合法？',
            '十年没变的称呼说明什么？',
            '用地图决定下一场的称呼。',
            '故意破坏称呼法则作为这一场的事件。',
            '散会后他叫“小王”——权限被拒绝。',
        ],
        'should_not_trigger': [
            '只分析这一句的称呼框架。',
            '统计关系词。',
            '比喻。',
            '人物动机。',
            '日语视点。',
            '对白HR。',
            '节奏。',
            '知识边界。',
        ],
        'ambiguous': [
            '单次称呼和全局地图的界限。',
            '正式场合头衔是角色扮演。',
            '故意误称是冲突。',
            '全文统一使用名字是设计。',
        ],
        'quality_cases': [
            {
                'fail': 'fixes the two names as an inconsistency',
                'pass': 'reads the permission change as the event and plots the arc',
                'prompt': '她叫他李叔。第七年，他第一次说：“叫我老李就行。”',
            },
            {
                'fail': 'advises using the formal title',
                'pass': 'reads the refusal of unearned familiarity as the move',
                'prompt': '散会后，他叫住她：“小王。”她没回头。',
            },
        ],
    },
    'corpus-convergence-audit': {
        'should_trigger': [
            '这些输出词都不同，但感觉是同一个作者。',
            '检测operation骨架的重复，不要看词汇。',
            '给这段做operation trace。',
            '转移矩阵里哪个op总跟在哪个后面？',
            '开头策略分布。',
            '收尾策略分布。',
            '事件化率是多少？',
            '抽象/证据交替的节奏。',
        ],
        'should_not_trigger': [
            '只改这一段。',
            '找比喻。',
            '统计n-gram词面复现。',
            '单变量diff。',
            '动词角色。',
            '称呼框架。',
            '句子节奏。',
            '评测skill触发。',
        ],
        'ambiguous': [
            '体裁本身有固定op序列。',
            '作者签名和模板的界限。',
            '主题组合作品的共享骨架。',
            '词汇复现和操作复现混合。',
        ],
        'quality_cases': [
            {
                'fail': 'reports no lexical repetition so no problem',
                'pass': 'detects the shared operation skeleton and reports coverage',
                'prompt': '两篇短文无共享词，但都走“感官异常→注意转移→事件化→开放结尾”。',
            },
            {
                'fail': 'flags the genre skeleton as a template defect',
                'pass': 'distinguishes genre mandate from author-level tic',
                'prompt': '推理小说都有线索→误导→揭示。',
            },
        ],
    },
    'literary-strategy-controller': {
        'should_trigger': [
            '前面700字已经六次事件化了，这次还事件化吗？',
            '边际效用评估：这个操作现在是边际最优吗？',
            '连续六个局部正确选择变成了一种文风。',
            '记录文档状态再决定下一步。',
            '重复必须改变作品状态——这是motif还是模板？',
            '不要随机换风格，按状态适应。',
            '这个veto的理由是什么？',
            '全文修订前先建立基线状态。',
        ],
        'should_not_trigger': [
            '只改一个词。',
            '统计关系词。',
            '比喻审计。',
            '单变量A/B。',
            '人物动机。',
            '日语视点。',
            '对白HR。',
            '短段落单句问题。',
        ],
        'ambiguous': [
            '段落很短，要不要控制器？',
            '刻意的仪式性重复。',
            'motif和模板的界限。',
            '体裁规范本身就是重复。',
        ],
        'quality_cases': [
            {
                'fail': "applies the local evidence rule again (show-don't-tell)",
                'pass': 'keeps the direct label as the marginal best move (contrast value)',
                'prompt': '700字里已有六次心理状态用动作表达，这句“他很紧张”怎么处理？',
            },
            {
                'fail': 'deletes the third occurrence as repetition',
                'pass': 'checks motif payoff: does this occurrence change the work state?',
                'prompt': '同一意象第三次出现。',
            },
        ],
    },
}
for name, c in new_sets.items():
    skills[name] = c

data['principles'] = [
    'route_by_mechanism_not_adjective',
    'frequency_is_alarm_not_verdict',
    'transfer_operation_not_costume',
    'one_variable_per_minimal_pair',
    'labels_are_observations_not_character_parameters',
    'rule_strength_decreases_with_depth',
    'repetition_must_change_work_state',
]
data['version'] = 2

(ROOT / 'tests' / 'eval_cases.yaml').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Wrote {len(skills)} skills; {sum(len(v["should_trigger"]) for v in skills.values())} ST prompts total')
