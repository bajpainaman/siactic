

# Sciatic Protocol

<img src="sciatic.jpg" alt="Description of image" width="400" height="400"/>

## Summary (TL;DR)

**Sciatic Protocol** is an open protocol for decentralized machine learning, enabling universal discovery and interaction of services from any Sciatic-enabled platform. The protocol comprises multiple layers, similar to BECKN, and includes:

- **Application Layer**
- **Network and Transaction Layer**
- **Infrastructure and Security Layer**
- **Certification Layer**
- **Specification and Support Layer**

The decentralized architecture and multi-layered structure ensure secure, privacy-protected interactions and seamless integration of machine learning services across various consumer interfaces.

**Sciatic Protocol** is an open, decentralized protocol designed to enable seamless discovery, communication, and transactions between machine learning entities across any platform. By integrating services from various machine learning providers, Sciatic Protocol facilitates the co-creation of advanced AI solutions.

## The Future of LLMs: Fragmentation and Personalization

In today's landscape, there are only a handful of Large Language Models (LLMs) that are structured with specific input and output pipelines. This rigidity forces users to modify their inputs, outputs, and even the data they've accumulated over years to fit the constraints of these models. Training and inference with LLMs require substantial time and financial investment, with the necessary infrastructure being accessible only to a few large organizations. This scenario is reminiscent of the software development landscape of the 1980s and 1990s.

**Sciatic Protocol** aims to revolutionize this by leveraging the power of an open network. We propose breaking down LLMs, data banks, and compute resources into smaller, manageable chunks—building blocks that can be assembled into a framework tailored to your personal use case. This approach enables the creation of models that align with specific input and output requirements without the prohibitive costs. Furthermore, it empowers the community to develop and chain together models that cater to their unique needs over an open network, thereby fostering the development of use case-specific models.

Welcome to **Sciatic**—where the future of LLMs is decentralized, personalized, and accessible to all.

## Overview

Sciatic Protocol comprises open specifications, including protocol APIs, message formats, network designs, and reference architectures. These components allow multiple entities to execute machine learning transactions, discover resources, and intercommunicate without requiring a shared platform.

This server-to-server communication protocol empowers any consumer-facing online platform to interact with machine learning services with minimal implementation overhead. By decoupling demand-side digital infrastructure (applications and channels) from supply-side service provisioning infrastructure, Sciatic Protocol makes integrated machine learning services accessible on any mainstream consumer interface, such as online maps, messaging apps, wallets, and voice assistant apps.

Sciatic Protocol is not a platform but a protocol that adopts a decentralized architecture, eliminating the need for a centralized platform to integrate services from multiple providers. It ensures privacy and security by design, enabling secure, encrypted interactions between entities.

## Core Specification

The **Sciatic Protocol - Core Specification** defines a generic, abstracted API enabling domain-agnostic, interoperable machine learning transactions between entities across different platforms. It functions similarly to the SMTP specification, which facilitates email communication between any two platforms implementing the same specification.

The core specification includes APIs for the following machine learning events:

### Discovery
- Platform discovery
- Model browsing
- Filtering
- Dataset viewing

### Transaction
- Initiating model training
- Performing inference
- Parameter tuning
- Confirming transactions

### Execution
- Tracking progress
- Updating models
- Canceling tasks
- Status updates

### Post-Execution
- Rating models
- Providing feedback
- Support
- Managing model updates and replacements

## Inter-Model Communication

To enable this, Sciatic  provides a robust framework that includes standard interfaces, communication protocols, and integration mechanisms.


### Communication Protocols

Sciatic Protocol includes protocols for efficient and reliable data exchange:

- **Request-Response Pattern:** For synchronous, real-time communication.
- **Publish-Subscribe Pattern:** For asynchronous communication, suitable for continuous learning.
- **Message Queueing:** Manages high-throughput and bursty traffic, ensuring no data loss.

### Integration Mechanisms

Sciatic Protocol facilitates complex workflows and pipelines:

- **Workflow Orchestration:** Allows sequential or parallel model workflows.
- **Data Pipeline Integration:** Models consume and feed data into pipelines.
- **Event-Driven Architecture:** Enables dynamic interactions based on events.

### Standard Interfaces
Standard interfaces for various model types (e.g., classifiers, regressors, neural networks) ensure interaction regardless of underlying implementations.

## Packet Structure

All communications using Sciatic Protocol follow this packet structure:

|  Field        |    Description                                                                                |
|---------------|-----------------------------------------------------------------------------------------------|
|  `context`    |    Contains header information for packet switching, key lookup, and encryption               |
|  `message`    |    Contains transaction information visible only to the transaction participants              |

## Transport Protocol

Although Sciatic Protocol is transport agnostic, HTTP is the default transport protocol. Additional security layers, like HTTPS and SSL, are recommended to secure communications.

## Use Cases

### 1. **Model Training and Deployment**
**Scenario:** A data science team trains and deploys a machine learning model using resources from multiple cloud providers.

- **Discovery:** The team discovers datasets and model training services across different cloud platforms using Sciatic Protocol.
- **Transaction:** They initiate model training on Platform A, involving parameter tuning and optimization.
- **Execution:** The model is evaluated on Platform B for performance metrics and compared with benchmarks.
- **Post-Execution:** Feedback and updates are exchanged to improve model accuracy and efficiency over time.

### 2. **Ensemble Learning and Model Fusion**
**Scenario:** A fintech company improves fraud detection by combining outputs from multiple anomaly detection models.

- **Discovery:** The company discovers and evaluates various anomaly detection models across different AI service providers.
- **Transaction:** They implement an ensemble learning approach, fusing outputs from different models to achieve higher accuracy.
- **Execution:** Real-time operations combine model outputs using specified algorithms to generate a unified fraud risk score.
- **Post-Execution:** The combined model's performance is continuously monitored and adjusted based on feedback.

### 3. **Transfer Learning and Model Adaptation**
**Scenario:** A healthcare provider deploys a pre-trained medical image classification model across multiple hospital networks.

- **Discovery:** Suitable pre-trained models and datasets for medical imaging tasks are identified from various AI vendors.
- **Transaction:** Transfer learning techniques fine-tune the pre-trained model on specific hospital datasets.
- **Execution:** The adapted model is deployed across hospital networks, performing image classification tailored to local patient demographics.
- **Post-Execution:** Continuous updates and refinements are made based on new medical data and evolving practices.

### 4. **Model Collaboration and Federated Learning**
**Scenario:** A consortium of financial institutions collaborates to improve credit scoring models while maintaining data privacy.

- **Discovery:** Compatible credit scoring models and secure data-sharing mechanisms are discovered.
- **Transaction:** Federated learning techniques train local models on proprietary data while aggregating updates centrally.
- **Execution:** Model updates are securely exchanged among institutions, enabling collaborative training without sharing sensitive information.
- **Post-Execution:** Improved credit scoring accuracy is achieved while adhering to privacy regulations.

### 5. **Multi-Modal Integration and AI Fusion**
**Scenario:** A smart city initiative integrates data from various sensors and IoT devices to optimize urban planning decisions.

- **Discovery:** Machine learning models for traffic prediction, air quality monitoring, and energy forecasting are integrated.
- **Transaction:** AI fusion techniques combine outputs from different modalities to provide real-time insights for city planners.
- **Execution:** Integrated models generate recommendations for optimizing traffic flow, reducing pollution, and enhancing energy efficiency.
- **Post-Execution:** Continuous model refinement based on real-time data and stakeholder feedback ensures adaptive urban management.


**6. **Real-Time Sentiment Analysis:**
- **Scenario:** A social media platform wants to perform real-time sentiment analysis on user posts.
- **Process:** User posts are processed by a text pre-processing model, which cleans and formats the data. The pre-processed text is then sent to a sentiment analysis model. The output sentiment scores are passed to a visualization model for displaying trends on a dashboard.
- **Benefit:** The seamless integration of models enables real-time insights into user sentiment, enhancing the platform's ability to respond to trends.

**7. **Fraud Detection in Financial Transactions:**
- **Scenario:** A bank aims to detect fraudulent transactions in real-time.
- **Process:** Transaction data is first processed by a feature extraction model, which identifies key attributes. The data is then analyzed by a fraud detection model. Suspicious transactions are flagged and sent to an alerting model, which notifies the security team.
- **Benefit:** The inter-model communication framework allows for quick detection and response to fraudulent activities, protecting the bank and its customers.

**8. **Personalized Recommendations:**
- **Scenario:** An e-commerce platform wants to provide personalized product recommendations to users.
- **Process:** User behavior data is collected and analyzed by a user profiling model. The profile data is then used by a recommendation model to generate product suggestions. The recommendations are further refined by an optimization model before being presented to the user.
- **Benefit:** The integration of multiple models ensures that users receive highly relevant and personalized recommendations, improving user experience and sales.





## Contributing

We welcome contributions to the Sciatic Protocol. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name (e.g., `feature-new-api`).
3. Make your changes and commit them with clear messages.
4. Create a pull request to merge your changes into the main repository.

## License

Sciatic Protocol is released under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or support, please contact [nb3283@drexel.edu](mailto:nb3283@drexel.edu).
