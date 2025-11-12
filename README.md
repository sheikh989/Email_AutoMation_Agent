# Automation Agent - CrewAI Email & Report Generation System

A sophisticated multi-agent AI system powered by CrewAI that automates research, report generation, and email delivery. This system intelligently orchestrates multiple AI agents to research topics, create detailed reports, format documents, and send emails with attachments.

## 🎯 Project Overview

This automation system uses CrewAI to coordinate specialized AI agents that work together to:

- **Research**: Gather cutting-edge information on any topic
- **Report Generation**: Create both long-form (~2300 words) and executive (~400 words) reports
- **Formatting**: Transform reports into beautifully formatted markdown documents
- **Email Composition**: Write professional, context-aware emails
- **Email Delivery**: Send emails via SMTP with attachments and bulk capabilities

### Key Features

✨ **Multi-Agent Collaboration**: Researcher, Reporting Analyst, Formatter, Email Writer, and Email Assistant agents
📧 **Smart Email Handling**: Automatic subject generation, bulk sending via CSV, file attachments
📝 **Flexible Report Generation**: Choose between comprehensive or executive summaries
🔄 **Context-Aware Processing**: Agents share context and build upon each other's outputs
🎨 **Markdown Formatting**: Professional document formatting with proper structure and citations
📎 **File Attachment Support**: Seamlessly attach files to emails
🔐 **Secure SMTP**: Support for multiple email providers (Gmail, Outlook, Yahoo, Zoho, iCloud)

## 📋 Prerequisites

- **Python**: 3.10 - 3.13
- **pip** or **uv** (recommended for dependency management)
- **Environment Variables**: 
  - `OPENAI_API_KEY` or equivalent LLM provider key
  - Email credentials (configured in [src/automation/log_in.py](src/automation/log_in.py))

## 🚀 Installation

### 1. Clone or Download the Project

```bash
cd Automation_agent
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Using pip:
```bash
pip install -r requirements.txt
```

Or using uv:
```bash
pip install uv
uv pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
# Or if using other LLM providers:
# GEMINI_API_KEY=your_gemini_key
# ANTHROPIC_API_KEY=your_claude_key
```

### 5. Configure Email Credentials

Edit [src/automation/log_in.py](src/automation/log_in.py):

```python
email = "your_email@gmail.com"
password = "your_app_password_here"  # Use app-specific password, NOT your email password
```

**Important**: For Gmail and other providers, use an [App Password](https://youtu.be/MkLX85XU5rU?feature=shared), not your regular email password.

## 📁 Project Structure

```
Automation_agent/
├── src/automation/
│   ├── main.py                 # Entry point - configure inputs here
│   ├── crew.py                 # CrewAI crew definition and orchestration
│   ├── log_in.py               # Email credentials
│   ├── email_body_display.py   # Email preview utility
│   ├── config/
│   │   ├── agents.yaml         # Agent configurations
│   │   └── tasks.yaml          # Task definitions
│   └── tools/
│       ├── __init__.py
│       └── email.py            # SMTP email sending tool
├── knowledge/
│   └── user_preference.txt     # User preferences and context
├── output/                     # Generated reports and emails
│   ├── report.txt
│   ├── report.md
│   ├── report.json
│   ├── report_short.txt
│   ├── email_body.txt
│   └── research.txt
├── requirements.txt            # Python dependencies
├── pyproject.toml             # Project metadata
├── .env                       # Environment variables (create this)
├── .gitignore
├── Book1.csv                  # Example CSV for bulk email sending
└── README.md
```

## 🔧 Configuration

### Agents Configuration [src/automation/config/agents.yaml](src/automation/config/agents.yaml)

Defines the behavior, goals, and backstories of each AI agent:
- **Researcher**: Uncovers cutting-edge information on topics
- **Reporting Analyst**: Creates detailed reports from research findings
- **Formatter**: Transforms reports into beautifully formatted markdown
- **Email Writer**: Composes professional emails
- **Email Assistant**: Orchestrates email delivery via SMTP

### Tasks Configuration [src/automation/config/tasks.yaml](src/automation/config/tasks.yaml)

Defines specific tasks for each agent:
- `research_task`: Research on a given topic
- `reporting_task_long`: Create comprehensive (~2300 word) reports
- `reporting_task_short`: Create executive (~400 word) reports
- `formatting_task`: Format reports as markdown
- `write_email_body`: Compose email messages
- `send_email_task`: Send emails via SMTP

## 🎬 Usage

### Basic Usage

Edit [src/automation/main.py](src/automation/main.py) to configure your query:

```python
inputs = {
    'query': "send email to user@example.com and tell him about the Burj Khalifa",
    'attach_file_path': None,  # Optional: path to file to attach
    'csv_file': None,          # Optional: CSV for bulk email sending
    'date': datetime.now().strftime('%Y-%m-%d')
}
```

Run the automation:

```bash
python -m src.automation.main
```

Or use the configured script:

```bash
python -m automation.main
```

### Query Examples

#### 1. Send Email with Custom Message

```python
'query': "send email to john@example.com and tell him about the latest AI developments"
```

#### 2. Generate and Send Report

```python
'query': "generate a report on Sustainable Energy Solutions and send it to jane@example.com with subject 'Energy Report'"
```

#### 3. Bulk Email via CSV

```python
'csv_file': 'Book1.csv',
'query': "send report on Artificial Intelligence to clients in CSV file"
```

#### 4. Email with Attachment

```python
'query': "send email to client@example.com with the report",
'attach_file_path': 'output/report.pdf'
```

#### 5. Just Research (No Email)

```python
'query': "research the latest advancements in quantum computing"
```

## 📧 Email Features

### Supported Email Providers

The system automatically detects and configures SMTP for:
- **Gmail** (smtp.gmail.com:465)
- **Outlook/Hotmail** (smtp-mail.outlook.com:465)
- **Yahoo** (smtp.mail.yahoo.com:465)
- **Zoho** (smtp.zoho.com:465)
- **iCloud** (smtp.mail.me.com:465)

### Bulk Email Sending

Create a CSV file with an `Emails` column:

```csv
Emails
user1@example.com
user2@example.com
user3@example.com
```

Then use it in your query:

```python
'csv_file': 'Book1.csv'
```

### Email Subject Generation

The system intelligently generates subjects:
1. If you provide `subject 'My Subject'` in the query, it uses that
2. Otherwise, it extracts the first line from the report
3. Fallback: Uses "Automated Email"

### File Attachments

Attach files by providing the file path:

```python
'attach_file_path': 'output/report.pdf'
```

## 🧠 How It Works

### Agent Workflow

The system dynamically selects agents and tasks based on your query:

```
Query Analysis
    ↓
├─ Has Email? ─→ Yes ─→ Has Report? ─→ Yes ─→ Has Custom Message?
│                         │                      ├─ Yes → Research + Long Report + Short Report + Format + Write Email + Send
│                         │                      └─ No → Research + Short Report + Format + Send
│                         │
│                         └─ No → Has Custom Message?
│                                  ├─ Yes → Write Email + Send
│                                  └─ No → Write Email + Send
│
└─ No ─→ Has Report?
         ├─ Yes → Research + Long Report + Format
         └─ No → Write Email
```

### Email Composition Logic

The system combines multiple content sources:

1. **User-provided message** (from `send this message '...'`)
2. **AI-generated email body** (from write_email_body task)
3. **Generated report** (from reporting tasks)

All markdown formatting is cleaned before sending for plain-text email compatibility.

## 📊 Output Files

Generated files are saved to the `output/` directory:

| File | Purpose |
|------|---------|
| `research.txt` | Raw research findings in JSON format |
| `report.txt` | Formatted markdown report (sent via email) |
| `report.md` | Markdown version of the report |
| `report.json` | Structured report in JSON format |
| `report_short.txt` | Executive summary (~400 words) |
| `email_body.txt` | Composed email body |

## 🛠️ Tools and Libraries

### Core Dependencies

- **crewai[tools]**: Multi-agent AI orchestration framework
- **pydantic**: Data validation and settings management
- **pandas**: Data manipulation and CSV handling
- **requests**: HTTP library for data fetching
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning utilities
- **matplotlib**: Data visualization

### Python Version

- **Minimum**: 3.10
- **Maximum**: 3.13

## 🔐 Security Best Practices

1. **Never commit `.env` file** or credentials to version control
2. **Use app-specific passwords** for email accounts, not your actual password
3. **Keep `log_in.py` secure** - it contains email credentials
4. **Validate file paths** before attaching to emails
5. **Monitor SMTP logs** for unusual activity
6. **Rotate credentials regularly**

## 🐛 Troubleshooting

### SMTP Authentication Failed

```
SMTP Send Error: (535, b'5.7.8 Username and password not accepted')
```

**Solution**: 
- Verify email and password in [src/automation/log_in.py](src/automation/log_in.py)
- Use an app-specific password, not your email password
- Check that 2-factor authentication is enabled (required for Gmail app passwords)

### Email Not Sending

```
FileNotFoundError: Attachment not found
```

**Solution**: Verify the attachment file path exists and is accessible.

### No Report Generated

Ensure your query contains keywords like "report", "research", or "generate" for report tasks to be included.

### API Key Issues

Verify your `.env` file has the correct API key for your LLM provider (OpenAI, Gemini, etc.).

## 📝 Example Queries

See [knowledge/user_preference.txt](knowledge/user_preference.txt) for user context and preferences that inform agent behavior.

### Complete Examples

1. **Research + Email**
   ```
   "Generate a report on Quantum Computing and send it to alice@example.com"
   ```

2. **Bulk Email + Report**
   ```
   "Send research on AI Ethics to all clients in Book1.csv"
   ```

3. **Custom Email + Attachment**
   ```
   "Send email to bob@example.com with message 'Please review attached document' and attach report.pdf"
   ```

## 📚 Resources

- [CrewAI Documentation](https://docs.crewai.com)
- [CrewAI GitHub Repository](https://github.com/joaomdmoura/crewai)
- [NIST Email Authentication Guide](https://www.nist.gov/)
- [App Password Setup Video](https://youtu.be/MkLX85XU5rU?feature=shared)
- [CrewAI Discord Community](https://discord.com/invite/X4JWnZnxPb)

## 🤝 Contributing

This is a personal automation project. For improvements or extensions:
1. Test thoroughly with different query types
2. Update configuration files as needed
3. Ensure backward compatibility with existing tasks

## 📄 License

Personal use project.

## ✨ Future Enhancements

- [ ] Database integration for report storage
- [ ] Web UI for easy query input
- [ ] Advanced scheduling for automated reports
- [ ] Multi-language email support
- [ ] Report analytics and metrics
- [ ] Custom agent capabilities
- [ ] Advanced authentication methods (OAuth2)

---

**Last Updated**: 2025
**Python Version**: 3.10 - 3.13
**CrewAI Version**: 0.148.0+
