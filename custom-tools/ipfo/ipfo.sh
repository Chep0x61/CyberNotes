#!/bin/bash

print_color() {
    local color="$1"
    local text="$2"
    echo -e "\e[${color}m${text}\e[0m"
}

echo -n "🌐 public: "
print_color "32" "$(curl -s ifconfig.me)"

echo -n "🏠 local: "
local_network_ip=$(hostname -I | awk '{print $1}')
print_color "32" "$local_network_ip"

echo -n "🕳️  tun0: "
tun0_ip=$(ip addr show tun0 | grep "inet " | awk '{print $2}' | sed 's/\/.*//')
print_color "32" "$tun0_ip"
