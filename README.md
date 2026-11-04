# ch-public-skills

A Claude Code plugin marketplace with my public skills.

| Plugin | What it does |
|---|---|
| `korean-sermon-translator` | Translates a Korean sermon manuscript (TXT or PDF) into English and saves a Word file. By default the Korean stays, with the English directly underneath each title, header, paragraph and scripture. Ask for English only to drop the Korean. Scripture uses the NASB 1995 unless the sermon or you name another version. |

## Install

```
/plugin marketplace add calebih/ch-public-skills
/plugin install korean-sermon-translator@ch-public-skills
```

## Use

```
/korean-sermon-translator:korean-sermon-translator <sermon-file>
```

The skill also triggers on its own when you hand Claude a Korean sermon.

It needs Python with `python-docx` to build the Word file (`pip install python-docx`) and web search to look up scripture.

## Layout

```
.claude-plugin/marketplace.json        # marketplace catalog
plugins/<plugin>/.claude-plugin/plugin.json
plugins/<plugin>/skills/<skill>/SKILL.md
```

To ship an update, bump `version` in both the plugin's `plugin.json` and its `marketplace.json` entry.

## License

MIT
