### 🔹 Lesson #4 | Beginner | Networking

**Configure SSH Remote Management and Disable Telnet: Securing Remote Access**

Welcome to Lesson 4! In our previous sessions, we built the physical topology (Lesson 1), established device identities (Lesson 2), and secured local console access with strong passwords (Lesson 3). Today, we address a critical vulnerability in network management: remote access. Our objective is to transition our infrastructure from insecure, clear-text remote management (Telnet) to encrypted sessions (SSH). You will master generating RSA crypto keys, defining domain parameters, and restricting virtual terminal (VTY) lines to exclusively accept SSH traffic, effectively mitigating eavesdropping and remote credential theft.

### 💡 Analogy
Imagine you need to send your credit card number to a colleague. If you send it via **Telnet**, it is like writing the number on the back of a postcard. Anyone who handles that postcard—the mail carrier, the sorting facility—can easily read it. If you send it via **SSH**, it is like placing the number inside a heavily encrypted, titanium briefcase with a unique digital lock. Even if someone intercepts the briefcase in transit, all they see is scrambled, useless data. In networking, we must always use the titanium briefcase.

---

### Step 1️⃣: Defining the Network Domain on HQ-R1

**Mini-Lesson / Explanation**
Before we can generate the cryptographic keys required for SSH, the router needs a sense of identity beyond just its hostname. In Lesson 2, we named our router `HQ-R1`. Now, we must assign it a domain name. The combination of the hostname and the domain name creates a fully qualified domain name (FQDN), which is mathematically required by the router to generate RSA keys. Without a domain name, the key generation command will fail.

**Commands to execute**
1. Click on the `HQ-R1` device in your workspace and navigate to the **CLI** tab.
2. Enter privileged EXEC and global configuration modes:

```bash
enable
configure terminal
```

3. Define the enterprise domain name:

```bash
ip domain-name enterprise.com
```

**Verification commands**
Verify that the domain name has been successfully applied to the global configuration:

```bash
show running-config | include domain-name
```

*Observation:* The output should explicitly display `ip domain-name enterprise.com`. This confirms the router now has the necessary naming context to proceed with cryptographic operations.

**🚨 Common error note or Troubleshooting tip**
If you attempt to generate RSA keys without configuring the `ip domain-name` first, the router will return an error: `% Invalid input detected at '^' marker` or simply refuse to generate the key. Always establish the domain name before touching crypto commands.

**🎯 Mini challenge**
If you were to change the domain name from `enterprise.com` to `branch.local` after generating the RSA keys, what would happen to the existing RSA keys, and what would the router require you to do?

---

### Step 2️⃣: Generating RSA Keys and Enforcing SSHv2 on HQ-R1

**Mini-Lesson / Explanation**
With the domain name established, we can now generate the RSA (Rivest-Shamir-Adleman) cryptographic keys. These keys are the mathematical foundation of the SSH server, used to encrypt the session and verify the device's identity. We will use a modulus of 2048 bits, which is the current industry standard for security. Furthermore, we must explicitly enforce SSH version 2, as version 1 has known cryptographic vulnerabilities and is deprecated.

**Commands to execute**
While still in global configuration mode on `HQ-R1`, execute the following commands:

```bash
crypto key generate rsa modulus 2048
ip ssh version 2
```
*(Note: When prompted to confirm the generation, type `yes` or press `Enter` depending on your IOS version).*

**Verification commands**
Verify the RSA key generation and the active SSH version:

```bash
show crypto key mypubkey rsa
show ip ssh
```

*Observation:* 
- The first command should display a long string of characters representing the public key, confirming the 2048-bit modulus.
- The second command should show `SSH Enabled` and `Configuration version: 2`. This confirms the SSH server is active and strictly using the secure v2 protocol.

**🚨 Common error note or Troubleshooting tip**
If you specify a modulus size less than 768 bits, the router will generate the key but will *not* enable the SSH server, as it considers the key too weak. Always use at least 1024, but preferably 2048 for modern enterprise baselines.

**🎯 Mini challenge**
Look at the output of `show crypto key mypubkey rsa`. The key is named `HQ-R1.enterprise.com`. How did the router automatically construct this specific name for the key?

---

### Step 3️⃣: Hardening the VTY Lines on HQ-R1

**Mini-Lesson / Explanation**
Generating keys enables the SSH server, but we must also configure the "doors" that remote users walk through. These doors are the Virtual Teletype (VTY) lines. On a Cisco 4331 router, there are typically 5 VTY lines, numbered `0` through `4`. By default, these lines might allow Telnet or have no authentication. We must restrict them to accept *only* SSH traffic and instruct them to use the local user database (`admin`) we created in Lesson 3.

**Commands to execute**
Enter the VTY line configuration mode and apply the security restrictions:

```bash
line vty 0 4
login local
transport input ssh
exit
```

**Verification commands**
Verify that the VTY lines are correctly restricted to SSH and local authentication:

```bash
show running-config | include transport
show running-config | include login local
```

*Observation:* You should see `transport input ssh` and `login local` in the output. This guarantees that any remote connection attempt via Telnet will be instantly rejected, and only users from our Lesson 3 local database can log in via encrypted SSH.

**🚨 Common error note or Troubleshooting tip**
If you type `transport input all`, you are allowing both Telnet and SSH. While SSH will still work, you have left the insecure Telnet "door" open. Always use `transport input ssh` to explicitly disable Telnet.

**🎯 Mini challenge**
If an attacker tries to connect to `HQ-R1` using a Telnet client on their PC, what exact message or behavior will they experience, given our `transport input ssh` configuration?

---

### Step 4️⃣: Replicating SSH Configuration to Branch-R2

**Mini-Lesson / Explanation**
An enterprise network is only as secure as its weakest link. Securing `HQ-R1` is useless if an attacker can simply bypass the headquarters and remotely log into `Branch-R2` via unencrypted Telnet. We must apply the exact same cryptographic and VTY hardening baseline to the branch router. This ensures uniform remote access security across all routing infrastructure.

**Commands to execute**
Access the CLI of `Branch-R2` and apply the consolidated SSH configuration block:

```bash
enable
configure terminal
ip domain-name enterprise.com
crypto key generate rsa modulus 2048
ip ssh version 2
line vty 0 4
login local
transport input ssh
exit
copy running-config startup-config
```

**Verification commands**
Verify the SSH status and VTY configuration on the branch router:

```bash
show ip ssh
show running-config | section line vty
```
*(If `section` is not supported in your PT version, use `show running-config` and scroll to the bottom).*

*Observation:* `show ip ssh` must confirm SSH is enabled on version 2. The VTY configuration block must show `login local` and `transport input ssh` applied to lines 0 through 4. The hostname in the RSA key should now read `Branch-R2.enterprise.com`.

**🚨 Common error note or Troubleshooting tip**
When copy-pasting configurations between devices, ensure you are actually in the `Branch-R2` CLI tab. Applying the `Branch-R2` configuration to `HQ-R1` will overwrite its unique RSA key identity and cause confusion in your network documentation.

**🎯 Mini challenge**
Both `HQ-R1` and `Branch-R2` are connected via their `G0/0/0` interfaces (from Lesson 1). Once we configure IP addresses in a future lesson, will the SSH traffic between these two routers be encrypted? Why or why not?

---

### Step 5️⃣: Configuring SSH on the Headquarters Switch (HQ-S1)

**Mini-Lesson / Explanation**
Routers are not the only devices that need remote management; switches do as well. In Lesson 1, we connected `HQ-S1` to `HQ-R1` and attached `HQ-PC1` and `HQ-PC2` to it. We must secure remote access to this switch. However, there is a critical hardware difference: while routers typically have 5 VTY lines (0-4), Cisco Catalyst switches like the 2960 have 16 VTY lines (0-15). We must configure the correct range to ensure all possible simultaneous remote sessions are secured.

**Commands to execute**
Access the CLI of `HQ-S1` and apply the switch-specific SSH configuration:

```bash
enable
configure terminal
ip domain-name enterprise.com
crypto key generate rsa modulus 2048
ip ssh version 2
line vty 0 15
login local
transport input ssh
exit
copy running-config startup-config
```

**Verification commands**
Verify that all 16 VTY lines on the switch are properly secured:

```bash
show running-config | begin line vty 0
```

*Observation:* You should see the configuration block for `line vty 0 15`. It is crucial that the range says `0 15` and not `0 4`. If it only says `0 4`, lines 5 through 15 remain at their default settings, potentially allowing unencrypted Telnet access.

**🚨 Common error note or Troubleshooting tip**
The most common mistake when configuring switches is blindly copying the router's `line vty 0 4` command. Always remember: Routers = `0 4`, Switches = `0 15`. Failing to configure the full range on a switch is a classic CCNA exam trap.

**🎯 Mini challenge**
If a network administrator opens 5 simultaneous SSH sessions to `HQ-S1`, they will use VTY lines 0 through 4. If they open a 6th session, which specific VTY line will the switch assign to that session, and is it protected by our `transport input ssh` command?

---

### Step 6️⃣: Finalizing Branch-S2 and Global SSH Verification

**Mini-Lesson / Explanation**
The final step in our remote access hardening is configuring the Branch switch, `Branch-S2`, and performing a global verification. `Branch-S2` hosts `BR-PC3` and `BR-PC4` (from Lesson 1) and connects to `Branch-R2`. Once configured, we must mentally and logically verify that our entire enterprise topology—both routers and both switches—shares the exact same secure remote access baseline. 

**Commands to execute**
Access the CLI of `Branch-S2` and apply the final switch configuration:

```bash
enable
configure terminal
ip domain-name enterprise.com
crypto key generate rsa modulus 2048
ip ssh version 2
line vty 0 15
login local
transport input ssh
exit
copy running-config startup-config
```

**Verification commands**
Perform a final global verification across all four network devices to ensure uniformity:

```bash
show ip ssh
show line vty 0
```

*Observation:* 
- On `HQ-R1` and `Branch-R2`, `show line vty 0` should indicate `SSH` is allowed, and `show ip ssh` confirms version 2.
- On `HQ-S1` and `Branch-S2`, the same commands should yield identical results, but remember they have 16 lines instead of 5. 
- All devices should show `login local`, meaning they will all prompt for the `admin` username and `admin123!` password (from Lesson 3) when a remote connection is attempted.

**🚨 Common error note or Troubleshooting tip**
A major "gotcha" for beginners at this stage: If you try to test your SSH connection right now from `HQ-PC1` to `HQ-R1`, **it will fail**. Why? Because SSH is a Layer 3 (Network Layer) protocol, and we have not yet configured IP addresses on our interfaces! The physical and data link layers are up (Lesson 1), and the SSH server is running (Lesson 4), but without IP addresses, the PC cannot route the SSH packets to the router. We will fix this in Lesson 5.

**🎯 Mini challenge**
Since we cannot test SSH yet due to missing IP addresses, how can you use the `show users` or `show ssh` command in Privileged EXEC mode to prove that the SSH server process is actively running and listening for connections on `HQ-R1`?

---

### 📌 Key Takeaway
In this lesson, you successfully transitioned your network infrastructure from vulnerable, clear-text remote management to robust, encrypted SSH access. You learned that generating RSA keys requires a defined `ip domain-name`, and that enforcing `ip ssh version 2` is mandatory for modern security. By configuring the VTY lines with `login local` and `transport input ssh`, you explicitly disabled Telnet and restricted remote access to your encrypted local user database. You also mastered the critical hardware distinction between router VTY ranges (0-4) and switch VTY ranges (0-15), ensuring comprehensive security across your entire enterprise topology.

Powered by Coding5s System