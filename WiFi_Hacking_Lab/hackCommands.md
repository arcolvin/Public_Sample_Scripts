# Set the WI-Fi card into monitor mode

First kill all OS based network interference:

> \# airmon-ng check kill

**NOTE**: This may not be strictly required abut this will kill all networking on the hacking device. Doing this step will decrease the likelihood of interference from other processes.

Next step is to see what wireless devices we have available

> \# airmon-ng

Take note of the interface name. We will use this with the next  command.

> \# airmon-ng start \<interfaceName>

This will change the device name. In short it will append mon to the end of the device nome. This will be shortened to \<mon0> for the remainder of this writeup, but needs to be the full name when entered on the command line

**NOTE**: If you want to restore this to normal operation stop the monitor version of the interface

> \# airmon-ng stop \<mon0>

# Monitor the local Wi-Fi Landscape

Use the following command to identify local base stations.

> \# airodump-ng \<mon0>

Identify the station that we want to attack. This can be done by its ESSID if the SSID is known / broadcasting.

Once the network is identified stop the capture with ctrl+c and record the BSSID and Channel.

The BSSID is the MAC Address of the target base station. The BSSID will take the form 1A:2B:3D:4E:5F:6G. Save this for future steps This will be shortened to \<apBSSID> for future commands. 

We also need to record what channel the station is communicating on. This value will be indicated with \<ch> in future commands.

# Capture the WPA Handshake

The following command will monitor a base station for a handshake to occur.

> \# airodump-ng -c \<ch> --bssid \<apBSSID> -w WPAcrack \<mon0> --ignore-negative-one

A handshake happens every so often if patent. This is due to Wi-Fi requiring reauthorization periodically from its clients.

If we are not patient, we can force a deauth / reauth. While this speeds things up, it also is a noisy attack. Up until now we have simply been listening, and in theory no one should know we are here. Performing the deauth will inject packets into the datastream and someone who knows what to look for will know what is happening.

While monitoring for a handshake connected clients should pop up in the window as traffic is sent. Collect the Station address and use it in the following command. Station address will be referenced as \<stBSSID>.

To deauth a target:

> \# aireplay-ng --deauth 100 -a \<apBSSID> -c \<stBSSID> \<mon0> --ignore-negative-one

Regardles of wether the deaith attack was sent or not, once the banner WPA handshake 00:11:22:33:44:55 appears at the top of the monitoring terminal stop the monitoring process.

# Break the Wi-Fi Password

Using aircrack-ng we will now attempt to identify the password. We will need a wordlist such as rockyou.txt, but anywordlist will work (Assuming the password is in the list somewhere!)

> \# aircrack-ng -w \<wordList> -b \<apBSSID> \<capturedCrackFile (WPAcrack.cap)>

From:
https://www.shellhacks.com/how-to-use-aircrack-ng-wifi-password-hacker-tutorial/

https://www.aircrack-ng.org/doku.php?id=cracking_wpa