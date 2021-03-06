# Stubs for fabric.network (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

msg = ...  # type: Any
ipv6_regex = ...  # type: Any

def direct_tcpip(client, host, port): ...
def is_key_load_error(e): ...
def get_gateway(host, port, cache, replace: bool = ...): ...

class HostConnectionCache(dict):
    def connect(self, key): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key): ...
    def __contains__(self, key): ...

def ssh_config(host_string: Optional[Any] = ...): ...
def key_filenames(): ...
def key_from_env(passphrase: Optional[Any] = ...): ...
def parse_host_string(host_string): ...
def normalize(host_string, omit_port: bool = ...): ...
def to_dict(host_string): ...
def from_dict(arg): ...
def denormalize(host_string): ...
def join_host_strings(user, host, port: Optional[Any] = ...): ...
def normalize_to_string(host_string): ...
def connect(user, host, port, cache, seek_gateway: bool = ...): ...
def prompt_for_password(prompt: Optional[Any] = ..., no_colon: bool = ..., stream: Optional[Any] = ...): ...
def needs_host(func): ...
def disconnect_all(): ...
