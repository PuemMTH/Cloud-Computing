<script setup lang="ts">
  import WelcomeItem from './WelcomeItem.vue'
  import DocumentationIcon from './icons/IconDocumentation.vue'
  import ToolingIcon from './icons/IconTooling.vue'
  import EcosystemIcon from './icons/IconEcosystem.vue'
  import CommunityIcon from './icons/IconCommunity.vue'
</script>

<template>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>
      Client
    </template>

    This project was created with <a href="https://v3.vuejs.org/" target="_blank" rel="noopener"
      >Vue 3</a> it is a client for the LoadBalancer project.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading>
      Nginx Server
    </template>
    Nginx is a web server that can also be used as a reverse proxy, load balancer, mail proxy, and HTTP cache.
    In this project, we use Nginx as a reverse proxy and <a href="https://www.nginx.com/" target="_blank" rel="noopener"
      >load balancer</a>.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <EcosystemIcon />
    </template>
    <template #heading>
      Node.js Server
    </template>
    Node.js is an open-source, cross-platform, back-end JavaScript runtime environment that runs on the V8 engine and executes JavaScript code outside a web browser.
    
    <a href="https://puem.tech/" target="_blank" rel="noopener"
      >In this project</a>, we use Node.js as a server to handle the requests from the client.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <CommunityIcon />
    </template>
    <template #heading>
      Rendering from Server 1
    </template>

    Server is running in container in rasp pi 4 server and it is rendering the client request.

    Server Name: Server 1
    IP Address: 
    
  </WelcomeItem>
</template>
