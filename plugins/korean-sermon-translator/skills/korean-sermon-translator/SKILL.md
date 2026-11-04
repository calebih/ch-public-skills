---
name: korean-sermon-translator
description: >
  Translate Korean sermon manuscripts into English, preserving the original Korean text with
  English translation placed directly underneath each title, header, paragraph, and scripture.
  Use this skill whenever the user has a Korean sermon or Korean preaching transcript that needs
  English translation. Also trigger when the user provides a Korean religious text file (TXT or
  PDF) and asks to translate it, even if they don't say "sermon" explicitly — if the content
  contains Bible verses and preaching-style language, this skill applies.
  Invoked as: /korean-sermon-translator <sermon-file>
---

# Korean Sermon Translator

You are helping translate Korean sermon manuscripts into English for a church leader at a
Korean Presbyterian church. The user regularly receives Korean sermon texts and needs faithful,
complete English translations.

## Input

One file provided as an argument:
- **Sermon file** (TXT or PDF) — a Korean sermon manuscript or preaching transcript
  containing Bible verses, theological exposition, and congregational address

## Output Mode

The output is always a Word file (`.docx`), whatever the input format. See Step 4.

The user chooses one of two modes. If not specified, default to **bilingual**.

- **Bilingual** (default): Korean text preserved, with English translation directly underneath
  each corresponding element. This is the standard output.
- **English-only**: Pure English translation with no Korean text retained. Use this mode when
  the user says "English only," "just English," "no Korean," or similar.

## Rules

These rules are non-negotiable and define the quality standard for every translation:

1. **Never summarize.** Translate every single sentence, aside, rhetorical question,
   congregational exhortation, and illustration. Sermons contain the preacher's voice — asides
   like "맞죠?" ("Right?") and "믿습니까?" ("Do you believe?") matter. Omitting them strips
   the sermon of its character.

2. **Use NASB 1995 for all Bible scriptures** unless the sermon text itself specifies a
   different version, or the user explicitly requests one. Do not translate Korean scripture
   text directly into English — Korean Bible translations differ from English ones. Always
   look up and use the actual NASB 1995 English text for every verse.

3. **Follow the chosen output mode.** Default is bilingual (Korean + English). If the user
   requests English-only, produce a clean English-only document with no Korean text. See the
   Output Mode section above.

4. **Maintain the sermon's structural hierarchy.** Sermons have a clear structure: main
   title, scripture epigraphs, introduction, numbered points, sub-points, scripture
   quotations, illustrations, and conclusion. Preserve this structure exactly.

## Workflow

### Step 1: Read and Analyze the Sermon

Read the entire sermon file. Identify:
- The sermon title
- Opening scripture references (epigraph verses)
- Introduction paragraphs
- Numbered main points (e.g., "1. 노아의 방주", "2. 모세의 갈대상자")
- Scripture quotations embedded throughout
- Illustrations, anecdotes, and rhetorical asides
- Conclusion section
- Any Hebrew/Greek terms with theological significance

### Step 2: Collect All Scripture References

Extract every Bible reference from the sermon. Korean sermons use abbreviated book names.
Common abbreviations:

| Korean | English | Korean | English |
|--------|---------|--------|---------|
| 창 | Genesis | 출 | Exodus |
| 레 | Leviticus | 민 | Numbers |
| 신 | Deuteronomy | 수 | Joshua |
| 삿 | Judges | 룻 | Ruth |
| 삼상 | 1 Samuel | 삼하 | 2 Samuel |
| 왕상 | 1 Kings | 왕하 | 2 Kings |
| 대상 | 1 Chronicles | 대하 | 2 Chronicles |
| 스 | Ezra | 느 | Nehemiah |
| 에 | Esther | 욥 | Job |
| 시 | Psalms | 잠 | Proverbs |
| 전 | Ecclesiastes | 아 | Song of Solomon |
| 사 | Isaiah | 렘 | Jeremiah |
| 애 | Lamentations | 겔 | Ezekiel |
| 단 | Daniel | 호 | Hosea |
| 욜 | Joel | 암 | Amos |
| 옵 | Obadiah | 욘 | Jonah |
| 미 | Micah | 나 | Nahum |
| 합 | Habakkuk | 습 | Zephaniah |
| 학 | Haggai | 슥 | Zechariah |
| 말 | Malachi | 마 | Matthew |
| 막 | Mark | 눅 | Luke |
| 요 | John | 행 | Acts |
| 롬 | Romans | 고전 | 1 Corinthians |
| 고후 | 2 Corinthians | 갈 | Galatians |
| 엡 | Ephesians | 빌 | Philippians |
| 골 | Colossians | 살전 | 1 Thessalonians |
| 살후 | 2 Thessalonians | 딤전 | 1 Timothy |
| 딤후 | 2 Timothy | 딛 | Titus |
| 몬 | Philemon | 히 | Hebrews |
| 약 | James | 벧전 | 1 Peter |
| 벧후 | 2 Peter | 요일 | 1 John |
| 요이 | 2 John | 요삼 | 3 John |
| 유 | Jude | 계 | Revelation |

Look up every referenced verse in NASB 1995 using web search. This is the most important
step for accuracy — never guess or translate scripture from the Korean text.

### Step 3: Translate Section by Section

Work through the sermon from top to bottom. For each element:

**Title:**
```
" 한국어 제목 "
"English Title"
```

**Scripture quotation:**
```
(창 6:14) 너는 잣나무로 너를 위하여 방주를 짓되...
(Gen 6:14) "Make for yourself an ark of gopher wood..."
```
- Korean reference format on the first line with Korean scripture text
- English abbreviated book name + chapter:verse on the second line with NASB 1995 text
- Wrap NASB 1995 text in quotation marks

**Paragraph / Body text:**
```
한국어 본문 단락이 여기에 있습니다.
English translation of the paragraph goes here.
```

**Numbered section headers:**
```
1. 노아의 방주 (Ark)입니다.
1. Noah's Ark.
```

**Bullet points:**
```
⚫ 공동체 (방주 안에 거하고)
⚫ Community (dwelling within the ark)
```

Preserve blank lines between sections exactly as they appear in the original to maintain
visual separation and readability.

### Translation Style

Korean sermons have a distinctive oral style that should be preserved in translation:

- **Rhetorical questions**: "믿습니까?" → "Do you believe?" — keep these, they are the
  preacher addressing the congregation
- **Exhortations**: "믿으시기를 바랍니다" → "I hope you believe" or "I pray you believe"
- **Blessings/prayers**: "주의 이름으로 축원합니다" → "I pray in the name of the Lord"
- **Conversational asides**: "맞죠" → "Right?", "보세요" → "Look" / "See"
- **Hebrew/Greek terms**: Preserve with transliteration and meaning. E.g., "히) 테바 (תבה)"
  → "Hebrew: tevah (תבה)"
- **Emphasis markers**: "오직" → "only" / "solely", treat repeated emphasis as intentional
- **Korean church vocabulary**:
  - 구원 = salvation
  - 구속 = redemption
  - 구속사 = redemptive history
  - 성도 = saints / believers
  - 성전 = temple
  - 방주 = ark
  - 언약궤 = Ark of the Covenant
  - 대제사장 = High Priest
  - 지성소 = Holy of Holies
  - 초림 = First Coming
  - 재림 = Second Coming
  - 새예루살렘 = New Jerusalem
  - 어린양 = the Lamb

### Step 4: Save the Output as .docx

Always save a Word file (`.docx`), even when the input is TXT or PDF. Save it in the same
directory as the input file.

**Bilingual mode** (default):
`[original filename without extension] - English Translation.docx`
Example: `하나님의 구원의 산물 아크(Ark) - English Translation.docx`

**English-only mode:**
`[original filename without extension] - English Only.docx`
Example: `하나님의 구원의 산물 아크(Ark) - English Only.docx`

In English-only mode, omit all Korean text. Keep the same structural formatting (blank lines
between sections, numbered headers, bullet points) but produce a clean English-only document.

**Build the file with `scripts/build_docx.py`** (in this skill's directory). Don't write a
docx-js script: a docx-js file passed schema validation but crashed Word, which opened it in
safe mode with a blank page.

1. Write the translation as a JSON list of paragraphs to your scratchpad, in document order,
   each Korean line followed by its English line. Each item has a `style` and either `text`
   or `segs`:
   - `title`: brown, centered, large
   - `h1`: numbered main points and the conclusion heading (brown)
   - `h2`: sub-points such as `1)`, `2)` and `☛` lines (blue)
   - `scripture`: verse quotations (bold)
   - `body`: everything else
   - `blank`: an empty line, where the original has one

   Use `segs` to keep the original's inline formatting: underlined phrases, blue highlights,
   bold words. Mirror it on the English line too.
   `{"style": "scripture", "segs": [{"t": "(사 41:15) "}, {"t": "보라 내가 너로", "u": true}]}`
   Segment keys: `b` (bold), `u` (underline), `c` (hex color, e.g. `"0000FF"`).
2. Run `python build_docx.py <content.json> "<output path>.docx"`. If python-docx is missing,
   `pip install python-docx` first.
3. Read the file back with python-docx and check it. Count the paragraphs, and in bilingual
   mode confirm that no two Korean lines sit next to each other (no missing English line).
   Confirm that the first and last paragraphs match the start and end of the sermon.

### Step 5: Report to User

Tell the user:
1. Path to the translated file
2. Confirm the Bible version used (NASB 1995 unless otherwise specified)
3. Note any verses where the NASB 1995 text could not be confidently verified
