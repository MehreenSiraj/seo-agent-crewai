#!/usr/bin/env python
import warnings
from datetime import datetime

from seo_agent_crew.crew import SeoAgentCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

"""
Entry point for running the SEO Agent Crew locally.

Purpose:
- Generate SEO keywords
- Perform SERP & intent research
- Write a long-form SEO blog article
- Save output to file (defined in tasks.yaml)
"""

def run():
    """
    Run the SEO Agent Crew with test inputs.
    """
    inputs = {
        "topic": "Agentic AI workflows for SEO",
        "current_year": datetime.now().year
    }

    try:
        crew = SeoAgentCrew().crew()
        crew.kickoff(inputs=inputs)

        print("\n✅ SEO blog generation completed successfully.")
        print("📄 Check the output folder for the generated Markdown file.")

    except Exception as e:
        raise RuntimeError(f"❌ Error while running SEO Agent Crew: {e}")


if __name__ == "__main__":
    run()
