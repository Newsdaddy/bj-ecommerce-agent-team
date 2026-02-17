# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**APAC Lead Magnet Auto-Generator** - Multi-agent system that automatically generates 3 lead magnets daily for APAC commerce professionals and publishes them to Google Docs.

**Tech Stack:**
- Python 3.10+
- LangChain + LangGraph (multi-agent orchestration)
- Anthropic Claude API (Opus 4.5)
- Google Docs API
- APScheduler (daily automation)
- Pydantic (data validation)

## Development Commands

### Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with API keys
```

### Running the System

```bash
# Run once immediately
python main.py --run-now

# Run for specific date
python main.py --run-now --date 2025-01-15

# Start daily scheduler (blocking, runs at configured time)
python main.py --schedule
```

### Google API Setup

Before first run, set up Google Docs API:

1. Go to Google Cloud Console
2. Create new project or select existing
3. Enable Google Docs API and Google Drive API
4. Create OAuth 2.0 Client ID (Desktop app)
5. Download `credentials.json` to project root
6. First run will open browser for OAuth consent
7. Token saved to `token.json` for future runs

## Architecture

### Multi-Agent Pipeline

```
Scheduler (07:00 GMT daily)
    ↓
Orchestrator (LangGraph StateGraph)
    ├─ Research Agent         → research-apac-trends skill
    ├─ Content Writer Agent   → structure-lead-magnet skill (×3)
    └─ QA Editor Agent        → fact-check-content + design-google-doc skills
```

### 3 Agents

**1. Research Agent** (`agents/research_agent.py`)
- Researches APAC eCommerce, D2C, logistics trends
- Uses `research-apac-trends` Claude skill
- Outputs: 3-5 trends + 3 distinct content angles
- Returns: `ResearchOutput` model

**2. Content Writer Agent** (`agents/content_writer_agent.py`)
- Creates 3 lead magnets (1 Korean + 2 English)
- Uses `structure-lead-magnet` Claude skill
- Types: Mix of reports, checklists, guides, case studies
- Returns: `ContentWriterOutput` with 3 `LeadMagnetContent` objects

**3. QA Editor Agent** (`agents/qa_editor_agent.py`)
- Fact-checks content using `fact-check-content` skill
- Publishes to Google Docs using `design-google-doc` skill
- Returns: `QAEditorOutput` with document URLs

### 4 Claude Skills

Located in `.claude/skills/`. Each has a `SKILL.md` file.

**1. research-apac-trends** - Research APAC commerce trends
**2. structure-lead-magnet** - Write lead magnet content
**3. fact-check-content** - Review and polish content
**4. design-google-doc** - Format and publish to Google Docs

Skills are invoked automatically by agents through Claude's skill system.

## Key Files

### Configuration
- `config/settings.py` - Pydantic Settings loading from `.env`
- `config/prompts.py` - System prompts for each agent
- `.env` - API keys, schedule, content settings

### Data Models
- `models.py` - Pydantic models for all data structures:
  - `ResearchOutput`, `ResearchTrend`
  - `LeadMagnetContent`, `ContentWriterOutput`
  - `ReviewedContent`, `PublishedDocument`, `QAEditorOutput`
  - `WorkflowState` (LangGraph state)

### Orchestration
- `orchestrator/workflow.py` - LangGraph StateGraph implementation
- `orchestrator/scheduler.py` - APScheduler for daily runs

### Utilities
- `utils/google_docs_client.py` - Google Docs API wrapper
  - Authentication, document creation, formatting, folder management

## Workflow State Machine

LangGraph manages state through these transitions:

```
pending → research → writing → qa → completed
                               ↓
                            failed (if error)
```

State passed between nodes contains:
- `research_output`: Research data
- `content_writer_output`: Draft lead magnets
- `qa_editor_output`: Reviewed + published documents
- `final_document_urls`: List of Google Docs URLs
- `workflow_status`: Current stage
- `error_message`: If failed

## Modifying Agents

### Adding New Agent Capability

1. **Add skill** in `.claude/skills/new-skill/SKILL.md`
2. **Update agent** to invoke skill in prompt
3. **Modify workflow** if adding new node (optional)

### Changing Content Settings

Edit `.env`:
- `DAILY_LEAD_MAGNETS` - Total count
- `KOREAN_COUNT` / `ENGLISH_COUNT` - Language split
- `TARGET_WORDS_MIN` / `TARGET_WORDS_MAX` - Length range

### Changing Schedule

Edit `.env`:
- `GENERATION_TIME` - Time in HH:MM format (24-hour)
- `TIMEZONE` - Timezone (e.g., "GMT", "Asia/Seoul")

## Google Docs Integration

### Document Creation Flow

1. **GoogleDocsClient** authenticates via OAuth
2. **create_document()** - Creates blank doc
3. **insert_and_format_content()** - Parses markdown, applies styling
4. **move_to_folder()** - Moves to specified Drive folder
5. Returns document ID and URL

### Styling

- Korean docs: 맑은 고딕 font
- English docs: Arial font
- Title: 24pt bold, centered
- Headings: 18pt bold
- Body: 11pt, 1.5 line spacing

### Markdown Parsing

`_parse_markdown()` converts:
- `# Title` → Title style
- `## Heading` → Heading style
- `- List` → Bullet points
- `1. Numbered` → Numbered list
- Plain text → Body text

## Error Handling

### Common Issues

**"Google API not authenticated"**
- Run once manually to complete OAuth flow
- Ensure `credentials.json` exists
- Check `token.json` permissions

**"Quota exceeded"**
- Google Docs API has rate limits
- Agent implements retry with delay
- Consider caching or reducing calls

**"Parsing failed"**
- Agents use regex to extract JSON from Claude responses
- May be wrapped in ```json code blocks
- Fallback: use original content

**"Workflow failed at X stage"**
- Check `error_message` in final state
- Review agent logs (printed to console)
- Each agent can fail independently

## Testing Workflow

```bash
# Test single run (will use real APIs)
python main.py --run-now

# Test with specific date
python main.py --run-now --date 2025-01-20
```

No dedicated test suite - system integrates with real APIs (Claude, Google).

## Data Flow

```
Research Agent
    ↓ ResearchOutput (JSON)
Content Writer Agent
    ↓ ContentWriterOutput (3 × LeadMagnetContent)
QA Editor Agent
    ├─ ReviewedContent (corrected markdown)
    └─ PublishedDocument (Google Docs URLs)
```

All models are Pydantic - validated at runtime.

## Environment Variables

Required:
- `ANTHROPIC_API_KEY` - Claude API key
- `GOOGLE_FOLDER_ID` - Drive folder for documents

Optional:
- `CLAUDE_MODEL` - Default: claude-opus-4-5-20251101
- `MAX_TOKENS` - Default: 4000
- `TEMPERATURE` - Default: 0.7
- `GENERATION_TIME` - Default: 07:00
- `TIMEZONE` - Default: GMT

## Customization Points

### Target Audience

Edit `TARGET_REGIONS` and `TARGET_ROLES` in `.env`:
```
TARGET_REGIONS=Korea,Vietnam,Indonesia,Singapore
TARGET_ROLES=D2C Strategy,eCommerce Manager,Logistics Partnership
```

### Lead Magnet Types

Defined in `structure-lead-magnet` skill:
1. Industry Insight Report
2. Checklist
3. How-to Guide
4. Case Study Brief
5. Framework/Template

### Content Prompts

Edit `config/prompts.py` to change agent behavior:
- `RESEARCH_AGENT_PROMPT` - Research focus areas
- `CONTENT_WRITER_AGENT_PROMPT` - Writing guidelines
- `QA_EDITOR_AGENT_PROMPT` - Review criteria

## Scheduler Details

Uses APScheduler `BlockingScheduler`:
- Runs in foreground (blocking)
- CronTrigger for daily execution
- Timezone-aware scheduling
- Graceful shutdown on Ctrl+C

For production:
- Use `BackgroundScheduler` for non-blocking
- Or deploy with systemd/supervisor
- Add logging to file instead of console

## Known Limitations

1. **Sequential processing**: 3 lead magnets created sequentially (not parallel) - each waits for previous
2. **No retry logic**: If one lead magnet fails, workflow continues but that magnet is skipped
3. **Single instance**: Not designed for concurrent runs (state is process-local)
4. **API rate limits**: No built-in throttling for Google/Claude APIs
5. **No database**: All state is in-memory, lost on restart

## Future Enhancements

If extending this system:
- Add database (SQLite/PostgreSQL) for historical tracking
- Implement parallel content generation (async agents)
- Add webhook notifications instead of just console output
- Create web dashboard for monitoring
- Add retry logic with exponential backoff
- Support multiple output formats (PDF, Notion, etc.)
