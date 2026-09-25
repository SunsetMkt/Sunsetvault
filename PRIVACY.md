# Privacy Policy for Sunsetvault

This Privacy Policy explains how the **Sunsetvault** browser extension ("Sunsetvault", "the Extension", "we", or "this project") handles user information and personal data.

---

### 1. Disclaimer and Non-Affiliation
**Sunsetvault is an independent open-source custom build and is NOT affiliated with, authorized by, endorsed by, or in any way officially connected with Bitwarden, Inc. or any of its subsidiaries or affiliates.**  
The official Bitwarden website is located at [https://bitwarden.com](https://bitwarden.com). The name "Bitwarden" and any related trademarks, emblems, or logos belong to their respective owners.

---

### 2. Source Code, Patches, and Reproducible Builds
* **Upstream Codebase:** Sunsetvault is built directly from the latest release tags of the official open-source [Bitwarden Browser extension](https://github.com/bitwarden/clients).
* **Open-Source Patches:** The build applies a minimal set of transparent, open-source patches located within this repository.
* **Reproducible Builds:** Sunsetvault artifacts are compiled using public, verifiable GitHub Actions workflows hosted directly in this repository. Build configurations and workflow logs are publicly visible to ensure that the published artifact hashes are verifiable and reproducible.

---

### 3. Maintainer Data Collection (Zero-Telemetry Policy)
**The maintainers of Sunsetvault do NOT collect, transmit, log, store, or sell any personal information, vault data, or telemetry.**

* We do not operate any telemetry services, proxies, or analytics platforms for this extension.
* The maintainers have zero access to your master passwords, encryption keys, stored credentials, IP addresses, or browsing activities.

---

### 4. Data Processing and Server Endpoints
How your personal data (such as login credentials, notes, and session tokens) is collected, stored, and transmitted is determined solely by the underlying open-source Bitwarden codebase and the **server endpoint you choose to connect to**:

* **Self-Hosted / Private Servers:**  
  Sunsetvault is intended to connect to private server instances (such as a self-hosted Bitwarden or Vaultwarden server). When connected to a self-hosted instance, all encrypted data is transmitted directly and exclusively between your browser and your private server. The server owner/operator is entirely responsible for the privacy, logging, and data retention policies of that instance.
* **Official Bitwarden Cloud Servers:**  
  If you choose to configure the extension to connect to Bitwarden’s official cloud servers, your data is processed directly by Bitwarden, Inc. In that scenario, your data collection and handling are subject to the official [Bitwarden Privacy Policy](https://bitwarden.com/privacy/).

---

### 5. Browser Permissions
All browser permissions requested by Sunsetvault (e.g., `storage`, `activeTab`, `contextMenus`, `webRequest`, clipboard access) are strictly inherited from upstream Bitwarden. These permissions are used exclusively to enable core extension functions, including:
* Storing locally cached, encrypted vaults in your browser’s local storage.
* Detecting input fields and autofilling credentials on websites you browse.
* Copying credentials and handling clipboard clearing.

---

### 6. Verification and Inquiries
All patches, build scripts, and workflow definitions are hosted in this repository for full public inspection. 

If you have questions, feedback, or security concerns regarding this custom build or this policy, please open an issue in this repository's **Issues** section.
