from dataclasses import dataclass

from snek_sploit.lib.base import Base
from snek_sploit.util import constants


@dataclass
class JobInformation:  # TODO unfinished, untested
    id: int
    name: str
    start_time: int
    datastore: dict
# 'jid' [Integer] The Job ID.
# 'name' [String] The name of the job.
# 'start_time' [Integer] The start time.
# 'datastore' [Hash] Datastore options for the module. 

class RPCJob(Base):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Job.html
    """
    INFO = "job.info"
    LIST = "job.list"
    STOP = "job.stop"

    def info(self, job_id: int) -> JobInformation:  # TODO unfinished, untested
        """
        Get information about a job.
        :return: Information about the job
        :full response example:
        """
        response = self._context.call(self.INFO, [job_id])

        return response

    def list_jobs(self) -> dict[int, JobInformation]:  # TODO unfinished, untested
        """
        List jobs.
        :return: All jobs and their information
        :full response example:
        """
        response = self._context.call(self.LIST, [])

        return response

    def stop(self, job_id: int) -> bool:  # TODO unfinished, untested
        """
        Stop a job.
        :return: True in case of success
        :full response example:
        """
        response = self._context.call(self.STOP, [job_id])

        return response[constants.RESULT] == constants.SUCCESS
