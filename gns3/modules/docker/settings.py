# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Default Docker settings.
"""

from gns3.node import Node

DOCKER_SETTINGS = {
    "docker_url": "",
    "docker_user": "",
    "use_local_server": True
}

DOCKER_SETTING_TYPES = {
    "docker_url": str,
    "docker_user": str,
    "use_local_server": bool
}

# FIXME: symbols
DOCKER_CONTAINER_SETTINGS = {
    "default_symbol": ":/symbols/vbox_guest.normal.svg",
    "hover_symbol": ":/symbols/vbox_guest.selected.svg",
    "category": Node.end_devices,
    "adapters": 1,
    "adapter_type": "veth",
    "console": "gnome-terminal",
    "enable_remote_console": False,
}

DOCKER_CONTAINER_SETTING_TYPES = {
    "default_symbol": str,
    "hover_symbol": str,
    "category": int,
    "adapters": int,
    "adapter_type": str,
    "console": str,
    "enable_remote_console": bool
}
