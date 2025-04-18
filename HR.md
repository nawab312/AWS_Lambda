
# Siddharth Singh – DevOps & Cloud Engineer Interview Preparation

## Quick Links

- [Introduction](#introduction)
- [Family Background](#family-background)
- [Troubleshooting Approach](#troubleshooting-approach)
- [Why Looking for Change](#why-looking-for-change)
- [Why Should We Hire You](#why-should-we-hire-you)
- [Strengths and Weaknesses](#strengths-and-weaknesses)
- [Why Alkira?](#why-alkira)
- [5-Year Plan](#5-year-plan)
- [Handling Pressure](#handling-pressure)
- [Challenging Situation](#challenging-situation)
- [Salary Expectation](#salary-expectation)
- [About Alkira](#about-alkira)
- [Questions for Alkira](#questions-for-alkira)

---
I'm doing great, thank you! Excited to be here and looking forward to our conversation

## Introduction
I’m Siddharth Singh, a DevOps and Cloud Engineer with 3 years of hands-on experience, currently working at Infosys.
In these 3 years, I’ve worked on two major projects. In my first project, I deployed PNB  banking application to an Amazon EKS cluster using containerization tools like Docker and Kubernetes. I also implemented monitoring with Prometheus and Grafana and centralized logging using the ELK stack.
In my second project, I led the cloud migration of core banking systems for Punjab National Bank and other regional banks. I used a wide range of AWS services like VPC, EC2, RDS, ALB, Auto Scaling, and S3. Again, I set up observability using Prometheus and Grafana.
I’m also well-versed in Terraform for IaC, and I use Python and Bash regularly for scripting and automation. Right now, I’m looking for an opportunity where I can grow further

I’m currently providing production support for Punjab National Bank (PNB) and several other Regional Rural Banks (RRBs). My day-to-day responsibilities include:
- Monitoring application health and performance (via tools like CloudWatch, Prometheus, ELK).
- Investigating and resolving issues such as slow response times, intermittent 503 errors, or connectivity failures.
- Performing root cause analysis when services degrade, especially during peak banking hours.
- Debugging issues like connection pool exhaustion, unhealthy target groups in ALB, DB query slowness, and network latency.
- Coordinating with developers and infrastructure teams to push hotfixes or scaling solutions."

In production support for banking apps like PNB and RRBs, we proactively monitor a combination of infrastructure, application, and network metrics. Some of the key metrics we track are:
- Load Balancer (ALB) Metrics – AWS CloudWatch
 - `HTTPCode_Target_5XX_Count`: Shows 503s, 504s — helps detect unhealthy backend services.
 - `TargetResponseTime`: Measures how fast the backend responds.
 - `RequestCount`: High spikes may indicate traffic surges or DDoS attacks.
- EC2 / App Layer Metrics
 - `CPUUtilization`, `MemoryUsage`, `Disk IO`: To detect resource bottlenecks.
 - `Connection Coun`t: Helps identify connection pool exhaustion.
 - `Thread Count`: If too many threads are waiting/blocked, performance degrades.
 - `Error logs`, `GC logs` (Java): For JVM-based apps.
- Application Metrics (via Prometheus/Grafana or ELK)
 - `Latency (p95, p99)`: How fast the app responds to 95% or 99% of requests.
 - `Error Rate`: % of failed API calls, HTTP 4xx/5xx.
 - `Throughput (RPS)`: Requests per second — helps in scaling decisions.
- Database Metrics (RDS / Aurora)
- Network Metrics

## Family Background
I come from a family of four. My father is an engineer at Aditya Birla’s Hindalco Industries, and my mother is a homemaker. I have a younger sister who recently completed her B.Tech from JSS Noida and is now working at InfoEdge in Noida.
Right now, we’re living in Singrauli because of my father’s job, but our hometown is Lucknow. We’re a close family and they've always supported me in everything I do.

## Troubleshooting Approach
-Understand the Problem Clearly:
 - First, I look at the exact symptoms — whether it's a pod crash, resource issue, API error, or an AWS service behaving unexpectedly. I check logs, events, metrics, and alerts using tools like kubectl, CloudWatch, Prometheus, or ELK depending on what’s available.
- Impact Analysis:
 - I quickly check how critical the issue is — whether it's affecting users, production, or just a dev environment. This helps prioritize the fix.
- Reproduce and Isolate:
 - I try to reproduce the issue in a test/staging environment if possible. This helps me narrow it down — for example, if it's related to pod limits, IAM permissions, or a config error.
- Root Cause Investigation:
 - Once I have some logs or patterns, I dig deeper. For Kubernetes, I use kubectl describe, logs, and check resource limits, probes, and PVCs. For AWS, I use CloudTrail, CloudWatch, or the AWS CLI to track errors and permissions.
- Fix and Validate:
 - After identifying the root cause, I apply the fix — whether it’s updating a manifest, adding IAM permission, modifying a load balancer config, or adjusting auto-scaling parameters. Then I validate if the issue is resolved completely.
- Document and Automate (if needed):
 - I document the root cause and the fix for the team and, if it’s something recurring, I try to automate it — like adding alerts in Prometheus/Grafana or writing a script for validation checks.
- Postmortem or Review:
 - If it was a critical issue, I do a short postmortem and suggest preventive measures so it doesn’t happen again.

## Why Looking for Change
I’ve had a great experience in my current company, but over the past few months, the client has started redistributing key technologies and responsibilities to different vendors. As a result, my involvement in meaningful, hands-on work has reduced.
I’m someone who enjoys working on challenging projects and continuously growing my skills. So, I’m looking for a new opportunity where I can stay technically involved, contribute more actively, and grow in a more stable and forward-looking environment.

## Why Should We Hire You
I believe you should hire me because I bring hands-on experience in DevOps and Cloud technologies, especially with tools like AWS, Kubernetes, Docker, Prometheus, and Terraform. I’ve worked on real-time banking projects, deploying applications to EKS and managing large-scale infrastructure on AWS, which has given me a strong foundation in production-grade deployments and monitoring.
I’m someone who learns quickly, takes ownership of my work, and enjoys solving real problems through automation and optimization. I'm also a good team player and communicator, and I’m genuinely excited about working in an environment like Alkira where I can grow, contribute, and be part of impactful projects.

## Strengths and Weaknesses
One of my key strengths is my work ethic—I’m very hardworking and dedicated to delivering quality results. I’m also a strong team player who enjoys collaborating and helping others. I believe in staying humble and learning from everyone around me.
Weakness:
As for my weakness, I can sometimes be a bit careless with small details when I’m managing multiple tasks at once. However, I’m actively working on this by keeping a detailed daily to-do list and prioritizing tasks better. This helps me stay organized and ensure nothing slips through the cracks.

My mother would say my strength is that I’m very calm and composed, even in stressful situations — I don’t panic easily, and I try to keep things peaceful around me.
As for a weakness, she would probably say I get too involved in work sometimes and forget to take breaks or take care of myself — which she reminds me about often.

My father would say my strength is that I’m very responsible — if I take ownership of something, I make sure I complete it properly.
And a weakness he’d point out is that I sometimes overthink things or double-check too much, which slows me down — but I’m working on trusting my instincts more.

## Why Alkira?
I’m really impressed by Alkira’s innovative approach to cloud networking. The way you simplify complex cloud architectures and enable seamless multi-cloud operations is something I’m very passionate about. I’ve worked with AWS and Kubernetes, and I believe Alkira’s solutions could help me grow in those areas while contributing to exciting and meaningful projects.

The opportunity to work with a forward-thinking company like Alkira, which is pushing the boundaries of cloud technologies, really excites me. I’m looking for a role where I can work on challenging problems and grow my skills, and I see Alkira as the perfect place for that.

## 5-Year Plan
In the next five years, I see myself diving deeper into AI and machine learning. These fields are evolving really fast, and I think they have a huge potential to make a difference in how we work. At Alkira, I’d love to integrate these technologies into my work to improve processes and bring in new efficiencies.

On top of that, I also see myself growing within the company, taking on more responsibilities, and eventually leading projects or teams to help drive Alkira’s success. I’m excited about the opportunities for both personal and professional growth here.

## Handling Pressure
When I’m under pressure or working with tight deadlines, I first try to stay calm and break down the tasks into smaller, more manageable chunks. I prioritize what needs to be done right away and what can wait a bit.

I also communicate with my team and stakeholders early on if I feel like there’s a risk of missing a deadline so we can plan accordingly or adjust expectations. Staying organized and focused helps me manage pressure, and I’ve learned that staying proactive and not getting overwhelmed makes all the difference.

## Challenging Situation
One of the most challenging situations I faced was during the deployment of a new TAB banking module for a core banking client. Before the rollout, we were running multiple EC2 instances behind a Load Balancer, and all frontend services were served from a single folder named FE. Everything seemed stable during testing.

However, once the new service went live, we started seeing major performance issues and crashes. The TAB banking traffic was significantly higher than projected, and it was causing CPU spikes and service unavailability across all instances.

After a detailed investigation, we found that keeping everything under one frontend folder was not scalable. So, we redesigned our structure: we created separate frontend directories – FE_1, FE_2, and FE_3 – across different EC2 instances. We moved the TAB banking load entirely to FE_3, which was hosted on a high-capacity instance type optimized for compute.

We then updated the target groups in our Elastic Load Balancer to route TAB traffic specifically to FE_3, and other services to FE_1 and FE_2. This helped isolate the high load and protected the other services from being impacted.

To prevent future crashes, I also configured CloudWatch alarms and dashboards to monitor system metrics like CPU, memory, and latency. Additionally, I implemented Auto Scaling policies that added or removed EC2 instances based on real-time traffic.

This incident taught me not only the importance of modularizing deployments and traffic segregation, but also how crucial it is to proactively monitor and test under peak-load conditions, especially in financial systems where downtime is critical.

## Salary Expectation
My current CTC is ₹7 LPA, and apart from that, I also get other projects related allowing including foor and cab which roughly adds up to around ₹2.4 lakhs per year.
Considering my experience, the skills I bring in DevOps and AWS, and the benefits I'm currently receiving, I’m expecting a package around ₹11 LPA.
Of course, I’m open to discussing it further based on the role, responsibilities, and overall benefits at Alkira.

I’m definitely open to discussing the offer. While ₹11 LPA is what I’m expecting based on my skills and market research, I’m more focused on the kind of work I’ll get to do, the team, and long-term growth opportunities.
If everything aligns well, I’m happy to be flexible and have a fair discussion around the numbers.

## About Alkira
Alkira is a cloud networking company that offers a platform to simplify and secure network connectivity across multiple cloud environments. Their solution, known as Cloud Area Networking, allows businesses to connect users, sites, and applications across various cloud providers like AWS, Azure, and Google Cloud without the need for additional hardware. ​
What stands out about Alkira is its agentless, as-a-service model, which means companies can deploy and manage their networks more efficiently, with built-in security and scalability. This approach helps organizations reduce complexity and accelerate their cloud adoption strategies. ​
I also read that prominent companies like S&P Global and Warner Music Group have utilized Alkira's services to streamline their network operations. I'm particularly interested in how Alkira's innovative solutions are shaping the future of cloud networking.

## Questions for Alkira
Yes, I’d love to know — what does the growth path look like for someone in this role at Alkira? are there any exciting projects or technology shifts coming up that I might get to work on?

Sometimes, during peak traffic, our banking app (3-tier: Web → App → DB) slows down or returns HTTP 503 errors. I follow a structured approach to debug and resolve it
- Check Load Balancer (ALB/NLB) Metrics. Check `HTTPCode_ELB_5XX`, `TargetResponseTime`, `HealthyHostCount`
 - If I see 503 errors in ALB logs or high TargetResponseTime, it usually indicates backend unavailability.
- Check EC2 Target Instances (App Layer)
 - Instance health: Use DescribeTargetHealth
 - Logs: Look at app logs (/var/log, custom log path) for: Unhandled exceptions, Connection pool exhaustion, Timeout errors (e.g., when talking to DB)
   - A connection pool is a set of pre-created, reusable network connections (usually from App → DB or App → external services). All connections in the pool are currently in use, and new requests are waiting (or failing) to get a free connection.
   - What causes Connection Pool Exhaustion?
     - Long-running DB queries, Code doesn’t release connections, App threads stuck waiting, Too many concurrent users, Small connection pool config(	e.g., Max pool size = 10 under 1000 users)
   - How to Fix It?
     - Increase pool size, Always close connections, Optimize DB queries, Add caching(	Offload frequent reads to Redis), Scale app servers(	Add more EC2 instances or containers)
 - System checks: top, htop, vmstat for CPU, memory, load avg
 - Disk IO spikes (iostat, iotop)
- Investigate Network Bottlenecks
 - VPC Flow Logs: Look for dropped packets or throttled connections
 - Route Tables & Security Groups: Misconfiguration can cause latency or blocked packets
 - Peak hours = network congestion:
   - Check bandwidth usage (CloudWatch, ifstat)
   - Use enhanced networking (ENA) for better throughput on EC2
   - Use Auto Scaling to handle peak loads
 - *In one incident, we observed network throughput maxing out on EC2 which caused slow responses during salary processing hours*
- Debug Database Layer

![image](https://github.com/user-attachments/assets/e2246613-47e7-420a-a9f7-eec52d11f5a0)

