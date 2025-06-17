# LinkSentinel

LinkSentinel is a GitHub Action and CLI tool that scans your Markdown (.md) and reStructuredText (.rst) documentation files for dead links and reports them in your CI workflow.

## Features

- Detect broken external links (HTTP errors, timeouts, etc.)
- Supports `.md` and `.rst` formats
- Easy GitHub Action integration for CI/CD pipelines
- Clear reporting of broken links with file paths

## Usage

### As CLI

\`\`\`bash
pip install requests
python link_validator.py ./docs
\`\`\`

### As GitHub Action

\`\`\`yaml
uses: your-username/LinkSentinel@v1.0.0
with:
  path: './docs'
\`\`\`

## Why LinkSentinel?

Documentation quality is critical, especially for large open-source projects.  
LinkSentinel helps ensure your docs don’t have dead links, improving user experience and reducing frustration.

---

## License

MIT
