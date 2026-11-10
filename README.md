# LLM-Powered Business Analyst Assistant

A locally hosted Generative AI application built with Python, Ollama, Qwen3 8B, and Pydantic.

## Overview

This application transforms business requirements into structured Business Analysis deliverables using a locally running Large Language Model.

## Features

- Business requirement input via CLI
- Role-based prompting
- User story generation
- Acceptance criteria generation
- Clarification question generation
- Structured JSON outputs
- Pydantic schema validation
- Unique analysis IDs and metadata
- Human review status tracking
- Automated testing with pytest
- Mocking of Ollama connection and API errors

## Technology Stack

- Python
- Ollama
- Qwen3 8B
- Pydantic
- pytest
- JSON

## Requirements

- Python 3.11+
- Ollama installed and running
- Sufficient local memory to run Qwen3 8B

## Installation

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install Python dependencies:

   `python -m pip install -r requirements.txt`

4. Download the model:

   `ollama pull qwen3:8b`

5. Ensure Ollama is running.

6. Run the application:

   `python main.py`

## Testing

Run the automated tests:

`python -m pytest -v`

## Outputs

The application saves validated analysis records as uniquely named JSON files inside the `outputs/` directory.

Each record includes:

- Analysis ID
- Creation timestamp
- Original business requirement
- Model name
- Review status
- Generated user story
- Acceptance criteria
- Clarification questions

## Limitations

AI-generated requirements are drafts and must be reviewed by a qualified Business Analyst or relevant stakeholder before implementation.

Schema validation does not guarantee business correctness.

## Future Improvements

- Multi-turn requirements elicitation
- Automated requirements traceability
- Business process analysis
- RAG integration
- Agentic AI workflows
- Web-based user interface

## Purpose

This project demonstrates practical application of Generative AI, Python software development, business analysis, structured output validation, and automated testing.