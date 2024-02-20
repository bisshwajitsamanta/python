"""
    Goal:
        1. Capture the service status of
            a. CDR Agent
            b. SCE Agent
            c. audit node service status
        2. Send the metrics to Datadog
            a. as a metric to datadog
        3. Capture all the python programs which are running part of Cron Jobs
            a. Health check job
            b. zfs snapshot

"""
import subprocess
from shlex import quote as shlex_quote


class ServiceStatus:

    def check_service_status(self,service_name):
        try:
            subprocess.run(["systemctl", "is-active", "--quiet", shlex_quote(service_name)], shell=True)
            return 1
        except subprocess.CalledProcessError:
            return 0

    def cdr_agent_status(self):
        return self.check_service_status("cdr-agent")

    def sce_agent_status(self):
        return self.check_service_status("sce-agent")

    def audit_node_status(self):
        return self.check_service_status("auditd")


class CaptureScript:

    def capture_cronjob_programs(self):
        pass


class SendMetricToDatadog:

    def __init__(self, datadog_api_key, datadog_app_key):
        self.datadog_api_key = datadog_api_key
        self.datadog_app_ke = datadog_app_key

    def send_custom_metric(self):
        pass
