import logging
import abc

class AgentError(Exception):
    """Custom exception for agent errors."""
    pass

class BaseAgent(abc.ABC):
    """Base class for all agents implementing the abstract base class pattern."""

    def __init__(self):
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        self.logger.info('Logging has been set up for BaseAgent.')

    @abc.abstractmethod
    def run(self):
        """Abstract method to run the agent. Must be implemented by subclasses."""