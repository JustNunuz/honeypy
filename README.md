```
██╗  ██╗ ██████╗ ███╗   ██╗███████╗██╗   ██╗██████╗ ██╗   ██╗
██║  ██║██╔═══██╗████╗  ██║██╔════╝╚██╗ ██╔╝██╔══██╗╚██╗ ██╔╝
███████║██║   ██║██╔██╗ ██║█████╗   ╚████╔╝ ██████╔╝ ╚████╔╝
██╔══██║██║   ██║██║╚██╗██║██╔══╝    ╚██╔╝  ██╔═══╝   ╚██╔╝
██║  ██║╚██████╔╝██║ ╚████║███████╗   ██║   ██║        ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝        ╚═╝
```

![HoneyPy](assets/honeypy.jpeg)

# About


**Honeypy** = **honey**pot + **py**thon.

A honeypot is a decoy system designed to attract and trap hackers. This repository is a Python implementation of honeypots, utilizing port binding to emulate both a basic SSH server and a web server. It logs activities such as IP addresses used to log in, commands executed, and credentials entered. Port binding is employed to associate the honeypot with a specific port on a single machine, allowing for easy testing and deployment.

## Why Honeypots?

Why would you use one? Here are some key reasons:

1. **Early Detection**: Honeypots help you identify breaches or intrusions before they can cause significant damage.
2. **Attack Analysis**: They allow you to observe and analyze attacker behavior, tools, and techniques.
3. **Incident Response Testing**: Honeypots provide a controlled environment to test and refine your incident response procedures.

---

## Types of Honeypots

| **Type**                 | **Description**                                                                                                                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Production Honeypots** | Deployed within an organization's production environment. Mimic real systems to lure attackers away from critical assets. Focused on early detection rather than detailed attack analysis.                               |
| **Research Honeypots**   | Used by security researchers to study attack techniques and trends. Often more complex and designed to capture detailed information about attacks. Operate outside of production environments, with no legitimate users. |
| **Low-Interaction**      | Simulate basic system functionality. Easy to set up and maintain but provide limited information about attackers. Examples include emulated services like SSH or HTTP servers.                                           |
| **High-Interaction**     | Fully functional systems that replicate real services and operating systems. Provide in-depth insights into attacker behavior. Require more resources to set up and monitor.                                             |
| **Malware Honeypots**    | Specifically designed to attract and capture malicious software. Help analyze malware behavior and propagation methods.                                                                                                  |
| **Spam Honeypots**       | Target spammers by emulating email servers or open relays. Collect data about spam campaigns and distribution methods.                                                                                                   |
| **Database Honeypots**   | Simulate database systems to attract attackers seeking sensitive information. Capture SQL injection attempts and other database-specific attacks.                                                                        |
