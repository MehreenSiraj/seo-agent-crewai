from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, task


@CrewBase
class SeoAgentCrew:
    """
    SEO Agent Crew for agenticflow.digital
    CrewAI version: 1.7.2 (YAML-first)
    """

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # --------------------
    # Agents
    # --------------------

    @agent
    def keyword_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["keyword_agent"],
            verbose=True,
        )

    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["research_agent"],
            verbose=True,
        )

    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["writer_agent"],
            verbose=True,
        )

    # --------------------
    # Tasks
    # --------------------

    @task
    def keyword_task(self) -> Task:
        return Task(
            config=self.tasks_config["keyword_task"],
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["writing_task"],
        )

    # --------------------
    # Crew
    # --------------------

    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.keyword_agent(),
                self.research_agent(),
                self.writer_agent(),
            ],
            tasks=[
                self.keyword_task(),
                self.research_task(),
                self.writing_task(),
            ],
            process=Process.sequential,
            verbose=True,
        )
