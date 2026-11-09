Learn Kubernetes Basics

![](/_common-resources/images/flower.svg)

[Kubernetes](/docs/concepts/overview/), also known as K8s, is an open source system for automating deployment, scaling, and management of containerized applications.

It groups containers that make up an application into logical units for easy management and discovery. Kubernetes builds upon [15 years of experience of running production workloads at Google](https://queue.acm.org/detail.cfm?id=2898444), combined with best-of-breed ideas and practices from the community.

![](/_common-resources/images/scalable.svg)

#### Planet scale

Designed on the same principles that allow Google to run billions of containers a week, Kubernetes can scale without increasing your operations team.

![](/_common-resources/images/blocks.svg)

#### Never outgrow

Whether testing locally or running a global enterprise, Kubernetes flexibility grows with you to deliver your applications consistently and easily no matter how complex your need is.

![](/_common-resources/images/suitcase.svg)

#### Run K8s anywhere

Kubernetes is open source giving you the freedom to take advantage of on-premises, hybrid, or public cloud infrastructure, letting you effortlessly move workloads to where it matters to you.

To download Kubernetes, visit the [download](/releases/download/) section.

## The Absolute Beginner's Guide To Cloud Native

by Kyle Penfound, Dagger & Cortney Nickerson, Kubeshop

Watch Video

## Attend upcoming KubeCon + CloudNativeCon events

[**Japan** (Yokohama, Jul 28–30)](https://events.linuxfoundation.org/kubecon-cloudnativecon-japan/)

[**North America** (Salt Lake City, Nov 9–12)](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)

## Kubernetes Features

### [Automated rollouts and rollbacks](/docs/concepts/workloads/controllers/deployment/)

Kubernetes progressively rolls out changes to your application or its configuration, while monitoring application health to ensure it doesn't kill all your instances at the same time. If something goes wrong, Kubernetes will rollback the change for you. Take advantage of a growing ecosystem of deployment solutions.

### [Service discovery and load balancing](/docs/concepts/services-networking/service/)

No need to modify your application to use an unfamiliar service discovery mechanism. Kubernetes gives Pods their own IP addresses and a single DNS name for a set of Pods, and can load-balance across them.

### [Storage orchestration](/docs/concepts/storage/persistent-volumes/)

Automatically mount the storage system of your choice, whether from local storage, a public cloud provider, or a network storage system such as iSCSI or NFS.

### [Secret and configuration management](/docs/concepts/configuration/secret/)

Deploy and update Secrets and application configuration without rebuilding your image and without exposing Secrets in your stack configuration.

### [Automatic bin packing](/docs/concepts/configuration/manage-resources-containers/)

Automatically places containers based on their resource requirements and other constraints, while not sacrificing availability. Mix critical and best-effort workloads in order to drive up utilization and save even more resources.

### [Batch execution](/docs/concepts/workloads/controllers/job/)

In addition to services, Kubernetes can manage your batch and CI workloads, replacing containers that fail, if desired.

### [Self-healing](/docs/concepts/architecture/self-healing/#automated-recovery-from-damage)

Kubernetes restarts containers that crash, replaces entire Pods where needed, reattaches storage in response to wider failures, and can integrate with node autoscalers to self-heal even at the node level.

### [Horizontal scaling](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)

Scale your application up and down with a simple command, with a UI, or automatically based on CPU usage.

### [Vertical scaling](/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/)

Automatically adjust resource requests and limits based on actual usage patterns.

### [IPv4/IPv6 dual-stack](/docs/concepts/services-networking/dual-stack/)

Allocation of IPv4 and IPv6 addresses to Pods and Services

### [Designed for extensibility](/docs/concepts/extend-kubernetes/)

Add features to your Kubernetes cluster without changing upstream source code.

We are a [CNCF](https://cncf.io/) graduated project

![Cloud Native Computing Foundation logo](/images/cncf-logo-white.svg)
