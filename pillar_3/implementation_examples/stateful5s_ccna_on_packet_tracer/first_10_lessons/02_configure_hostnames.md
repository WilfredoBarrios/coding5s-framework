### 🔹 Lesson #2 | Beginner | Networking

**Configure Device Hostnames: Establishing Administrative Identity**

Welcome to Lesson 2! In our previous session, we successfully built the physical topology, connecting our routers, switches, and PCs. However, a physical network is only half the battle. Today, our objective is to establish foundational administrative control by systematically applying unique, standard-compliant identifiers to our network devices. In real-world enterprise environments, precise hostname configuration is a critical prerequisite for accurate syslog monitoring, secure SSH remote management, and comprehensive network documentation.

### 💡 Analogy
Imagine walking into a massive corporate headquarters where no one is wearing a name badge, and the rooms have no numbers. If a security incident occurs, the security team’s report would just say, "An unknown person in an unmarked room accessed the server." By assigning hostnames, we are essentially issuing digital name badges and room numbers to every device. When a log entry says "HQ-R1 denied SSH access," you know exactly which device, in which location, experienced the event.

---

### Step 1️⃣: Accessing Privileged EXEC Mode on the HQ Router

**Mini-Lesson / Explanation**
Before we can change how a device identifies itself, we must understand the Cisco IOS command hierarchy. When you first open the CLI of a router, you are in **User EXEC mode** (indicated by the `>` prompt). This mode is highly restricted, meant only for basic monitoring. To make configuration changes, we must elevate our permissions to **Privileged EXEC mode** (indicated by the `#` prompt) using the `enable` command. This is the gateway to all administrative tasks.

**Commands to execute**
1. Click on the `HQ-R1` device in your workspace and navigate to the **CLI** tab.
2. Press `Enter` to wake up the console.
3. Execute the following command to elevate your privileges:

```bash
enable
```

**Verification commands**
To verify that you have successfully entered Privileged EXEC mode, check your current privilege level:

```bash
show privilege
```

*Observation:* The output should display `Current privilege level is 15`. This confirms you have successfully elevated from User EXEC (level 1) to Privileged EXEC (level 15). You will also notice the prompt has changed from `Router>` to `Router#`.

**🚨 Common error note or Troubleshooting tip**
A frequent beginner mistake is trying to type configuration commands (like `hostname`) while still in User EXEC mode. If the router replies with `% Invalid input detected at '^' marker`, you are likely in the wrong mode. Always ensure you see the `#` prompt before proceeding.

**🎯 Mini challenge**
If you need to step down from Privileged EXEC mode back to User EXEC mode without exiting the CLI entirely, what command would you use?

---

### Step 2️⃣: Configuring and Saving the HQ Router Identity

**Mini-Lesson / Explanation**
Now that we have administrative access, we must enter **Global Configuration mode**. This mode allows us to make changes that affect the entire device globally. We will apply the hostname `HQ-R1` to clearly identify this device as the primary router at the Headquarters. Furthermore, we must save this configuration to the `startup-config` file; otherwise, our changes will be lost the moment the device reboots.

**Commands to execute**
Execute the following sequence to enter configuration mode, apply the hostname, and save it:

```bash
configure terminal
hostname HQ-R1
exit
copy running-config startup-config
```
*(Note: When prompted with `Destination filename [startup-config]?`, simply press `Enter` to accept the default).*

**Verification commands**
Verify that the hostname has been applied and saved in the running configuration:

```bash
show running-config | include hostname
```

*Observation:* The output should explicitly show `hostname HQ-R1`. The prompt should also now read `HQ-R1#`, reflecting the new identity.

**🚨 Common error note or Troubleshooting tip**
When executing the `copy` command, many students accidentally type `copy startup-config running-config` (which overwrites your new config with the old one). Always remember the flow: you are copying the **running** (active) config **to** the **startup** (saved) config.

**🎯 Mini challenge**
If you were to reboot `HQ-R1` right now *without* running the `copy running-config startup-config` command, what would the hostname revert to?

---

### Step 3️⃣: Configuring and Saving the Branch Router Identity

**Mini-Lesson / Explanation**
With the Headquarters router identified, we move to the Branch site. In Lesson 1, we connected `HQ-R1` to `Branch-R2` via a Cross-Over cable on ports `G0/0/0`. Now, we must ensure the branch router is also uniquely identified. The process is identical to the HQ router, reinforcing the standard operational procedure for deploying Cisco devices. Consistency in these steps is key to building muscle memory for the CCNA exam and real-world deployments.

**Commands to execute**
1. Click on the `Branch-R2` device in your workspace and open the **CLI** tab.
2. Execute the following commands to elevate privileges, configure the hostname, and save:

```bash
enable
configure terminal
hostname Branch-R2
exit
copy running-config startup-config
```

**Verification commands**
Verify the configuration on the branch router:

```bash
show running-config | include hostname
```

*Observation:* The output must display `hostname Branch-R2`, and your CLI prompt should now read `Branch-R2#`. This confirms the device knows its identity and has saved it.

**🚨 Common error note or Troubleshooting tip**
When switching between devices in Packet Tracer, it is easy to lose track of which CLI tab you are looking at. Always double-check the device name at the top of the CLI window. Typing `hostname Branch-R2` inside the `HQ-R1` CLI by mistake will cause naming conflicts and documentation errors.

**🎯 Mini challenge**
Look at the physical topology from Lesson 1. `Branch-R2` is connected to `HQ-R1` via `G0/0/0`. Why is it crucial for a network administrator that the CLI hostname perfectly matches the physical location label on the server rack?

---

### Step 4️⃣: Configuring the Headquarters Switch Identity

**Mini-Lesson / Explanation**
Next, we configure the switch at the Headquarters. In Lesson 1, we connected `HQ-R1` to `HQ-S1` using a Straight-Through cable from `G0/0/1` to `G0/1`. Switches run the same Cisco IOS as routers, but their default prompt is `Switch>`. We will apply the hostname `HQ-S1` to distinguish it as the primary access-layer switch at the Headquarters, where end devices like `HQ-PC1` and `HQ-PC2` will eventually connect.

**Commands to execute**
1. Click on the `HQ-S1` device and open the **CLI** tab.
2. Execute the standard sequence to configure and save the identity:

```bash
enable
configure terminal
hostname HQ-S1
exit
copy running-config startup-config
```

**Verification commands**
Verify the switch's new identity:

```bash
show running-config | include hostname
```

*Observation:* The output should show `hostname HQ-S1`. The prompt will change to `HQ-S1#`. Notice that even though it is a switch, the command structure and privilege levels remain identical to the routers.

**🚨 Common error note or Troubleshooting tip**
Switches do not have the exact same hardware interfaces as routers, but the IOS navigation is the same. A common error is trying to configure an IP address directly on a switch port (like `F0/1`) without assigning it to a VLAN interface. For this step, strictly focus on the hostname and saving the configuration.

**🎯 Mini challenge**
Since `HQ-S1` is connected to `HQ-PC1` on port `F0/1` and `HQ-PC2` on port `F0/6` (from Lesson 1), how does having the standardized hostname `HQ-S1` help you when writing interface descriptions for those specific ports later?

---

### Step 5️⃣: Finalizing the Branch Switch and Global Verification

**Mini-Lesson / Explanation**
The final device in our core infrastructure is the Branch switch, `Branch-S2`. In Lesson 1, we connected this switch to `Branch-R2` via `G0/0/1`, and it hosts `BR-PC3` and `BR-PC4` on ports `F0/1` and `F0/6`. Once we configure and save this last device, we must perform a global mental verification across our entire topology. Ensuring every device has a saved, unique hostname is the baseline for all future troubleshooting, logging, and remote access configurations.

**Commands to execute**
1. Click on the `Branch-S2` device and open the **CLI** tab.
2. Execute the final configuration sequence:

```bash
enable
configure terminal
hostname Branch-S2
exit
copy running-config startup-config
```

**Verification commands**
Verify the final device, and then conceptually verify the entire Lesson 1 topology:

```bash
show running-config | include hostname
```

*Observation:* The output must display `hostname Branch-S2`. 
*Global Verification:* Mentally check your workspace. You should now have four network devices (`HQ-R1`, `Branch-R2`, `HQ-S1`, `Branch-S2`) all displaying their correct, saved hostnames in their CLI prompts, while the four PCs (`HQ-PC1`, `HQ-PC2`, `BR-PC3`, `BR-PC4`) retain their GUI display names.

**🚨 Common error note or Troubleshooting tip**
The "I'll save it later" trap is a critical error in networking. If you configure the last device and close Packet Tracer without running `copy running-config startup-config`, that specific device will revert to its default factory name upon reboot. Always make saving the configuration an automatic, non-negotiable final step for every device you touch.

**🎯 Mini challenge**
If you type `show hosts` on `Branch-S2`, it will display the name resolution cache. Since we haven't configured DNS yet, what does this command tell you about how the device currently resolves names, and why is having a correct local hostname still important for the `show hosts` output?

---

### 📌 Key Takeaway
In this lesson, you established the administrative identity of your enterprise network. You mastered the Cisco IOS hierarchy by navigating from User EXEC to Privileged EXEC (`enable`), and into Global Configuration (`configure terminal`). You learned how to apply standard-compliant hostnames (`hostname`) to routers and switches, and crucially, you understood the importance of persisting these changes to non-volatile memory (`copy running-config startup-config`). A properly named and saved network is the foundation of effective monitoring, security, and troubleshooting.

Powered by Coding5s System