### 🔹 Lesson #3 | Beginner | Networking

**Configure Local Users, Enable Secret and Password Encryption: Securing Device Access**

Welcome to Lesson 3! In Lesson 1, we built the physical topology, and in Lesson 2, we established the administrative identities (hostnames) for our devices. Today, we take a critical step forward in network administration: security. Our objective is to secure foundational device access by configuring local user databases, protecting the privileged execution mode, and encrypting plain-text passwords. This ensures a critical layer of defense against unauthorized access in our enterprise infrastructure.

### 💡 Analogy
Think of your network devices as rooms in a highly secure corporate building. The hostnames we configured in Lesson 2 are the nameplates on the doors. Today, we are installing the actual locks and security systems. The `enable secret` is the master key to the CEO's office. The local `username` is an employee ID badge. Finally, `service password-encryption` is like applying privacy film to the windows of the security office—it doesn't make the locks stronger, but it prevents people walking by from easily reading the passwords sitting on the desk (shoulder surfing).

---

### Step 1️⃣: Accessing HQ-R1 and Entering Global Configuration

**Mini-Lesson / Explanation**
Before we can secure our devices, we must access their Command Line Interface (CLI) and navigate to the correct configuration mode. We will start with our Headquarters router, `HQ-R1`. Just like in Lesson 2, we must elevate our privileges from User EXEC mode to Privileged EXEC mode, and then enter Global Configuration mode to make system-wide security changes.

**Commands to execute**
1. Click on the `HQ-R1` device in your workspace and navigate to the **CLI** tab.
2. Press `Enter` to wake up the console.
3. Execute the following commands to elevate privileges and enter global configuration:

```bash
enable
configure terminal
```

**Verification commands**
To verify that you have successfully entered the correct mode to make global changes, check your current prompt and privilege level:

```bash
show privilege
```

*Observation:* The output should display `Current privilege level is 15`, and your prompt should read `HQ-R1(config)#`. This confirms you have the necessary administrative rights to alter the device's security posture.

**🚨 Common error note or Troubleshooting tip**
If you see `HQ-R1>` instead of `HQ-R1#`, you are still in User EXEC mode. You cannot enter `configure terminal` from this mode. Always ensure you type `enable` first and see the `#` prompt.

**🎯 Mini challenge**
If you type `disable` at the `HQ-R1#` prompt, what will the prompt change to, and what privilege level will you be operating at?

---

### Step 2️⃣: Securing Privileged EXEC Mode on HQ-R1

**Mini-Lesson / Explanation**
The Privileged EXEC mode (the `#` prompt) grants full access to view and modify the device's configuration. By default, it has no password, meaning anyone with physical console access can take full control. We must secure this using the `enable secret` command. Unlike the older `enable password` command, `enable secret` uses a strong MD5 cryptographic hash to protect the password, ensuring it cannot be easily read if someone views the configuration file.

**Commands to execute**
While in global configuration mode on `HQ-R1`, execute the following command to set the privileged mode password. For this lab, we will use `class` as the secret:

```bash
enable secret class
```

**Verification commands**
Verify that the enable secret has been applied and is properly hashed in the configuration:

```bash
show running-config | include enable secret
```

*Observation:* The output should display `enable secret 5 $1$mERz$...` (the exact hash string will vary). The `5` indicates it is using MD5 hashing, which is exactly what we want to see.

**🚨 Common error note or Troubleshooting tip**
Never use the `enable password` command in a real-world or production environment. It stores the password in plain text (Type 0), which is a massive security vulnerability. Always use `enable secret`.

**🎯 Mini challenge**
If you configure both `enable password cisco` and `enable secret class` on the same router, which password will the router actually require when you type `enable` from User EXEC mode, and why?

---

### Step 3️⃣: Creating a Local Administrative User on HQ-R1

**Mini-Lesson / Explanation**
Relying solely on the enable secret is not a best practice for enterprise environments. Instead, we should create specific local user accounts. This allows for better accountability. We will create a user named `admin` and assign it a privilege level of `15`, which grants full administrative rights identical to the enable secret. We will use the `secret` keyword to ensure this user's password is also strongly hashed.

**Commands to execute**
Create the local user account with the following command:

```bash
username admin privilege 15 secret admin123!
```

**Verification commands**
Verify that the user has been created and the password is hashed:

```bash
show running-config | include username
```

*Observation:* The output should display `username admin privilege 15 secret 5 $1$...`. Again, the `5` confirms the password is securely hashed using MD5, not stored in plain text.

**🚨 Common error note or Troubleshooting tip**
If you omit the `secret` keyword and just type `username admin privilege 15 admin123!`, the router will store the password in plain text (Type 0). Always explicitly use the `secret` keyword for local user passwords.

**🎯 Mini challenge**
What privilege level would you assign to a junior technician who only needs to view the configuration and run basic troubleshooting commands, but should not be allowed to make changes?

---

### Step 4️⃣: Applying Local Authentication to the Console on HQ-R1

**Mini-Lesson / Explanation**
Creating a local user database is useless if the device doesn't know it needs to use it. By default, the console port (the physical port you use to connect a laptop directly to the router) does not require a password. We must enter the line configuration mode for the console and explicitly tell it to use the `local` user database we just created.

**Commands to execute**
Enter the console line configuration and apply local authentication:

```bash
line console 0
login local
exit
```

**Verification commands**
Verify that the console line is configured to use local authentication:

```bash
show running-config | include login local
```

*Observation:* The output should display `login local` under the `line con 0` section. This confirms that the console port will now prompt for a username and password from our local database.

**🚨 Common error note or Troubleshooting tip**
If you type just `login` without the `local` keyword, the router will prompt for a password, but it will look for a specific line password (configured via the `password` command under the line), not your local user database. Always use `login local` when using local usernames.

**🎯 Mini challenge**
If you disconnect your console cable and reconnect it, what exact sequence of prompts will appear on your screen before you are granted access to the CLI?

---

### Step 5️⃣: Encrypting Plain-Text Passwords on HQ-R1

**Mini-Lesson / Explanation**
While `enable secret` and local user `secret` commands use strong MD5 hashing, other configuration commands (like VTY line passwords or SNMP community strings) might still be stored in plain text. The `service password-encryption` command applies a Type 7 encryption to all current and future clear-text passwords in the configuration. While Type 7 is easily cracked by hackers, its primary purpose is to prevent "shoulder surfing"—stopping someone looking over your shoulder or glancing at a screen from reading your passwords.

**Commands to execute**
Apply the global password encryption service and return to privileged EXEC mode:

```bash
service password-encryption
exit
```

**Verification commands**
Verify that the encryption service is active and observe the encrypted passwords:

```bash
show running-config | include password
```

*Observation:* You will see that any clear-text passwords (if you had configured any) are now replaced with a string of seemingly random characters, typically starting with `^]` or similar symbols. This indicates Type 7 encryption is active.

**🚨 Common error note or Troubleshooting tip**
A common misconception is that `service password-encryption` makes your `enable secret` or local user `secret` stronger. It does not. Those are already hashed with MD5 (Type 5). This service only affects weak, clear-text (Type 0) passwords.

**🎯 Mini challenge**
If you copy the encrypted Type 7 password string from the `show running-config` output and paste it into an online "Type 7 Cisco Decryptor" tool, what will the tool return?

---

### Step 6️⃣: Verifying the Security Baseline on HQ-R1

**Mini-Lesson / Explanation**
Before we roll out this security configuration to the rest of the network, we must perform a comprehensive verification on `HQ-R1`. We need to ensure that the enable secret is hashed, the local user is created with the correct privilege level, the console is using local authentication, and the password encryption service is active. This final check guarantees our baseline is solid.

**Commands to execute**
Perform a targeted verification of all the security configurations we applied in this lesson:

```bash
show running-config | include secret|login|password
```

**Verification commands**
Analyze the output of the verification command carefully:

*Observation:* 
1. You should see `enable secret 5 ...` (MD5 hashed).
2. You should see `username admin privilege 15 secret 5 ...` (MD5 hashed).
3. You should see `service password-encryption`.
4. You should see `login local` under the console line. 
If all four elements are present and correctly formatted, `HQ-R1` is fully secured.

**🚨 Common error note or Troubleshooting tip**
If you see `enable secret 0 ...` or `username admin ... 0 ...`, it means the passwords are in plain text. This usually happens if you typed the commands incorrectly in Steps 2 or 3. You must remove the incorrect command (using `no enable secret` or `no username admin`) and re-enter it correctly.

**🎯 Mini challenge**
If you save the configuration and reboot `HQ-R1`, will the `service password-encryption` command still be active? How do you know which commands are saved across reboots?

---

### Step 7️⃣: Replicating the Security Baseline Across the Enterprise

**Mini-Lesson / Explanation**
A network is only as secure as its weakest link. If we secure `HQ-R1` but leave `Branch-R2`, `HQ-S1`, and `Branch-S2` unconfigured, an attacker could simply target the branch switch to gain access to the network. We must apply the exact same security baseline to all remaining devices. To do this efficiently, we will use a consolidated configuration block for each device, ensuring uniform credential management across the entire enterprise topology.

**Commands to execute**
Access the CLI of `Branch-R2`, `HQ-S1`, and `Branch-S2` one by one. For each device, execute the following consolidated configuration block:

```bash
enable
configure terminal
enable secret class
username admin privilege 15 secret admin123!
line console 0
login local
exit
service password-encryption
exit
copy running-config startup-config
```

**Verification commands**
On each of the three remaining devices, verify that the security baseline matches `HQ-R1` and that the hostnames from Lesson 2 are still intact:

```bash
show running-config | include hostname|secret|login local
```

*Observation:* 
- For `Branch-R2`, you should see `hostname Branch-R2` alongside the security commands.
- For `HQ-S1`, you should see `hostname HQ-S1` alongside the security commands.
- For `Branch-S2`, you should see `hostname Branch-S2` alongside the security commands.
All devices must show the hashed `enable secret`, the hashed `username`, and `login local`.

**🚨 Common error note or Troubleshooting tip**
When copy-pasting or typing rapidly across multiple devices, it is incredibly easy to apply the `Branch-R2` configuration while looking at the `HQ-S1` CLI tab. Always verify the device name at the very top of the Packet Tracer window before executing the `copy running-config startup-config` command.

**🎯 Mini challenge**
Recall from Lesson 1 that `BR-PC3` is connected to `Branch-S2` on port `F0/1`. If an attacker physically unplugs `BR-PC3` and plugs their own laptop into port `F0/1` on the switch, will they be prompted for the console password we just configured? Why or why not?

---

### 📌 Key Takeaway
In this lesson, you transitioned from basic device identification to foundational network security. You learned to protect the Privileged EXEC mode using the strongly hashed `enable secret` command, and you created a local user database with specific privilege levels. By applying `login local` to the console port, you enforced authentication for physical access. Finally, you utilized `service password-encryption` to protect clear-text credentials from shoulder surfing. Applying these configurations uniformly across all routers and switches ensures a consistent, secure baseline for your enterprise network.

Powered by Coding5s System