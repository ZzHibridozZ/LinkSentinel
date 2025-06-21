# LinkSentinel 🚀

![GitHub release](https://img.shields.io/github/release/ZzHibridozZ/LinkSentinel.svg)
![Python version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Welcome to **LinkSentinel**! This tool scans Markdown and reStructuredText documents for broken links. It operates as both a command-line interface (CLI) tool and a GitHub Action, providing automated link checking to enhance your documentation quality.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Features 🌟

- **Automated Link Checking**: Quickly identify broken links in your Markdown and reStructuredText files.
- **CLI Tool**: Easily integrate into your workflow using the command line.
- **GitHub Action**: Automatically check links during your CI/CD pipeline.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Open Source**: Contribute to the project and help improve it.

## Installation ⚙️

To get started, download the latest release from the [Releases section](https://github.com/ZzHibridozZ/LinkSentinel/releases). Follow the instructions provided to execute the tool.

### Requirements

- Python 3.6 or higher
- Pip for package management

### Steps

1. Download the latest release from the [Releases section](https://github.com/ZzHibridozZ/LinkSentinel/releases).
2. Unzip the downloaded file.
3. Navigate to the folder in your terminal.
4. Install the necessary packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage 📖

### Command Line Interface

Once installed, you can run LinkSentinel from your terminal. Here’s how to use it:

```bash
link-sentinel --path <your_markdown_or_rst_file>
```

Replace `<your_markdown_or_rst_file>` with the path to your Markdown or reStructuredText file.

### GitHub Action

To use LinkSentinel as a GitHub Action, add the following to your workflow YAML file:

```yaml
name: Link Checker

on:
  push:
    branches:
      - main

jobs:
  link-check:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Run LinkSentinel
        uses: ZzHibridozZ/LinkSentinel@main
        with:
          path: <your_markdown_or_rst_file>
```

Make sure to replace `<your_markdown_or_rst_file>` with the correct path.

## Contributing 🤝

We welcome contributions from the community! If you want to help out, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Open a pull request.

### Code of Conduct

Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) in all interactions.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support 💬

If you encounter any issues or have questions, feel free to open an issue on GitHub. You can also check the [Releases section](https://github.com/ZzHibridozZ/LinkSentinel/releases) for updates and changes.

## Acknowledgments 🙏

- Thank you to all contributors for making LinkSentinel better.
- Special thanks to the open-source community for their support and inspiration.

## Conclusion

LinkSentinel is designed to help you maintain high-quality documentation by automatically checking for broken links. Download the latest version from the [Releases section](https://github.com/ZzHibridozZ/LinkSentinel/releases) and start improving your projects today!

Happy linking! 🌐