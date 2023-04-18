import subprocess


class BedrockServerWrapper:
    def __init__(self, server_path, server_args):
        self.server_path = server_path
        self.server_args = server_args
        self.process = None

    def start_server(self):
        self.process = subprocess.Popen(
            [self.server_path, *self.server_args],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    def send_command(self, command):
        if not self.process:
            raise RuntimeError("Server is not running")
        self.process.stdin.write(f"{command}\n".encode())
        self.process.stdin.flush()

    def get_output(self):
        if not self.process:
            raise RuntimeError("Server is not running")
        output = self.process.stdout.readline()
        return output.decode().strip()

    def get_error(self):
        if not self.process:
            raise RuntimeError("Server is not running")
        error = self.process.stderr.readline()
        return error.decode().strip()

    def stop_server(self):
        if not self.process:
            return
        self.send_command("stop")
        self.process.wait()
        self.process = None

    def backup_server(self, backup_path):
        if not self.process:
            raise RuntimeError("Server is not running")
        self.send_command(f"save hold")
        self.send_command(f"save resume")
        self.send_command(f"save query")
        while True:
            response = self.get_output()
            if response.startswith("Data saved."):
                break
            elif response.startswith("Failed to save data."):
                raise RuntimeError("Failed to backup server")
        subprocess.call(["tar", "-czf", backup_path, "worlds"])
        return backup_path

    def get_status(self):
        if self.process is None:
            return "Server not running"
        elif self.process.poll() is not None:
            return "Server stopped with exit code {}".format(self.process.returncode)
        else:
            return "Server is running"

    def __del__(self):
        self.stop_server()
