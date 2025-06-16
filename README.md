# Affirmation System

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&style=flat)
![Twilio](https://img.shields.io/badge/Twilio-API-red?logo=twilio&style=flat)
![OpenAI](https://img.shields.io/badge/OpenAI-API-black?logo=openai&style=flat)
![Vault](https://img.shields.io/badge/Vault-Secrets_Management-000000?logo=hashicorp&style=flat)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-326CE5?logo=kubernetes&style=flat)
![Helm Chart](https://img.shields.io/badge/Helm-Chart-blue?logo=helm)
![CI](https://github.com/damienjburks/affirmation-system/actions/workflows/main.yml/badge.svg?style=flat)
![License](https://img.shields.io/github/license/damienjburks/affirmation-system?style=flat)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat)

> 💙 _Consistency is key. Working out is vital. One message at a time, we build the habit. —Love, Damien_

## 🧠 Overview

This is a secure, AI-powered Python FastAPI application that delivers daily affirmations via SMS. It's designed for resilience, privacy, and extensibility. This service is built with modern cloud-native principles and deployed in Kubernetes with hardened Chainguard base images.

## 🚀 Features

- 🧠 **OpenAI Integration** — AI-generated affirmations tailored for motivation, health, and mindset.
- 📬 **Twilio SMS Delivery** — Sends messages directly to recipients' phones each day.
- 🔐 **Vault Secrets** — Dynamically pulls credentials for OpenAI and Twilio from HashiCorp Vault.
- ☸️ **Runs in Kubernetes** — Deployed as a standard container, but uses **Python-based scheduling** rather than Kubernetes CronJobs.
- 🐳 **Chainguard Base Image** — Lightweight, secure-by-default containers.
- ✅ **CI/CD** — Automated testing and builds via GitHub Actions (`main.yml`)

## 📜 License

MIT © 2025 [Damien J Burks](https://github.com/damienjburks)
