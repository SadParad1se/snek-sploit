from typing import Dict, Any
from dataclasses import dataclass

from snek_sploit.lib.context import ContextBase, Context
from snek_sploit.util import constants


@dataclass
class JobInformation:
    id: int
    name: str
    start_time: int
    datastore: Dict[str, Any]


class RPCJobs(ContextBase):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Job.html
    """

    INFO = "job.info"
    LIST = "job.list"
    STOP = "job.stop"

    @staticmethod
    def _parse_job_information(response: Dict[str, Any]) -> JobInformation:
        return JobInformation(
            response[constants.JID],
            response[constants.NAME].decode(),
            response[constants.START_TIME],
            {
                key.decode() if isinstance(key, bytes) else key: value
                for key, value in response[constants.DATASTORE].items()
            },
        )

    def info(self, job_id: int) -> JobInformation:
        """
        Get information about a job.
        :param job_id: ID of the job
        :return: Information about the job
        :full response example:
            {'jid': 2, 'name': b'Auxiliary: scanner/portscan/tcp', 'start_time': 1700170400,
             'datastore': {b'PORTS': '[22, 123, 21]', b'RHOSTS': '192.168.0.0/24', b'VERBOSE': 'false', b'SSL': 'false',
             b'SSLVersion': b'Auto', b'SSLVerifyMode': b'PEER', b'ConnectTimeout': '10', b'TCP::max_send_size': '0',
             b'TCP::send_delay': '0', b'THREADS': '1', b'ShowProgress': 'true', b'ShowProgressPercent': '10',
             b'TIMEOUT': '1000', b'CONCURRENCY': '10', b'DELAY': '0', b'JITTER': '0', b'WORKSPACE': '',
             b'SSLServerNameIndication': '', b'SSLCipher': '', 'Proxies': '', 'CPORT': '', 'CHOST': ''}}
        """
        response = self._context.call(self.INFO, [job_id])

        return self._parse_job_information(response)

    def list_jobs(self) -> dict[int, str]:
        """
        List jobs.
        :return: Job ID and name
        :full response example: {'0': b'Auxiliary: scanner/portscan/tcp'}
        """
        response = self._context.call(self.LIST, [])

        return {int(key): value.decode() for key, value in response.items()}

    def stop(self, job_id: int) -> bool:
        """
        Stop a job.
        :param job_id: ID of the job
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(self.STOP, [job_id])

        return response[constants.B_RESULT] == constants.B_SUCCESS


class Jobs(ContextBase):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCJobs(context)
