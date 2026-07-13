### 🔹 Lesson #05 | [Beginner] | Networking

### Concept: Basic Device Hardening - Login Banners and Session Timeouts

Greetings, future network engineers! Welcome back to the training terminal. As your Enterprise Infrastructure Hardening & Access Policy Compliance Sentinel, I am here to guide you through another critical phase of securing our corporate topology.

In our previous lessons, we successfully established hostnames, enforced local user authentication, encrypted local passwords, and deployed secure SSH access across our routers (`HQ-R1`, `Branch-R2`) and switches (`HQ-S1`, `Branch-S2`). Today, we focus on operational security and liability management. This lesson covers how to display legal warning banners to deter unauthorized access and enforce automatic idle session timeouts. These steps prevent administrative sessions from being left open and vulnerable to exploitation.

---

### 💡 Analogy

Imagine the server room is a high-security corporate building.

* **The MOTD Banner** is like a prominent **"WARNING: AUTHORIZED PERSONNEL ONLY. VIOLATORS WILL BE PROSECUTED"** sign posted directly on the front door. Without this sign, an intruder could legally claim they didn't know they were trespassing.
* **The Exec-Timeout** is like an **automatic self-locking spring** on that door. If an administrator opens the door to walk in but gets distracted and walks away, the door automatically swings shut and locks itself after a few minutes, preventing unauthorized people from slipping inside.

---

### Step 1️⃣: Access HQ-R1 via the CLI and Enter Global Configuration Mode

* **Mini-Lesson / Explanation**: To make any fundamental architectural changes to our network devices, we must navigate up the Cisco IOS privilege hierarchy. We start from user EXEC mode, use credentials established in Lesson 3 to enter privileged EXEC mode, and finally move into global configuration mode.
* **Commands to execute**:
```bash
HQ-R1> enable
Password: class
HQ-R1# configure terminal
HQ-R1(config)#

```


* **Verification commands**: Observe the CLI prompt transition to ensure you are in the correct mode.
```bash
# The prompt must display:
HQ-R1(config)#

```


* **🚨 Common error note or Troubleshooting tip**: If you type `configure terminal` and receive an error, make sure your prompt shows `HQ-R1#` (Privileged EXEC) and not `HQ-R1>` (User EXEC).
* **🎯 Mini challenge**: What keyboard shortcut can you use instead of typing out the full word `configure terminal`? *(Answer: `conf t`)*

---

### Step 2️⃣: Configure a Message of the Day (MOTD) Banner on HQ-R1

* **Mini-Lesson / Explanation**: A Message of the Day (MOTD) banner displays a legal notice before a user logs in. We use a delimiting character (like `#`) to mark the beginning and end of our banner text. The text inside must clearly state that unauthorized access is prohibited to provide legal protection during security audits.
* **Commands to execute**:
```bash
HQ-R1(config)# banner motd # UNAUTHORIZED ACCESS STRICTLY PROHIBITED #

```


* **Verification commands**: Exit to the initial login screen to see your new banner in action.
```bash
HQ-R1(config)# exit
HQ-R1# exit
# Press Enter to activate the console, and you should see:
UNAUTHORIZED ACCESS STRICTLY PROHIBITED

```


* **🚨 Common error note or Troubleshooting tip**: If you forget to close the banner text with the matching delimiting character (the second `#`), the router will keep consuming every command you type next as part of the banner message.
* **🎯 Mini challenge**: Try creating a multi-line banner by pressing Enter before typing the final `#` delimiter.

---

### Step 3️⃣: Enter Console Line Configuration Mode on HQ-R1

* **Mini-Lesson / Explanation**: Devices have physical and virtual management paths called lines. To change settings for a direct physical connection using a console cable, we need to shift from global configuration mode into console line configuration mode using `line console 0`.
* **Commands to execute**:
```bash
HQ-R1# configure terminal
HQ-R1(config)# line console 0
HQ-R1(config-line)#

```


* **Verification commands**: Verify that your prompt changes to show you are configuring a specific line.
```bash
# The prompt must change to:
HQ-R1(config-line)#

```


* **🚨 Common error note or Troubleshooting tip**: Do not confuse `line console 0` with virtual lines. Routers only have one physical console port, which is always designated as number `0`.
* **🎯 Mini challenge**: Run `show line` from privileged EXEC mode to view all available management lines on this device.

---

### Step 4️⃣: Configure Console Exec-Timeout on HQ-R1

* **Mini-Lesson / Explanation**: If an administrator leaves their terminal unattended, anyone with physical access could tamper with the network. The `exec-timeout` command automatically disconnects an inactive session. The syntax is `exec-timeout [minutes] [seconds]`. We will set this to 5 minutes and 0 seconds.
* **Commands to execute**:
```bash
HQ-R1(config-line)# exec-timeout 5 0

```


* **Verification commands**: Check the active console line settings using the `show running-config` command section.
```bash
HQ-R1(config-line)# do show running-config | section line con 0
# Expected output:
line con 0
 exec-timeout 5 0
 login local

```


* **🚨 Common error note or Troubleshooting tip**: Be careful not to type `exec-timeout 0 0`. Setting both values to zero disables the timeout completely, leaving the line permanently open if left logged in.
* **🎯 Mini challenge**: How would you configure an executive timeout of exactly 2 minutes and 30 seconds? *(Answer: `exec-timeout 2 30`)*

---

### Step 5️⃣: Enter Virtual Terminal (VTY) Line Mode on HQ-R1

* **Mini-Lesson / Explanation**: In Lesson 4, we enabled SSH for remote connections on lines `0` through `4`. Just like physical console lines, remote terminal lines can be left open accidentally. We need to enter VTY configuration mode to apply timeout policies to these lines.
* **Commands to execute**:
```bash
HQ-R1(config-line)# exit
HQ-R1(config)# line vty 0 4
HQ-R1(config-line)#

```


* **Verification commands**: Ensure that your context prompt transitions correctly back to the line mode.
```bash
# Confirm the prompt reads:
HQ-R1(config-line)#

```


* **🚨 Common error note or Troubleshooting tip**: If you accidentally type `line vty 0 15` on a router, some routers may give an error if they do not support 16 simultaneous virtual connections. Always verify device limits.
* **🎯 Mini challenge**: What command allows you to jump directly from console mode to VTY mode without typing `exit` first? *(Answer: Simply type `line vty 0 4` directly from `config-line`)*

---

### Step 6️⃣: Configure VTY Exec-Timeout on HQ-R1

* **Mini-Lesson / Explanation**: Remote SSH sessions are common targets for session hijacking if left active. Applying the same `exec-timeout 5 0` rule to our VTY lines ensures that remote connections automatically log out after 5 minutes of inactivity.
* **Commands to execute**:
```bash
HQ-R1(config-line)# exec-timeout 5 0

```


* **Verification commands**: View the active VTY line configuration to verify the changes.
```bash
HQ-R1(config-line)# do show running-config | section line vty
# Expected output:
line vty 0 4
 exec-timeout 5 0
 login local
 transport input ssh

```


* **🚨 Common error note or Troubleshooting tip**: Make sure you apply this to all active VTY lines (`0 4` on this router). Leaving even one VTY line without a timeout leaves a vulnerability open.
* **🎯 Mini challenge**: If you want to drop a connection immediately when it goes idle for one minute, what parameters do you pass to the command? *(Answer: `exec-timeout 1 0`)*

---

### Step 7️⃣: Verify Running Configuration on HQ-R1

* **Mini-Lesson / Explanation**: Verification is a core habit of successful network engineers. We must check the system's running configuration to confirm that our banner and timeout settings are active before moving to other devices.
* **Commands to execute**:
```bash
HQ-R1(config-line)# end
HQ-R1# show running-config

```


* **Verification commands**: Scroll through the output and verify that both the banner and line definitions look correct.
```bash
# Look for these lines in the output:
banner motd ^C UNAUTHORIZED ACCESS STRICTLY PROHIBITED ^C
...
line con 0
 exec-timeout 5 0
line vty 0 4
 exec-timeout 5 0

```


* **🚨 Common error note or Troubleshooting tip**: Cisco IOS may automatically convert your `#` character to `^C` or another internal delimiter in the running configuration file. This is normal behavior and does not impact your configuration.
* **🎯 Mini challenge**: What filtered command shows only the lines containing the word "banner"? *(Answer: `show running-config | include banner`)*

---

### Step 8️⃣: Replicate Hardening Policies on Branch-R2

* **Mini-Lesson / Explanation**: Consistency is essential for maintaining enterprise security compliance. We will now apply the exact same configurations to our second router, `Branch-R2`, using the same banner wording and timeout intervals.
* **Commands to execute**:
```bash
Branch-R2# configure terminal
Branch-R2(config)# banner motd # UNAUTHORIZED ACCESS STRICTLY PROHIBITED #
Branch-R2(config)# line console 0
Branch-R2(config-line)# exec-timeout 5 0
Branch-R2(config-line)# line vty 0 4
Branch-R2(config-line)# exec-timeout 5 0
Branch-R2(config-line)# end

```


* **Verification commands**: Confirm that the running configuration on `Branch-R2` matches our security profile.
```bash
Branch-R2# show running-config | include banner
# Must output: banner motd # UNAUTHORIZED ACCESS STRICTLY PROHIBITED #

```


* **🚨 Common error note or Troubleshooting tip**: Double-check that you are logged into `Branch-R2` by looking at the hostname prompt before pasting commands, preventing configuration accidental overwrites on `HQ-R1`.
* **🎯 Mini challenge**: Save the running configuration to nvram on `Branch-R2` so it persists through a reboot. What command do you use? *(Answer: `copy running-config startup-config` or `write`)*

---

### Step 9️⃣: Configure MOTD and Console Timeout on HQ-S1 Switch

* **Mini-Lesson / Explanation**: Enterprise switches require the same security baseline as routers. We will access our primary switch, `HQ-S1`, configure the legal warning banner, and set the 5-minute timeout on its console port.
* **Commands to execute**:
```bash
HQ-S1# configure terminal
HQ-S1(config)# banner motd # UNAUTHORIZED ACCESS STRICTLY PROHIBITED #
HQ-S1(config)# line console 0
HQ-S1(config-line)# exec-timeout 5 0

```


* **Verification commands**: Verify your configuration directly from the line mode context.
```bash
HQ-S1(config-line)# do show running-config | include banner
# Verification check: Must display the warning string.

```


* **🚨 Common error note or Troubleshooting tip**: Switches use the exact same Cisco IOS syntax for banners and console lines as routers. If a command fails, verify that you are in the correct configuration mode.
* **🎯 Mini challenge**: Exit completely out of `HQ-S1` console to verify that the banner text appears correctly before the authentication prompt.

---

### Step 🔟: Configure VTY Lines Timeout on HQ-S1 Switch

* **Mini-Lesson / Explanation**: A key difference between Cisco routers and switches is the number of virtual terminal lines. While standard routers generally default to 5 lines (`0 4`), switches typically support 16 concurrent virtual terminal lines (`0 15`). We must apply the timeout configuration across all 16 lines.
* **Commands to execute**:
```bash
HQ-S1(config-line)# line vty 0 15
HQ-S1(config-line)# exec-timeout 5 0

```


* **Verification commands**: Run a running-config verification targeting the VTY blocks.
```bash
HQ-S1(config-line)# do show running-config | section line vty
# Expected output:
line vty 0 4
 exec-timeout 5 0
line vty 5 15
 exec-timeout 5 0

```


* **🚨 Common error note or Troubleshooting tip**: If you only type `line vty 0 4` on a switch, lines 5 through 15 will remain unsecured without a timeout value. Always verify the full line scope for switches (`0 15`).
* **🎯 Mini challenge**: Why does the switch break the running configuration display into `0 4` and `5 15`? *(Answer: Because lines 0-4 have historical defaults or additional parameters like SSH explicitly bound from Lesson 4, splitting the display views).*

---

### Step 1️⃣1️⃣: Replicate Hardening Policies on Branch-S2 Switch

* **Mini-Lesson / Explanation**: To complete our security baseline deployment, we must configure our final device: the branch switch, `Branch-S2`. We will apply the legal warning banner and secure both the console port and all 16 VTY lines.
* **Commands to execute**:
```bash
Branch-S2# configure terminal
Branch-S2(config)# banner motd # UNAUTHORIZED ACCESS STRICTLY PROHIBITED #
Branch-S2(config)# line console 0
Branch-S2(config-line)# exec-timeout 5 0
Branch-S2(config-line)# line vty 0 15
Branch-S2(config-line)# exec-timeout 5 0
Branch-S2(config-line)# end

```


* **Verification commands**: Perform a comprehensive running configuration check on the final switch.
```bash
Branch-S2# show running-config | include banner
# Verify: banner motd displayed.
Branch-S2# show running-config | section line
# Verify: Both con 0 and vty lines show exec-timeout 5 0.

```


* **🚨 Common error note or Troubleshooting tip**: If you notice any typos in your banner text, simply re-type the `banner motd # [corrected text] #` command to overwrite the old banner text.
* **🎯 Mini challenge**: Save the configuration across all four devices to ensure your modifications are preserved in NVRAM.

---

### 📌 Key Takeaway

* **Legal Protection**: The `banner motd` command sets up a clear legal notice that prevents unauthorized users from claiming they accessed a device accidentally.
* **Session Management**: The `exec-timeout` command automatically logs out idle sessions, protecting the network if an administrator leaves their terminal unattended.
* **Device Profiles**: Always remember that routers typically use lines `0 4` for virtual connections, while switches use lines `0 15`. Applying security updates across all active lines ensures your entire topology remains protected.

---

Powered by Coding5s System